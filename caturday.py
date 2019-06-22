import requests
import os
from twilio.rest import Client

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
fromNumber = os.environ['from_number']
numbers_to_message = os.environ['to_numbers'].split(',')

def its_caturday(event, context): 
    json = requests.get('https://www.reddit.com/r/aww/new.json', headers = {'User-agent': 'your bot 0.1'}).json()
    url = json['data']['children'][0]['data']['url']

    client = Client(account_sid, auth_token)

    for number in numbers_to_message:
        message = client.messages \
                        .create(
                            body=url,
                            from_=fromNumber,
                            to=number
                        )
    return url