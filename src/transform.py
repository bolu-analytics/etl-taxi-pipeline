import sqlite3

def run_sql_file(db_path, sql_file):
    conn = sqlite3.connect(db_path)
    with open(sql_file, "r") as f:
        conn.executescript(f.read())
    conn.close()
