import requests
import os
import json


api_key = str(os.environ.get('api_key_country', '-1'))
print("Welcome\n")
print("IP Address to Country Name\n")

ip_address = input("Enter the ip address\n")
print("Wait looking for the Country Name")
data = requests.get(f'https://api.ipdata.co/{ip_address}?api-key={api_key}').json()
print()
data_str = json.dumps(data, indent= 2)

print(data_str)



country_name = data['country_name']
country_code = data['country_code']

print(f'Country Name : {country_name} ({country_code})\n')






