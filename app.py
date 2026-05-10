from flask import Flask, render_template
import socket
import os

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()

    app_name = os.getenv("APP_NAME", "Default App")
    message = os.getenv("WELCOME_MSG", "Hello World")

    return render_template(
        'index.html',
        pod_name=hostname,
        app_name=app_name,
        message=message
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)