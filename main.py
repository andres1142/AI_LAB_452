import argparse
import openai
import json

from schema import get_schema
from db import create_connection

DATABASE = "./restaurant.db"


if __name__ == "__main__":
    conn = create_connection(DATABASE)
    
