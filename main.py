import argparse
import openai
import json
import os

from schema import get_schema
from query import select_from_table
from db import create_connection

DATABASE = "file:restaurant.db"


def main(conn, question):

    openai.api_key = os.environ['OPENAI_API_KEY']

    print(f"Question: {question}")

    prompt = f"""
    
    Given the following SQL Schema:{get_schema(conn)}
    For the isVegan and isGlutenFree columns, use only "true" or "false."
    Write a sqlite query to answer the following question: {question}
    
    """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=200
    )

    q = response["choices"][0]["text"]

    print(f"AI-generated SQL query: \n{q}\n")
    print("Answer: \n")
    select_from_table(conn, q)


if __name__ == "__main__":
    while True:
        parser = argparse.ArgumentParser()
        query = input("What would you like to know about the data? Type 'q' to quit\n")
        if query == "q":
            break
        parser.add_argument("--query", type=str, default=query)
        args = parser.parse_args()
        conn = create_connection(DATABASE)

        main(conn, question=args.query)

