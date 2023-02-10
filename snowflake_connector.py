import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv

dotenv_path = join(os.path.dirname(os.path.abspath(__file__)),'.env')
load_dotenv(find_dotenv())

 # Get the credentials from .env
account    = os.getenv('account')
user       = os.getenv('user')
warehouse  = os.getenv('warehouse')
database   = os.getenv('databsae')
schema     = os.getenv('schema')
password   = os.getenv('password')
region     = os.getenv('region')

