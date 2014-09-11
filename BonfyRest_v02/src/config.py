'''
Created on 2013-11-20
@author: ChenKai
'''
import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sa:1qaz@WSX@127.0.0.1:1433/mine'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')