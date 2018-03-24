'''
定义一个学生类，用来形容学生
'''

class Student():
    pass
#一个空类，pass代表直接跳过
#pass必须有
#定义一个对象
mingyue = Student()

#再定义一个类，用来描述学python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = 'Python'

    #1.注意def dohomework的缩进
    #2.系统默认有一个self参数
    def dohomework(self):
        print('在写作业')

        #推荐在函数末尾使用return语句
        return None

# 实例化一个叫杜哲的学生，是一个具体的值
duzhe = PythonStudent()
print(duzhe.name)
print(duzhe.age)
duzhe.dohomework()

print(PythonStudent.__dict__)
print(duzhe.__dict__)






class Teacher():
    name = '神魔恋'
    age = 20

    def say(self):
        self.name = 'duzhe'
        self.age = 21
        print('name is {}'.format(self.name))
        print('age is {}'.format(self.age))
    def sayAgain():
        print(__class__.name)
        print(__class__.age)
        print('你好，很高兴再次见到你')
t = Teacher()
t.say()
#调用绑定型变量时，要用类名调用，不能用对象名调用
Teacher.sayAgain()