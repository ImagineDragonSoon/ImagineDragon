# 继承的语法
# 在python中，任何类都有一个共同的父类叫object
class Person():
    name = 'None'
    age = 0
    _petname = 'sec'#保护变量，子类可以使用，但是不能公用
    __score = 0#私有变量，只有父类可以使用
    def sleep(self):
        print('sleeping...  ...')


# 父类写在括号里
class Teacher(Person):
    pass

t = Teacher()
print(t.name)
print(t.age)
print('*'*10)
t.sleep()
print(t._petname)





#构造函数的概念
class Dog():
    #__init__就是构造函数，每次实例化的时候第一个被调用
    #因为主要工作是进行初始化，所以得名
    def __init__(self):
        print('I am a dog')

yjj = Dog()
print('*' * 30)

class animal():
    pass

class paxing_animal(animal):
    def __init__(self):
        print('PaXing DongWu')

class Dog(paxing_animal):
    def __init__(self):
       print('I am init in dog')

#实例化的时候，自动调用了Dog的构造函数
#调用构造函数时，参数要和定义的时候的参数相匹配
#因为找到了构造函数，所以不再向上查找父类的构造函数
kaka = Dog()

class Cat(paxing_animal):
    pass
#此时自动调用构造函数，因为cat没有构造函数，所以查找父类的构造函数
#在父类中找到了，调用，并且停止查找
gaga = Cat()