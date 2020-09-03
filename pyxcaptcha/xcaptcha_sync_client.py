from .xcaptcha_sync_api import XCaptchaSyncApi
from .exceptions import CaptchaNotReadyException
from time import sleep


class XCaptchaSyncClient:
    def __init__(self, token: str):
        self.api = XCaptchaSyncApi(token)

    def send_captcha(self, site_key: str, page_url: str, test_interval: int = 1):
        task_id = self.api.send_captcha(site_key, page_url)

        resp = None

        while resp is None:
            try:
                server_answer = self.api.get_captcha_result(task_id)
                resp = server_answer
            except CaptchaNotReadyException:
                sleep(test_interval)

        return resp
