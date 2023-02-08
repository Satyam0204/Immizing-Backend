import requests


url="https://api-int.uscis.gov/oauth/accesstoken"

headers={
    'content-type': 'application/x-www-form-urlencoded'
}
payload={
    'grant_type':'client_credentials',
    'client_id':'gqn06Nbgh7AYEADu0fNdUex9is2NCgch',
    'client_secret':'Cyvez6HJ3ttDYXKA'
}
response = requests.post(url,headers=headers,data=payload)
data = response.json()
access_token=data['access_token']
print(access_token)