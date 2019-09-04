from flask import Flask
from azure.keyvault import KeyVaultClient
from azure.storage.blob import BlockBlobService
from msrestazure.azure_active_directory import MSIAuthentication
app = Flask(__name__)

@app.route("/")
def hello():
    credentials = MSIAuthentication(resource='https://vault.azure.net')
    kvclient = KeyVaultClient(credentials)
    key = kvclient.get_secret("https://mnanalyticssandbox-vault.vault.azure.net/", "DiskEncrption", "").value
    return "Hello!"
