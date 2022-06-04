from fastapi import FastAPI, UploadFile

from daemon.DeeppavlovUpdaterDaemon import DeeppavlovUpdaterDaemon
from faq_client.deeppavlov_faq_client.client import DeepPavlovRestApiClient
from faq_client.deeppavlov_faq_client.self_hosted_client import DeepPavlovSelfHostedClient
from faq_client.static_provider import FaqClientProvider
from settings.settings import SettingsProvider

app = FastAPI()
SettingsProvider()
faq_client = DeepPavlovSelfHostedClient()
FaqClientProvider.configure(faq_client)
faq_client.init()

updater_daemon = DeeppavlovUpdaterDaemon(faq_client)
updater_daemon.start()

# DEBUG
# faq_client.init()
# faq_client.send_question("Нужен ли мне паспорт?")
######


@app.get('/faq')
def faq(question: str):
    client = FaqClientProvider.get()
    res = client.send_question(question)
    return {"answer": res}

@app.get('/faq-voice')
def faq(voice: UploadFile):
    pass


@app.get('/faq/relearn')
def faq_relearn(apikey: str):
    if apikey != SettingsProvider.get("APIKEY"):
        return {"code": 401, "message": "Bad apikey"}
    client = FaqClientProvider.get()
    relearn_result = client.relearn()
    return {"result": relearn_result}
