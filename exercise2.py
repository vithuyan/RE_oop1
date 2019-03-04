from exercise import Task



class Todo:
    Todo_list = []


def __init__(self, tasks):
    self.tasks = tasks

@classmethod
def add_task(cls, description, due_date):
    task = Task(description, due_date)
    cls.Todo_list.append(task)
    return cls.Todo_list
         
