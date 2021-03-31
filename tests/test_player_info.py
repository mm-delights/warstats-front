import requests
import yaml
import pytest

@pytest.fixture
def xsrf_token():
    url="https://profile.callofduty.com/cod/login"
    r = requests.get(url)
    return r.cookies['XSRF-TOKEN']

def test_auth(xsrf_token):
    with open('config/dev_martin.yml') as config_file:
        config = yaml.safe_load(config_file)

    auth_url = "https://profile.callofduty.com/do_login"
    params = {
        "new_SiteId":"cod"
    }
    headers= {
       "Cookie": f"XSRF-TOKEN={xsrf_token}",
       "Connection": "keep-alive",
       "Accept": "*/*"
    }   
    payload = {
        "username": config['user'],
        "password": config['password'],
        "remember_me": True,
        "_csrf": xsrf_token
    }
    cookies={
        "XSRF-TOKEN":'xsrf_token'
    }
    r = requests.post(
        auth_url, 
        params=params, 
        data=payload, 
        cookies=cookies, 
        headers=headers, 
        timeout=5
    )
    print(r.json)