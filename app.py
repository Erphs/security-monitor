from flask import Flask, request
from user_agents import parse
import json
from datetime import datetime
import os



app = Flask(__name__)

LOG_FILE = "log.json"

def save_log(ip, user_agent_string):
    user_agent = parse(user_agent_string)
    log_entry = {
        "ip": ip,
        "user_agent": user_agent_string,
        "browser": f"{user_agent.browser.family} {user_agent.browser.version_string}",
        "os": f"{user_agent.os.family} {user_agent.os.version_string}",
        "device": f"{user_agent.device.family}",
        "time": datetime.now().isoformat()
    }


    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f, indent=4)


    with open(LOG_FILE, "r+", encoding='utf-8') as f:
        logs = json.load(f)
        logs.append(log_entry)
        f.seek(0)
        json.dump(logs, f, indent=4)


@app.route('/')
def index():
    ip = request.remote_addr
    user_agent_str = request.headers.get('User-Agent')


    save_log(ip, user_agent_str)

    return f"""<h1> 🧠 Your Info Logged!</h1>
    <p>IP : {ip}</p>
    <p> User-Agent: {user_agent_str}</p>"""

if __name__ == "__main__":
    app.run(debug=True)