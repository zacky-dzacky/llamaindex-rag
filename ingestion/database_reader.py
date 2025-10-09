from llama_index.core import download_loader
from llama_index.readers.database import DatabaseReader
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".venv/.env")

reader = DatabaseReader(
    scheme=os.getenv("DB_SCHEME"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    dbname=os.getenv("DB_NAME"),
)

query = "SELECT * FROM users"
documents = reader.load_data(query=query)

print (documents)