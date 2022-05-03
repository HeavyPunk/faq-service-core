import subprocess
from settings.settings import SettingsProvider

#subprocess.run(['uvicorn', 'api.api:app', '--reload', f"--host {SettingsProvider.get('SELF_HOST', default='127.0.0.1')}", f"--port {SettingsProvider.get('SELF_PORT', default='5123')}"])
#subprocess.run(f"uvicorn api.api:app --reload --host {SettingsProvider.get('SELF_HOST', default='127.0.0.1')} --port {SettingsProvider.get('SELF_PORT', default='5123')}")
subprocess.run(["uvicorn","api.api:app","--reload"])