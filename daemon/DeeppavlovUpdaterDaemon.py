import threading
import time
from settings.settings import SettingsProvider
from faq_client.deeppavlov_faq_client.self_hosted_client import DeepPavlovSelfHostedClient


class DeeppavlovUpdaterDaemon(threading.Thread):
    process = None

    def __init__(self, faq_client: DeepPavlovSelfHostedClient):
        super().__init__()
        self.faq_client = faq_client
        self.daemon = True

    def run(self):
        _lastUpdate = 0
        while True:
            current_time = time.time()
            if current_time - _lastUpdate > SettingsProvider.get("DP_UPD_DAEMON_UPDATE_THR_MINUTE", 10) * 60:
                _lastUpdate = current_time
                self.faq_client.relearn()
                print(f"[DeeppavlovUpdaterDaemon] INFO Updated")
            time.sleep(1)

