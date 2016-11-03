# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
import os

# Find these values at https://twilio.com/user/account
account_sid = "AC007ffbc7fa49cdc774c904ecf0ad4dfd"
auth_token = os.getenv('TWILIO_TOKEN')
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+17084464335", from_="+12023350157 ",
                                     body="There are snakes here!")
