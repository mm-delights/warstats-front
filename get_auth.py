import requests
import yaml


def xsrf_token():
    url="https://profile.callofduty.com/cod/login"
    session = requests.Session()
    r = session.get(url)
    token = r.cookies['XSRF-TOKEN']
    cookies = requests.utils.cookiejar_from_dict(requests.utils.dict_from_cookiejar(session.cookies))
    return cookies, session, token



def test_auth(cookies, session, xsrf_token):
    with open('config/dev_martin.yml') as config_file:
        config = yaml.safe_load(config_file)
    
    auth_url = "https://profile.callofduty.com/do_login"
    params = {
        "new_SiteId":"cod"
    }
    headers= {
       "Cookie": f"XSRF-TOKEN={xsrf_token}",
       "Connection": "keep-alive",
       "Content-Type": "multipart/form-data",
       "Accept": "*/*"
    }   
    payload = {
        "username": config['user'],
        "password": config['password'],
        "remember_me": True,
        "_csrf": xsrf_token
    }
    # cookies={
    #     "XSRF-TOKEN":'xsrf_token'
    # }
    r = session.post(
        auth_url, 
        params=params, 
        data=payload,
        allow_redirects=True,
        cookies=cookies, 
        headers=headers, 
        timeout=5
    )
    r.raise_for_status()
    return(r)

if __name__ == "__main__":
    cookies, session, xsrf_token = xsrf_token()
    test_auth(cookies, session, xsrf_token)