from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC492fcc157f994608dbe07676621ad5f9"
# Your Auth Token from twilio.com/console
auth_token  = "719c2751f8fc75940649c5fde5c2c8cb"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918073670036", 
    from_="+12403924070",
    body="Hello from Python! Spam your system is to be hacked!! :-)")

print(message.sid)
