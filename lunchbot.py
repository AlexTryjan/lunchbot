from slacker import Slacker
from boto.s3.connection import S3Connection

key = S3Connection(os.environ['SLACK_API_KEY'])

slack = Slacker(key)

# Send a message to #botsgonewild channel
slack.chat.post_message('#botsgonewild', 'Hello fellow robots!', as_user=True)