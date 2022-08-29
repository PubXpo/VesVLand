# standard imports
import pandas as pd
import chardet
import re
import os
import glob
import matplotlib.pyplot as plt
import seaborn as sns
import folium

from pymongo import MongoClient

# connect to the MongoDB Server
MONGO_CONNECTION_STRING = f"mongodb://localhost:27017/"
print(f"MONGO_CONNECTION_STRING = {MONGO_CONNECTION_STRING}")

DB_NAME ="ves_land_db"
print(f"DB_NAME = {DB_NAME}")

# connect to the database
mongo_client = MongoClient(MONGO_CONNECTION_STRING)
vess_land_db = mongo_client[DB_NAME]