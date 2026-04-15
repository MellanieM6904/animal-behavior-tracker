import mariadb
import sys, os
import models

try:
    conn = mariadb.connect(
        user = "mellaniem",
        password = "7minutes",
        host="localhost",
        port=3306
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

curr = conn.cursor()
sql = """DROP DATABASE IF EXISTS mpDB"""
curr.execute(sql)
sql = """CREATE DATABASE mpDB"""
curr.execute(sql)
conn.commit()

models.db.create_tables([models.Activities, models.Weights])
