import sqlite3
import string

connection = sqlite3.connect('user_stock_database.db')
cursor = connection.cursor()


def create_sqlite_database():
    sql = open('resource/create_database.sql', 'r', encoding='utf8')
    sql_text = "".join(sql.readlines())
    sql.close()
    cursor.execute(sql_text)
    close_sqlite()


def add_user_stock(user_id: string, stock_id: string):

    return ''


def delete_user_stock(user_id: string, stock_id: string):
    return ''


def close_sqlite():
    connection.close()
