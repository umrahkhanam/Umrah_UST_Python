from threading import Thread
class Hotel:
    def __init__(self,t):
        self.t=t
    def food(self):
        for i in range(1,11):  #number of table
            print(self.t,i)
h1=Hotel('Take order from table')
h2=Hotel('Server order from table')
t1=Thread(target=h1.food)
t2=Thread(target=h2.food)
t1.start()
t2.start()