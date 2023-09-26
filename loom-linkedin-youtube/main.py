# from linkedin import linkedin
import os
from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import requests
import string
import random

load_dotenv()

REDIRECT_URI = 'http://localhost:8000'
REDIRECT_URI_ENCODED = 'http%3A%2F%2Flocalhost%3A8000'
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

# Generate a random string to protect against cross-site request forgery
letters = string.ascii_lowercase
CSRF_TOKEN = ''.join(random.choice(letters) for i in range(24))

AUTH_CODE =''
ACCESS_TOKEN_URL = 'https://www.linkedin.com/oauth/v2/accessToken'

# auth_params = {'response_type': 'code',
#                'client_id': CLIENT_ID,
#                'redirect_uri': REDIRECT_URI_ENCODED,
#                'state': CSRF_TOKEN,
#                'scope': ['w_member_social']} #r_liteprofile,r_emailaddress,


# html = requests.get("https://www.linkedin.com/oauth/v2/authorization",
#                     params = auth_params)

# print(html.url)

authorization_base_url = "https://www.linkedin.com/oauth/v2/authorization"
scope = ["r_liteprofile","r_emailaddress","w_member_social"]
REDIRECT_URI = "http://127.0.0.1"
linkedin = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=scope)

# Redirect user to LinkedIn for authorization
authorization_url, state = linkedin.authorization_url(authorization_base_url)
print(f"Please go here and authorize: {authorization_url}")