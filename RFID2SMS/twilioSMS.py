from twilio.rest import TwilioRestClient
# TEST Credentials
#account_sid = 'AC20ee6335cf57634830ca28a67153643e'
#auth_token = '479a216814157e6c6bcfad31c8e3da1c'

# LIVE Credentials
account_sid = 'AC59c5760a59fc52efe5ac5d4b0a48a11b'
auth_token = '966e3ac2f5ae55d443bf4e2cb0edca12'
twilio_number = '5202140826'

def SMStwilio(mensaje, numero='+526311264764'):
    cliente = TwilioRestClient(account_sid, auth_token)
    mensaje = cliente.messages.create(to=numero, from_= twilio_number, body=mensaje)
