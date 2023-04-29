from random import randint

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from utils import send_otp_code
from .forms import UserRegistrationForm, VerifyCodeForm, UserLoginForm
from .models import OtpCode, User


class UserRegisterView(View):
    form_class = UserRegistrationForm
    templates_class = "accounts/register.html"

    def get(self, request):
        form = self.form_class
        return render(request, self.templates_class, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            random_code = randint(1000, 9999)
            # when we connect to api service recomment this code
            send_otp_code(cd['phone'], random_code)
            OtpCode.objects.create(phone_number=cd['phone'], code=random_code)
            request.session['user_registration_info'] = {
                'phone_number': cd['phone'],
                'email': cd['email'],
                'full_name': cd['full_name'],
                'password': cd['password'],
            }
            messages.success(request, 'we send message to you', 'success')
            return redirect("accounts:verify_code")
        return render(request, self.templates_class, {'form': form})


class UserRegisterVerifyCodeView(View):
    class_form = VerifyCodeForm

    def get(self, request):
        form = self.class_form
        return render(request, 'accounts/verify.html', {'form': form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])

        form = self.class_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create(phone_number=user_session['phone_number']
                                    , email=user_session['email']
                                    , full_name=user_session['full_name']
                                    , password=user_session['password'])
                code_instance.delete()
                messages.success(request, "you registered successfully", 'success')
                return redirect("home:home")
            else:
                messages.error(request, 'code was incorrect', 'danger')
                return redirect('accounts:verify_code')
        else:
            messages.error(request, 'form got error', 'danger')
            return redirect("home:home")


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'loggout successfully', 'success')
        return redirect('home:home')


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, phone_number=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, f'{user.full_name} !! you logged in successfully', 'info')
                return redirect('home:home')
            messages.error(request, "phone number or password is incorect", 'warning')
        return render(request, self.template_name, {'form': form})
