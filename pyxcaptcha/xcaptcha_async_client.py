from .xcaptcha_async_api import XCaptchaAsyncApi
from .exceptions import CaptchaNotReadyException
from asyncio import sleep


class XCaptchaAsyncClient:
    def __init__(self, token: str):
        self.api = XCaptchaAsyncApi(token)

    async def send_captcha(self, site_key: str, page_url: str, test_interval: int = 1):
        task_id = await self.api.send_captcha(site_key, page_url)

        resp = None

        while resp is None:
            try:
                server_answer = await self.api.get_captcha_result(task_id)
                resp = server_answer
            except CaptchaNotReadyException:
                await sleep(test_interval)

        return resp
