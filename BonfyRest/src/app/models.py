#-*- coding:utf-8  -*-
'''
Created on 2014-9-10

@author: ChenKai
'''
from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)

    def __repr__(self):
        return '<User %r>' % (self.nickname)
    
class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(120))
    done = db.Column(db.Boolean,default= False)
    
    def __repr__(self):
        return '<Task %r>' % (self.title)
    
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'done':self.done
        }