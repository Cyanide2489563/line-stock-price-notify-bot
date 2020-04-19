from database.sqlite import sqlite_api


def create_database():
    sqlite_api.create_sqlite_database()
