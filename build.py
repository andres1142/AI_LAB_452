import os

from db import create_table, create_connection
from schema import *


def insert_to_branch(conn):
    sql = """
        INSERT INTO "Branch" ("branch_id", "location", "manager_id")
        VALUES
            (1, 'Dallas', 101),
            (2, 'Los Angeles', 102),
            (3, 'Chicago', 103),
            (4, 'San Francisco', 104),
            (5, 'Los Angeles', 105),
            (6, 'Chicago', 106),
            (7, 'Dallas', 107),
            (8, 'San Francisco', 108),
            (9, 'San Francisco', 109),
            (10, 'San Francisco', 110);
    """
    cur = conn.cursor()
    cur.executescript(sql)  # Use executescript to execute multiple SQL statements
    conn.commit()
    return cur.lastrowid


def insert_to_employee(conn):
    sql = '''
        INSERT INTO "Employee" ("shift", "first_name", "last_name", "branch_id")
        VALUES
            ('Morning', 'John', 'Smith', 101),
            ('Morning', 'Jane', 'Doe', 102),
            ('Evening', 'Michael', 'Johnson', 103),
            ('Evening', 'Emily', 'Brown', 104),
            ('Night', 'William', 'Jones', 105),
            ('Night', 'Olivia', 'Wilson', 106),
            ('Morning', 'James', 'Taylor', 107),
            ('Morning', 'Emma', 'Miller', 108),
            ('Evening', 'Daniel', 'Anderson', 109),
            ('Evening', 'Sophia', 'White', 110),
            ('Morning', 'David', 'Martinez', 111),
            ('Morning', 'Oliver', 'Anderson', 112),
            ('Evening', 'Benjamin', 'Thompson', 113),
            ('Evening', 'Charlotte', 'Hernandez', 114),
            ('Night', 'Elijah', 'Lopez', 115),
            ('Night', 'Amelia', 'Garcia', 116),
            ('Morning', 'Mason', 'Lee', 117),
            ('Morning', 'Sophia', 'Davis', 118),
            ('Evening', 'Henry', 'Rodriguez', 119),
            ('Evening', 'Ava', 'Martinez', 120),
            ('Morning', 'Jackson', 'Williams', 121),
            ('Morning', 'Aiden', 'Gonzalez', 122),
            ('Evening', 'Sebastian', 'Smith', 123),
            ('Evening', 'Liam', 'Harris', 124),
            ('Night', 'Mia', 'Anderson', 125);
    '''

    cur = conn.cursor()
    cur.executescript(sql)  # Use executescript to execute multiple SQL statements
    conn.commit()
    return cur.lastrowid


def insert_into_customer(conn):
    sql = '''
        INSERT INTO "Customer" ("first_name", "last_name")
        VALUES
            ('John', 'Doe'),
            ('Jane', 'Smith'),
            ('Michael', 'Johnson'),
            ('Emily', 'Brown'),
            ('William', 'Jones'),
            ('Olivia', 'Wilson'),
            ('James', 'Taylor'),
            ('Emma', 'Miller'),
            ('Daniel', 'Anderson'),
            ('Sophia', 'White');
    '''

    cur = conn.cursor()
    cur.executescript(sql)  # Use executescript to execute multiple SQL statements
    conn.commit()
    return cur.lastrowid


def main():
    database = "./restaurant.db"

    # create a database connection
    conn = create_connection(database)

    # TODO: Uncomment when adding
    # insert_to_branch`(conn)
    # insert_to_employee(conn)
    # insert_into_customer(conn)

    print("Database build successful!")


if __name__ == "__main__":
    main()
