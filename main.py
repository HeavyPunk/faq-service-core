from flask import Flask
from flask_restful import Api
from faq_client.deeppavlov_faq_client.client import DeepPavlovClient

app = Flask(__name__)
api = Api(app)

faq_client = DeepPavlovClient()

#DEBUG
faq_client.init()
faq_client.send_question("Нужен ли мне паспорт?")
######

if __name__ == "__main__":
    app.run(host="localhost", port=5123)


@app.before_first_request
def init():
    faq_client.init()



