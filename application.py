import pandas as pd
import numpy as np
import tables
import time
from azure.storage.blob import BlockBlobService
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Python!"
