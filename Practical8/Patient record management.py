class patient(object):
    def __init__(self,name,age,latest_admission,history):
        self.name=name
        self.age=age
        self.latest_admission=latest_admission
        self.history=history
    
    def call(self):
        print(self.name,self.age,self.latest_admission,self.history)

patient1=patient('Mike',18,'2024_1_1','Noun')

patient1.call()