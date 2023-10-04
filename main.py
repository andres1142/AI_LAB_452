import argparse
import openai
import json
import os

from schema import get_schema
from query import select_from_table
from db import create_connection

DATABASE = "./restaurant.db"


def main(conn, question):

    openai.api_key = os.getenv('OPENAI_API_KEY')

    print(f"Question: {question}")

    prompt = f"""
    
    Given the following SQL Schema:{get_schema()}
    Write a SQL query to answer this question: {question}
    
    """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=200
    )

    q = response["choices"][0]["text"]

    print(f"AI-generated SQL query: \n{q}")
    print("Answer: \n")
    select_from_table(conn, q)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    query = input("What would you like to know about the data?\n")
    parser.add_argument("--query", type=str, default=query)
    args = parser.parse_args()
    conn = create_connection(DATABASE)

    main(conn, question=args.query)
