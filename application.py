from flask import Flask
from azure.keyvault import KeyVaultClient
from azure.storage.blob import BlockBlobService
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Python!"
