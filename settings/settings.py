SETTINGS = {
    "DP_FAQ_CONFIG_PATH": "path/to/config",
    "DP_FAQ_HOST": "localhost",
    "DP_FAQ_HTTP": "http",
    "DP_FAQ_PORT": 5005,
    "DP_FAQ_API":
        {
            "send_model": "model"
        }
}


class SettingsProvider:
    def __init__(self):
        pass

    def get(self, setting_name: str, default = None):
        if setting_name not in SETTINGS:
            return default
        else:
            return SETTINGS[setting_name]
