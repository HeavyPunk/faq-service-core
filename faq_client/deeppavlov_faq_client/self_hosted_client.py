import os

from database.database_client import DatabaseClient
from ..base_client import BaseFaqClient
from settings.settings import SettingsProvider
from deeppavlov import build_model
import json


class DeepPavlovSelfHostedClient(BaseFaqClient):
    _model = None
    _db = DatabaseClient()

    def init(self) -> None:
        config = json.load(open(SettingsProvider.get('DP_FAQ_CONFIG_PATH')))
        self._model = build_model(config=config, download=True)

    def send_question(self, question: str) -> (str, float):
        result = self._model([question])
        return result[0][0]

    def relearn(self):
        self._db.get_csv(f"{os.getcwd()}/FaqPairs.csv")
        config = json.load(open(SettingsProvider.get("DP_FAQ_CONFIG_PATH")))
        new_model = None
        try:
            new_model = build_model(config=config, download=True)
            self._model = new_model
            return "OK"
        except BaseException as e:
            return f"[DeepPavlovSelfHostedClient] ERROR {e}"
