sql_create_branch_table = """
    CREATE TABLE "Branch" (
        "branch_id"	INTEGER,
        "location_city"	TEXT,
        "manager_id"	INTEGER,
        PRIMARY KEY("branch_id"),
        FOREIGN KEY("manager_id") REFERENCES "Employee"("employee_id")
    );
"""

sql_create_employee_table = """
    CREATE TABLE "Employee" (
        "employee_id"	INTEGER NOT NULL,
        "shift"	TEXT,
        "first_name"	TEXT,
        "last_name"	INTEGER,
        "branch_id"	INTEGER,
        PRIMARY KEY("employee_id"),
        FOREIGN KEY("branch_id") REFERENCES "Branch"("branch_id")
    );
"""

sql_create_customer_table = """
     CREATE TABLE "Customer" (
        "customer_id"	INTEGER UNIQUE,
        "first_name"	TEXT,
        "last_name"	TEXT,
        PRIMARY KEY("customer_id")
    );
"""

sql_create_meals_table = """
    CREATE TABLE "Meals" (
        "meal_id"	INTEGER UNIQUE,
        "name"	TEXT,
        "price"	REAL,
        "calories"	INTEGER,
        "isVegan"	TEXT,
        "isGlutenFree"	TEXT,
        PRIMARY KEY("meal_id"),
        CHECK (isVegan IN ("true", "false")),
        CHECK (isGlutenFree IN ("true," "false"))
    );
"""

sql_create_order_table = '''
    CREATE TABLE "Order" (
        "order_id"	INTEGER,
        "customer_id"	INTEGER,
        "total_price"	REAL,
        "meal_id"	INTEGER,
        "quantity"	INTEGER,
        "employee_id"	INTEGER,
        PRIMARY KEY("order_id","meal_id"),
        FOREIGN KEY("customer_id") REFERENCES "Customer"("customer_id"),
        FOREIGN KEY("employee_id") REFERENCES "Employee"("employee_id"),
        FOREIGN KEY("meal_id") REFERENCES "Meals"("meal_id")
    );
'''


def get_schema():
    schema = f"{sql_create_branch_table}{sql_create_employee_table}{sql_create_customer_table}{sql_create_meals_table}{sql_create_order_table}"
    return schema
