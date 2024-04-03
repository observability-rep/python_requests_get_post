
import requests


def check_website(url):
    try:
        response = requests.get(url)
        # Check if the response status code is 200 (OK)
        if response.status_code == 200 or 201:
            print(f"The website {url} is accessible.\n")
        else:
            print(f"The website {url} is not accessible. Status code: {response.status_code}\n")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to access the website {url}: {e}")


def check_post_request(url, headers, data):
    try:
        response = requests.post(url, headers=headers, json=data)
        # Check if the request was successful
        is_request_ok = 200 <= response.status_code < 300  #all http responses between 200-300 mean successful 
        print("REQUEST SENT, Response:", is_request_ok)
        #print("")
        print("How to interpret response:\n   REQUEST SENT means authentication process started successfully \n   Response: True-> login successful \n   Response: False-> login unsuccessful")
        return is_request_ok

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to send POST request to {url}: {e}")
        return 0

#parameters to be sent to get function
url_get_response= "https://www.example.com/en"
check_website(url_get_response)

#parameters to be sent to post function
url_post_request= 'https://www.example.com/api/v1/single-sign-on-sessions/'
headers_post_request = {
            'authority': 'www.example.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,pl;q=0.8,en-GB;q=0.7,en-MT;q=0.6,pl-PL;q=0.5',
            'brandid': '537ff570-9c20-4b61-9427-3b09aac71995',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'dnt': '1',
            'marketcode': 'en',
            'origin': 'https://www.example.com',
            'pragma': 'no-cache',
            'referer': 'https://www.example.com/en',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'x-obg-channel': 'Web',
            'x-obg-country-code': 'MT',
            'x-obg-device': 'Desktop',
            'x-obg-experiments': 'ssrClientConfiguration'
        }
data_post_request = {
            "type": "up",
            "loginSource": "Web",
            "iovationBlackBox":  "0240322082257MWU2ZDBhOWU4ZTc3NGUwODk4NmFlMWYyOGRmZGRkYmE",
            "username": "yourtestingaccount@yourtestingaccount.com",
            "password": "yourpassword",
            "shouldRememberUser": True
        }

check_post_request(url_post_request, headers_post_request, data_post_request)


