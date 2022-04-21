from flask import Flask
from flask import request
from flask_restful import Api

from faq_client.deeppavlov_faq_client.client import DeepPavlovClient
from faq_client.static_provider import FaqClientProvider

app = Flask(__name__)
api = Api(app)

faq_client = DeepPavlovClient()
FaqClientProvider.configure(faq_client)


# DEBUG
# faq_client.init()
# faq_client.send_question("Нужен ли мне паспорт?")
######

@app.before_first_request
def init():
    faq_client.init()


@app.route("/faq", methods=['GET'])
def faq():
    question = request.args.get('question')
    client = FaqClientProvider.get()
    res = client.send_question(question)
    return {"answer": res}, 200


if __name__ == "__main__":
    app.run(host="localhost", port=5123)
