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