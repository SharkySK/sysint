import sqlite3
from sqlite3 import Error


def create_conn(db_file):
    conn = None
    try:
        """ Create SQLL in memory 
            conn = sqlite3.connect(':memory:')
            print(sqlite3.version)
        """
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def execute_sql(conn, sql_statement):
    try:
        c = conn.cursor()
        c.execute(sql_statement)
    except Error as e:
        print(e)


def create_table():
    sql_create_projects_table = "CREATE TABLE IF NOT EXISTS projects (id integer PRIMARY KEY, " \
                                "name text NOT NULL, " \
                                "begin_date text, " \
                                "end_date text ); "
    return sql_create_projects_table


def populate_table(conn, sql_data):
    sql_populate_projects = "INSERT INTO projects(name,begin_date,end_date)" \
                            "VALUES(?,?,?)"

    cur = conn.cursor()
    cur.execute(sql_populate_projects,sql_data)
    return cur.lastrowid


def update_project(conn, project):
    sql = "UPDATE projects " \
          "SET name = ?," \
          "begin_date = ?, " \
            "end_date = ? " \
          "WHERE id = ?"

    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()


def select_all(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM projects")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def delete_all(conn):
    sql = "DELETE FROM projects"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


if __name__ == "__main__":
    conn = create_conn("sqllite.db")

    if conn is not None:
        execute_sql(conn, create_table())
    else:
        print("Error")

    with conn:
        delete_all(conn)

        row_data = ("MySQL project", "2.1.2020", "22.1.2020")
        populate_table(conn, row_data)

        row_data = ("SQL Lite project", "12.1.2020", "22.1.2020")
        populate_table(conn, row_data)

        update_project(conn, ("New Project SQL", "24.12.2019", "2.1.2020", 1))

        select_all(conn)
