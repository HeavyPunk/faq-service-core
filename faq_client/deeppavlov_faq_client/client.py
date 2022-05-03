from ..base_client import BaseFaqClient
from settings.settings import SettingsProvider
from utils import requester


class DeepPavlovRestApiClient(BaseFaqClient):
    _base_url = None
    def init(self) -> None:
        protocol = SettingsProvider.get('DP_FAQ_HTTP')
        host = SettingsProvider.get('DP_FAQ_HOST')
        port = SettingsProvider.get('DP_FAQ_PORT')
        path = SettingsProvider.get('DP_FAQ_API')['send_model']

        url = f"{protocol}://{host}:{port}/{path}"
        self._base_url = url
        if not requester.ping(url):
            raise Exception(f"DeepPavlov is not available on url: {url}")

    def send_question(self, question: str) -> (str, float):
        data = {
            "q": [
                question
            ]
        }
        response = requester.send(method="POST", url=self._base_url, body=data)
        print(f"Request to {self._base_url} was send with code {response.status_code}")
        res = response.json()
        return res[0][0]

    def relearn(self):
        pass
