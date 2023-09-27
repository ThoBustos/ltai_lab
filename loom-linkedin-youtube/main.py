# from linkedin import linkedin
import os
from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import requests
import string
import random

load_dotenv()

# os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


REDIRECT_URI = 'https://www.linkedin.com/developers/tools/oauth/redirect'
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN') # generated from linkedin developer tools


# user info
# headers = {"Authorization": f"Bearer {ACCESS_TOKEN}",
#         "Content-Type": "application/json"}

# response_user_info = requests.get('https://api.linkedin.com/v2/me',headers=headers)
# print(response_user_info.status_code)
# print(response_user_info.json())

# post linkedin
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json"}

body = {
    "author": "urn:li:person:X04cifWENE",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": "Hello World! This is my first Share on LinkedIn (with api)!"
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
}
  
response_post = requests.post('https://api.linkedin.com/v2/ugcPosts',headers=headers, json=body)
print(response_post.status_code)
print(response_post.json())