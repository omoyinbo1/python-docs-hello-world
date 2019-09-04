from flask import Flask
from azure.keyvault import KeyVaultClient
from azure.storage.blob import BlockBlobService
from msrestazure.azure_active_directory import MSIAuthentication
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Python!"
