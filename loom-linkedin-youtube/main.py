from linkedin import linkedin
import os
from dotenv import load_dotenv
import requests

load_dotenv()

APPLICATON_KEY = os.getenv('CLIENT_ID')
APPLICATON_SECRET = os.getenv('CLIENT_SECRET')

url = 'https://www.linkedin.com/oauth/v2/accessToken'
params = {
    'grant_type': 'authorization_code',
    'code': 'your_authorization_code',
    'redirect_uri': 'https://yourwebsite.com/callback',
    'client_id': 'your_client_id',
    'client_secret': 'your_client_secret'
}
response = requests.post(url, data=params)

if response.status_code == 200:
    access_token = response.json()['access_token']
    print('Access token:', access_token)
else:
    print('Error:', response.status_code, response.text)



# api_url = 'https://api.linkedin.com/v2/me'

# headers = {
#     'Authorization': f'Bearer {APPLICATON_SECRET}',
#     'Connection': 'Keep-Alive',
#     'Content-Type': 'application/json',
# }

# response = requests.get(api_url, headers=headers)
# if response.status_code == 200:
#     print('Access token is valid!')
# else:
#     print('Access token is invalid or has expired.')