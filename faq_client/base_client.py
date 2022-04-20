
class BaseFaqClient:
    def init(self) -> None:
        pass

    def send_question(self, question: str) -> (str, float):
        pass

    def relearn(self):
        pass
