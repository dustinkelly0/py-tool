import requests
import boto3

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))

