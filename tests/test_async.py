import os
import asyncio

from pyxcaptcha import XCaptchaAsyncClient

TEST_TOKEN = os.getenv("test_token")


async def async_fun():
    client = XCaptchaAsyncClient(TEST_TOKEN)

    balance = await client.api.get_balance()
    print(balance)

    resp = await client.send_captcha("6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-", "https://www.google.com"
                                                                                 "/recaptcha/api2/demo")
    print(resp)


def func():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_fun())


func()
