from slacker import Slacker
from random import randint
import os
import datetime

farm_names = ['Farmers are friends, not food','Farm to fork',
              'Farmer Land','tekraM s\'remraF','Old MacDonald\'s',
              'Real talk, does Judy have a farm fetish?','Farmfefe',
              'Goat Grotto','Sheep Sanctuary','Cow Coliseum',
              'Farm me, Daddy','To farm or not to farm','Farm-fetched',
              'EIEIO','[Insert Farm Name Here]','You guys don\'t pay me enough for this',
              'Goat Land','farm plz, we never go there','tbh the farm is pretty bad',
              'Pirates of the Farm: Dead Farmers Tell No Tales',
              'Wake up sheeple, the cow bikes are just farm propaganda',
              'F-A-R-M','https://www.youtube.com/watch?v=RVJbKPW3Crs','George Orwell',
              'F A R M A G E D D O N','Boycott the farm!']

farm_index = len(farm_names) - 1

key = os.environ.get('SLACK_API_KEY', None)

slack = Slacker(key)

lunch_poll = 'React with your lunch choice emoji, or else:\n' \
             ':sheeple: Taco Tuesday @ 11'

if(datetime.datetime.today().weekday() < 5) :
  # Send a message to #botsgonewild channel
  slack.chat.post_message('#food', lunch_poll, as_user=True)
  
#  lunch_poll = 'React with your lunch choice emoji, or else:\n' \
#             ':peach: Cass\n' \
#             ':crossed_swords: King\'s Cross\n' \
#             ':sheeple: %s\n' \
#             ':bread: This chain called Mikey\'s\n' \
#             ':sushi: Is Chopstick\'s really even open?\n' \
#             ':fire: Spit & Fire'  % (farm_names[randint(0,farm_index)])
