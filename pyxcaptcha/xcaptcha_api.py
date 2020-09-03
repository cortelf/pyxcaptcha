from abc import ABC, abstractmethod
from typing import Dict, Union
from .exceptions import *


class XCaptchaApi(ABC):
    exception_map = {
        'ERROR_KEY_USER': InvalidAPIKeyException,
        'ERROR_ZERO_BALANCE': ZeroBalanceException,
        'ERROR_KEY_OR_URL': InvalidCaptchaParamsException,
        'ERROR_NOT_SLOT_ZERO': NoWorkersException,
        'ERROR_NOT_SLOT_BUSY': NotEnoughWorkersException,
        'ERROR_PAUSE_SERVICE': ServerPreventionException,
        'CAPCHA_NOT_READY': CaptchaNotReadyException,
        'ERROR_BAD_REZ_MANYBEK': WorkerMistakeException,
        'ERROR_BAD_TIME_MANYBEK': WorkerTimeoutException,
        'ERROR_NOT_CAPCHA_ID': WrongCaptchaIDException,
    }

    def __init__(self, api_key: str):
        self.api_key = api_key

    @abstractmethod
    def send_request(self,
                     method: str,
                     url: str,
                     query_params: Dict[str, Union[int, str]]):
        pass

    def handle_text_exceptions(self, text: str):
        if text in self.exception_map:
            raise self.exception_map[text]()

    def get_balance(self):
        return self.send_request("GET", "http://x-captcha2.ru/res.php", {"action": "getbalance"})

    def send_captcha(self, google_key: str, page_source: str):
        return self.send_request("GET", "http://x-captcha2.ru/in.php",
                                 {"method": "userrecaptcha", "googlekey": google_key, "pageurl": page_source})

    def get_captcha_result(self, captcha_id: Union[int, str]):
        return self.send_request("GET", "http://x-captcha2.ru/res.php", {"id": captcha_id})

