import sys
import operator
command = ''

class To_doList:

    def __init__(self,username):
        self.todos = []
        self.username = username
        #TODO check if user already exists
        self.filename = username + '.txt'
        self.getFile()

    def switchUser(self,name):
        self.writeFile()
        self.filename = name + '.txt'
        self.getFile()

    def getFile(self):
        self.todos = []
        try:
            with open(self.filename,'r') as f:
                for line in f:
                    if line != None:
                        temp = line.split()
                        self.todos.append(To_do(temp[0],' '.join(temp[1:3]),' '.join(temp[3:])))
        except IOError:
            pass
    def writeFile(self):
        with open(self.filename,'w') as f:
            for t in self.todos:
                f.write(t.getTask() + '\n')

    def append(self,t):
        self.todos.append(t)

    def remove(self,t):
        temp = int(t)
        temp = temp - 1
        self.todos.pop(temp)

    def sort(self, c = 'priority'):
        if c not in self.todos:
            c = 'priority'
        self.todos.sort(key=operator.attrgetter(c))

    def display(self):
        print '{0:^8} {1:^20} {2:<50}'.format('Priority', 'Date & Time', 'Description')
        for t in self.todos:
            print t.getTask()
        self.writeFile()


class To_do:
    def __init__(self,priority,time,desc):
        self.description = desc
        self.priority = priority
        self.time = time
    def getTask(self):
        return '{0:^8} {1:^20} {2:<50}'.format(self.priority, self.time, self.description)
def exit_fun(t):
    todos.writeFile()
    sys.exit(0)
def add_fun(desc):
    from time import strftime
    temp = desc.split()
    todos.append(To_do(temp[0],strftime("%Y-%m-%d %H:%M:%S"),' '.join(temp[1:])))
def remove_fun(num):
    todos.remove(num)
def sort_fun(t):
    todos.sort(t)
def switch_fun(name):
    todos.switchUser(name)

fun = {
'quit':exit_fun,
'add':add_fun,
'remove':remove_fun,
'sort':sort_fun,
'switch':switch_fun
}

print 'Please enter user'
print ' '
user = raw_input()
todos = To_doList(user)
print ' '
print 'To add to the list use the format "add \'priority description\'"'
print 'To remove from the list use the format "remove \'number\'"'
print 'To sort list based on priority use "sort \'attribute\'"'
print 'To switch user use "switch \'username\'"'
print '\'Quit\' to exit'
print ' '
todos.display()
print ' '
while True:
  line = raw_input()
  temp = line.split()
  command = temp[0]
  if command in fun:
      fun[command](' '.join(temp[1:]))
  print ' '
  todos.display()
  print ' '
