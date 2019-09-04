import json
import logging
import azure.functions as func
from azure.keyvault import KeyVaultClient
from azure.storage.blob import BlockBlobService
from msrestazure.azure_active_directory import MSIAuthentication
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Python!"
