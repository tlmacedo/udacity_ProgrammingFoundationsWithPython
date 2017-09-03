from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACd6a736939f8ec4ced05416efc6044034"

# Your Auth Token from twilio.com/console
auth_token = "b892fc2f89a7d4e24b566c0431e77e83"

client = Client(account_sid, auth_token)
message = client.messages.create(body="Hello from Python!111",
                                 to="+5592981686148",
                                 from_="+14243416591")

print("retorno da msg: [" + message.sid + "]")
