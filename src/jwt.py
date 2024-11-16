import jwt
from datetime import datetime, timedelta

import requests


# Import the correct exception class
from requests.exceptions import HTTPError

url ="http://localhost:3000/albums/"
try: 
    r = requests.get(url) 
	# Enable raising errors for all error status_codes
    r.____()
    print(r.status_code)
# Intercept the error 
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')

def create_jwt_token(payload):
    
    # Your secret key (guard it with your life!)
    secret_key = 'supersecretkey'
    
    # Algorithm for token generation
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    
    return token

def main():
    payload = {
        'user_id': 777,
        'username': 'tom',
        'role': 'mouse_catcher',
        'exp': datetime.now() + timedelta(hours=1) # Token will expire in 1 hour
    }
    print("JWT TOKEN: ", create_jwt_token(payload))

if __name__ == "__main__":
    main()