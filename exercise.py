class Task:

 def __init__(self, description, due_date):
     self.description = description
     self.due_date = due_date
def __str__(self):
    return ("This task is about {} and it is due {}.".format(self.description, self.due_date))

task1 = Task("draw", "Jan 10")
print(task1)

task2 = Task("run", "Jan 11")
print(task2)

task3 = Task("swim", "Jan 12")
print(task3)
