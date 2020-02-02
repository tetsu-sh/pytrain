#ラムダ関数

l=["Mon","tue","wed","thu","fri","Sat","Sun"]

def change_words(words,func):
    for word in words:
        print(func(word))
def function(word):
    return word.capitalize()

change_words(l,lambda word: word.capitalize())
change_words(l,function)

#クラス

class Person():
        def __init__(self,name):
                self.name=name
        def say_something(self):
                print("I am {}. hello".format(self.name))

person=Person("chim")
person.say_something()

#クラスの継承、オーバーライド、super
class Car():
        def __init__(self,model=None):
                self.model=model
        def run(self):
                print("run")
class ToyotaCar(Car):
        def run(self):
                print("fast")

class TeslaCar(Car):
        def __init__(self,model="Model S",enable_autorun=False):
        super().__init__(model)
        self.enable_autorun = enable_autorun

        def run(self):
                print("super fast")
        def autorun(self):
                print("autorun")

car=Car()
car.run()

toyotacar=ToyotaCar("lexas")
print(toyotacar.model)
toyotacar.run()

teslacar=TeslaCar()
print(teslacar.model)
teslacar.run()
teslacar.autorun()


class Car():
        def __init__(self,model=None):
                self.model=model
        def run(self):
                print("run")

class TeslaCar(Car):
        def __init__(self,model="dafd",speed=""):
                super().__init__(model)
                self.speed=speed
        def run(self):
                print("run"+self.speed)

teslacar=TeslaCar("dfljk","fast")
print(f'{"-"*10}')
teslacar.run()
print(teslacar.model)

#キーワードIN数
args=list(range(1,10))
kwargs={"sep":""}
print(*args,**kwargs)

#リスト内包標記
from pprint import pprint

loglist = [['1/1', '晴れ'],
           ['1/2', '晴れ'],
           ['1/3', '曇り'],
           ['1/4', '雨'],
           ['1/5', '雨'],
           ['1/6', '曇り'],
           ['1/7', '晴れ']]
loglist2 = [[it[i] for it in loglist] for i in range(2)]
pprint(loglist2)