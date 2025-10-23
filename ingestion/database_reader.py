from llama_index.core import download_loader
from llama_index.readers.database import DatabaseReader
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".venv/.env")

reader = DatabaseReader(
    scheme="transaction",
    host="172.17.0.2",
    port=3306,
    user="root",
    password="root",
    dbname="testdb",
)

query = "SELECT * FROM IB_USER"
documents = reader.load_data(query=query)

print (documents)