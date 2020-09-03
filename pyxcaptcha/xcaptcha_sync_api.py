from .xcaptcha_api import XCaptchaApi
from requests import Session, Response
from typing import Dict, Union
from .exceptions import ServerBadCodeResponseException


class XCaptchaSyncApi(XCaptchaApi):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.session: Session = Session()

    def _request_extractor(self, response: Response):
        if not (299 >= response.status_code >= 200):
            raise ServerBadCodeResponseException(response.status_code)

        text: str = response.text
        self.handle_text_exceptions(text)

        assert "OK|" in text
        return text.split("|")[1].strip()

    def send_request(self,
                     method: str,
                     url: str,
                     query_params: Dict[str, Union[int, str]] = None,
                     data: any = None):
        return self._request_extractor(
            self.session.request(method, url, params={'key': self.api_key, **query_params}, data=data))
