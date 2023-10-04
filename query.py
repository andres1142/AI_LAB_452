import argparse
from db import create_connection


def select_all_from_menu(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM menu")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_from_table(conn, query):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall()

    if (len(rows) == 0):
        print("No results found.")

    for row in rows:
        print(row)


if __name__ == "__main__":
    database = "./restaurant.db"
    conn = create_connection(database)

    print(f"Executing query: SELECT * FROM Employee WHERE shift = 'Morning'")
    select_from_table(conn, "SELECT * FROM Employee WHERE shift = 'Morning'")
