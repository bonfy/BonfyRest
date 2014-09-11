#-*- coding:utf-8  -*-
from app import app
from datetime import datetime
from models import Task
from app import db
from flask import jsonify,request,abort,make_response
import json

######################
#
# HTTP Status Handler
#
######################

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error':'Not Found 404' } ),404)
    
@app.errorhandler(400)
def error_400(error):
    return make_response(jsonify( { 'error':'Error 400' } ),400)

######################
#
# Route And RestFul
#
######################

@app.route('/')
@app.route('/index')
def index():
    
    return "hello world"
    
@app.route('/todo/api/v1.0/tasks', methods = ['GET'])
def get_tasks():
    #tasks = Task.query.get(1)
    #print tasks
    #return json.dumps(data1)#,sort_keys=True,indent=4)
    #return jsonify(tasks.to_json())
    #只能解决单个的to_json()
    
    tasks = Task.query.all()
    print tasks
    #json_list=[i.serialize for i in qryresult.all()]
    return jsonify(json_list = [i.to_json() for i in tasks])

@app.route('/todo/api/v1.0/tasks', methods = ['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
        
    task = Task(title = request.json['title'],description=request.json.get('description', ""),done=False)
    db.session.add(task)
    db.session.commit()
    
    return jsonify(  task = task.to_json() ), 201


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['GET'])
def get_task(task_id):
    task = Task.query.filter_by(id = task_id).first()
    if task == None:
        abort(404)
    return jsonify(  task = task.to_json()  )

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['PUT'])
def update_task(task_id):
    task = Task.query.filter_by(id = task_id).first()
    if task == None:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task.title = request.json.get('title', task.title)
    task.description = request.json.get('description', task.description)
    task.done = request.json.get('done', task.done)
    
    db.session.flush()
    db.session.commit()
    
    return jsonify( task = task.to_json() )

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['DELETE'])
def delete_task(task_id):
    task = Task.query.filter_by(id = task_id).first()
    if task == None:
        abort(404)
    db.session.delete(task)
    db.session.commit()
    
    return jsonify( { 'result': True } )