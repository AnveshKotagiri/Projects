
import requests

import schedule
import time

#telegram bot token
Token = ""
GroupID = ""
telegram_url = "https://api.telegram.org/bot{}/sendmessage?chat_id={}&text=".format(Token,GroupID)

pincode = ""
date = ""
#I used calendarByPin Api, you can use any as per requirement
cowin_url_api = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?"


def extract_from_cowin():
    queryParams = "pincode={}&date={}".format(pincode,date)
    final_url  = cowin_url_api + queryParams
    message = requests.get(final_url)
    message_json = message.json()
    #print(message_json)
    parse_query(message_json)


def parse_query(message_json):
    for center in message_json['centers']:
        for session in center['sessions']:
            if session['min_age_limit']==18 and session['available_capacity'] > 0:
                final_message = str(center['address']) +"  "+ str(session['available_capacity'])
                print(final_message)
                send_telegram_message(final_message)


def send_telegram_message(final_message):
    final_url_request = telegram_url + final_message
    response = requests.get(final_url_request)
    print(response.text)
#print(message.text)


'''
if __name__ == "__main__":
    extract_from_cowin()
'''


schedule.every(1).minutes.do(extract_from_cowin)


while True:
    schedule.run_pending()
    time.sleep(1)



