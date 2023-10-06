def get_schema(conn):
    cur = conn.cursor()
    cur.execute("SELECT sql from SQLITE_SCHEMA WHERE sql IS NOT NULL")
    rows = cur.fetchall()
    schema = ""
    for row in rows:
      schema += row[0]
      schema += "\n"
    return schema
