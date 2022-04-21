from .base_client import BaseFaqClient


class FaqClientProvider:
    _client = None

    @staticmethod
    def configure(client: BaseFaqClient):
        FaqClientProvider._client = client

    @staticmethod
    def get() -> BaseFaqClient:
        if not FaqClientProvider.is_configured():
            raise Exception(f"[{FaqClientProvider.__name__}] Faq client is not configured")
        return FaqClientProvider._client

    @staticmethod
    def is_configured():
        return FaqClientProvider._client is not None
