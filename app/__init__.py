"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgum850dh87vhrlgusig-a.oregon-postgres.render.com",
        database="nandan_todo_db",
        user="root",
        password="NGHGxGJoemNCRuGFqsGfDtMFogJRMG6g")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
