import os
import asyncio

from pyxcaptcha import XCaptchaSyncClient

TEST_TOKEN = os.getenv("test_token")


def sync_fun():
    client = XCaptchaSyncClient(TEST_TOKEN)

    balance = client.api.get_balance()
    print(balance)

    resp = client.send_captcha("6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-", "https://www.google.com"
                                                                                 "/recaptcha/api2/demo")
    print(resp)


def func():
    sync_fun()


func()
