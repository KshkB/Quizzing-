import requests

token_url = requests.get('https://opentdb.com/api_token.php?command=request')
token_data = token_url.json()
token = token_data['token']
