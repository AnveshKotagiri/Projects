import requests

import schedule
import time

#telegram bot token
Token = ""
telegram_url = "https://api.telegram.org/bot{}/sendmessage?chat_id=@Cowin_Self_Notifier&text=".format(Token)

pincode = "500032"
date = "11-06-2021"

cowin_url_api = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?"


def extract_from_cowin():
    queryParams = "pincode={}&date={}".format(pincode,date)
    final_url  = cowin_url_api + queryParams
    message = requests.get(final_url)
    message_json = message.json()
    #print(message_json)
    parse_query(message_json)


def parse_query(message_json):
    for session in message_json['sessions']:
        if session['min_age_limit']==18:
            final_message = str(session['address']) +"  "+ str(session['available_capacity'])
            #print(final_message)
            send_telegram_message(final_message)
     

def send_telegram_message(final_message):
    final_url_request = telegram_url + final_message
    response = requests.get(final_url_request)
   # print(response.text)
#print(message.text) 


schedule.every(1).minutes.do(extract_from_cowin)


while True:
    schedule.run_pending()
    time.sleep(1)



