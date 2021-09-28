import sqlite3


def main():
    con = sqlite3.connect("../netflix.db")
    cur = con.cursor()
    sqlite_query = ("SELECT title FROM netflix "
                    "WHERE description LIKE '%train%'"
                    "AND type='Movie'")
    cur.execute(sqlite_query)
    for row in cur.fetchall():
        print(row[0])
    con.close()


if __name__ == '__main__':
    main()