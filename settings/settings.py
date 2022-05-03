import os

SETTINGS = {
    "DP_FAQ_CONFIG_PATH": f"{os.getcwd()}/faq_school_en.json",
    "DP_FAQ_HOST": "localhost",
    "DP_FAQ_HTTP": "http",
    "DP_FAQ_PORT": 5005,
    "DP_FAQ_API":
        {
            "send_model": "model"
        },
    "SELF_HOST": "127.0.0.1",
    "SELF_PORT": 5123,
    "DATABASE_NAME": "postgres",
    "DATABASE_USER": "postgres",
    "DATABASE_HOST": "localhost",
    "DATABASE_PORT": 5432,
    "DATABASE_PASSWD": "pgpwd4habr",
    "DATABASE_TABLE": "FaqPairs",
}


class SettingsProvider:
    def __init__(self):
        pass

    @staticmethod
    def get(setting_name: str, default=None):
        if setting_name not in SETTINGS:
            return default
        else:
            return SETTINGS[setting_name]
