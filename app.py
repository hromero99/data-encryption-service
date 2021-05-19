from flask import Flask
from flask import jsonify
from flask import request
from flask import send_from_directory
from utils.encryptManager import EncryptorManager
from utils import KeysRepository
from utils import UploadManager
import os

app = Flask(__name__)


@app.errorhandler(404)
def resource_not_found(error):
    return jsonify(f"Resource not found {error}"), 404


@app.route("/encrypt/", methods=["POST"])
def encrypt_message():
    # Make request to another microservice to get the rsa key
    request_data = request.get_json()
    key = KeysRepository().get_public_key(device_id=request_data.get("device_id"))
    if key:
        encrypted = EncryptorManager(public_key=key).encrypt(msg=request_data.get("message"))
        UploadManager().upload_file(f"/tmp/{encrypted}")
        return send_from_directory("/tmp/", encrypted, as_attachment=True)
    return {"error": "Error query for public key"}


@app.route("/decrypt/", methods=["POST"])
def decrypt_message():
    # Make request to another microservice to get the rsa key
    request_data = request.get_json()
    key = KeysRepository().get_private_key(device_id=request_data.get("device_id"))
    if key:
        encrypted = EncryptorManager(private_key=key).decrypt(encrypted=request_data.get("encrypted_data"))
        return {"data": encrypted}
    return {"error": "Error query for public key"}


if __name__ == "__main__":
    if os.getenv("KEY_STORAGE") == "":
        raise EnvironmentError("KEY_STORAGE var not define")
