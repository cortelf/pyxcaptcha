from .xcaptcha_api import XCaptchaApi
from aiohttp import ClientSession
from typing import Dict, Union
from .exceptions import ServerBadCodeResponseException


class XCaptchaAsyncApi(XCaptchaApi):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.session: ClientSession = ClientSession()

    async def _request_extractor(self, request):
        async with request as resp:
            if not (299 >= resp.status >= 200):
                raise ServerBadCodeResponseException(resp.status)

            text: str = await resp.text()
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
