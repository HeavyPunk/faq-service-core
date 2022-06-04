import os
import json

PATH_RESOLVER_MIDDLEWARE = {
    "WorkingDir": os.getcwd(),
}


class SettingsProvider:
    SETTINGS = {
        "SERVICE_APIKEY": "62c50ba3-f149-40c6-b5a5-7506db4cd8bf",
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
        "DP_UPD_DAEMON_UPDATE_THR_MINUTE": 30
    }

    def __init__(self):
        file = open(f"{os.getcwd()}/production.settings.json")
        settings = file.read()
        for pattern in PATH_RESOLVER_MIDDLEWARE:
            settings = settings.replace('{' + pattern + '}', PATH_RESOLVER_MIDDLEWARE[pattern])
        SettingsProvider.SETTINGS = json.loads(settings)

    @staticmethod
    def get(setting_name: str, default=None):
        if setting_name not in SettingsProvider.SETTINGS:
            return default
        else:
            return SettingsProvider.SETTINGS[setting_name]
