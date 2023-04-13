from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('api')
        params = {
            'sender': '',  # optional
            'receptor': str(phone_number),  # multiple mobile number, split by comma
            'message': str(code),
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
