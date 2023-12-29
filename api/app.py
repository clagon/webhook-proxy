import os

import requests
from flask import Flask, request
from flask_cors import CORS

WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://resistance-predict.vercel.app:*", "http://localhost:*"]}})

@app.route("/proxy/discord/webhook", methods=["POST"])

def webhook():

    file_uploaded = request.files["attachment"]
    filename = file_uploaded.filename
    content = request.form.get("payload_json")

    r = None
    body = {
        "payload_json": content
    }
    files = {
        "attachment": (filename, file_uploaded.read())
    }
    r = requests.post(
        WEBHOOK_URL,
        body,
        files=files
    )
    print(r.status_code)
    return "ok"
