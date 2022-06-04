import requests
from fastapi import FastAPI, UploadFile, File

from daemon.DeeppavlovUpdaterDaemon import DeeppavlovUpdaterDaemon
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


@app.get('/faq')
def faq(question: str):
    client = FaqClientProvider.get()
    res = client.send_question(question)
    return {"answer": res}


@app.get('/faq-voice')
def faq(voice: UploadFile = File(...)):
    url = f"https://{SettingsProvider.get('RECOGNIZER_IP')}/messages"
    res = requests.post(url, files={'file': voice.file})
    if not res.ok:
        res.raise_for_status()
    res = res.json()
    if 'text' not in res:
        raise Exception(f"Recognizer returned unexpected answer: {res}")
    client = FaqClientProvider.get()
    answer = client.send_question(res['text'])
    return {"answer": answer}


@app.get('/faq/relearn')
def faq_relearn(apikey: str):
    if apikey != SettingsProvider.get("APIKEY"):
        return {"code": 401, "message": "Bad apikey"}
    client = FaqClientProvider.get()
    relearn_result = client.relearn()
    return {"result": relearn_result}
