# *-* coding:utf-8 *-*

def getTaskByID(int a,list tasks):
	for task in tasks:
		if task['id'] == a:
			return task
	return None;




