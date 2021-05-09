from flask import Flask, url_for
from flask import jsonify
from flask import request
import requests
from encrypt import EncryptorManager


app = Flask(__name__)


@app.errorhandler(404)
def resource_not_found(error):
    return jsonify(f"Resource not found {error}"), 404


@app.route("/encrypt", methods=["POST"])
def encrypt_message():
    # Make request to another microservice to get the rsa key
    util = EncryptorManager()
    msg = util.encrypt_rsa_msg("pipo")
    print(request.remote_addr)
    return jsonify(str(msg)),400

@app.route("/generate", methods=["GET"])
def generate_key():
    key = EncryptorManager().generate_rsa_key()

    return jsonify(key.decode("utf-8"))

if __name__ == "__main__":
    app.run()