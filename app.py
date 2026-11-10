from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from Azure Container Apps! <br>Storage: {os.getenv('STORAGE_ACCOUNT')} <br>Blob Container: uploads"

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
