from dotenv import load_dotenv
load_dotenv()

import requests
import os
import argparse

AUTH_TOKEN = os.getenv('AUTH_TOKEN')
SERVER_URL = 'https://api-ssl.bitly.com'
BITLY_LINKS = [
  'bit.ly/',
  'https://bit.ly/',
  'http://bit.ly',
  'https://www.bit.ly',
  'http://www.bit.ly'
]


def short_url(url, auth_token):
    headers = {
        'Authorization': f'Bearer {auth_token}'
    }

    payload = {
        'long_url': url
    }

    response = requests.post(
        f'{SERVER_URL}/v4/bitlinks',
        headers=headers,
        json=payload)
    
    if not response.ok:
        return None

    return response.json()['id']


def get_total_clicks(bitlink, auth_token):

    headers = {
        'Authorization': f'Bearer {auth_token}'
    }

    payload = {
        'unit': 'day',
        'units': '-1'
    }

    response = requests.get(
        f'{SERVER_URL}/v4/bitlinks/{bitlink}/clicks/summary',
        headers=headers,
        params=payload)

    if not response.ok:
        return None

    return response.json()['total_clicks']


def is_bitly_link(link, known_links):
    for prefix in known_links:
        if link.startswith(prefix):
            return True
    return False

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Shortens the link or shows statistics on the shortened link'
    )
    parser.add_argument('link', help='Link')
    args = parser.parse_args()
    link = args.link

    if is_bitly_link(link, BITLY_LINKS):
        total_clicks = get_total_clicks(link, AUTH_TOKEN)
        print(total_clicks if total_clicks is not None else 'Invalid bitlink')
    else:
        shorten_link = short_url(link, AUTH_TOKEN)
        print(shorten_link if shorten_link is not None else 'Invalid url')


