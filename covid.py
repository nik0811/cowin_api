#!/usr/bin/env python3
#AUTHOR: NIKHIL KUMAR
#EMAIL: NIKHIL811RAJ@GMAIL.COM

import time
import requests
import json

#Telegram bot

bot_token = '18983345665451:AAHAzLtVtyseYUtjvjhsffhhkFmF3IrMoKbYcJnHiIF4dw8'
bot_baseURL = 'http://api.telegram.org/bot'
bot_id = bot_baseURL + bot_token + '/getMe'
bot_headers = {'Content-Type': 'text/plain', 'charset':'utf-8'}

#bot_chat_id=requests.post(bot_id, headers=bot_headers, verify=True).json()['result']['id']
#https://api.telegram.org/bot1898365451:AAHAzLtVYUtjvFmF3IrMoKbYcJnHiIF4dw8/getUpdates

bot_chat_id='-442861707'


#COWIN API

date=time.strftime("%d-%m-%Y")
headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}

# PINCODE OF PUNE REGION
pincode=[411001, 411003, 411037, 411057, 411028, 411014, 411011, 411004, 411028, 411026, 411017, 411033]

api = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByPin?pincode=%s&date=%s"

#MAIN LOGIC
for i in pincode:
    try:
        r=requests.get(api%(i,date), headers=headers)
        j=r.json()
        center = j['centers']
        for k in center:
            name=k['name']
            address=k['address']
            pincode=k['pincode']
            fee_type=k['fee_type']
            session=k['sessions']
            available_capacity=[]
            min_age_limit=[]
            vaccine=[]
            available_capacity_dose1=[]
            available_capacity_dose2=[]
            for m in session:
                available_capacity.append(m['available_capacity'])
                min_age_limit.append(m['min_age_limit'])
                vaccine.append(m['vaccine'])
                available_capacity_dose1.append(m['available_capacity_dose1'])
                available_capacity_dose2.append(m['available_capacity_dose2'])
            main_data=("Name: %s\nAddress: %s\nPincode: %s\nMinAgeLimit: %s\nAvailableCapacityDose1: %s\nAvailableCapacityDose2: %s\nFeeType: %s\nAvailableCapacity: %s\nVaccine: %s"%(name, address, pincode, ",".join(map(str,min_age_limit)), ",".join(map(str,available_capacity_dose1)), ",".join(map(str,available_capacity_dose2)), fee_type, ",".join(map(str,available_capacity)), ",".join(map(str,vaccine))))
            bot_sendURL = bot_baseURL + bot_token + "/sendMessage?chat_id={0}".format(bot_chat_id) + "&parse_mode=Markdown&text={0}".format(main_data)
            for doses in available_capacity_dose1:
                if (doses != 0):
                    nikhil=requests.post(bot_sendURL, headers=bot_headers, verify=True)
                else:
                   print("No Doses Available")
    except:
        print("Invalid Response")
