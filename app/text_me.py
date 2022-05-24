from twilio.rest import Client
from config.config import ACCOUNT_SID, AUTH_TOKEN, FROM_NUMBER, TO_NUMBER

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_=FROM_NUMBER,
    body='Hello Test SMS',
    to=TO_NUMBER
)

print(message.sid)
