import mysql.connector as sql
import click
from flask import current_app, g
from flask.cli import with_appcontext
from .schema import inst

def get_db():
    if 'db' not in g:
        g.db = sql.connect(
            host = "localhost",#current_app.config['DATABASE_HOST'],
            user = "Nano",#current_app.config['DATABASE_USER'],
            password = "123456",#current_app.config['DATABASE_PASSWORD'],
            database = "prueba"#current_app.config['DATABASE'],
        )

        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None: db.close()

def init_db():
    db, c = get_db()
    for i in inst:
        c.execute(i)
    db.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Base de datos inicializada.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)