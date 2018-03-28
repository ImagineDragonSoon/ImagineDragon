#property函数案例
#定义一个person类，具有name和age两个属性
#对于任意输入的姓名，我们都希望用大写方式保存
#年龄，我们希望内部统一用整数保存

class person():
    def fget(self):
        return self._name * 2
    def fset(self,name):
        self._name = name.upper()
    def fdel(self):
        self._name = 'NoName'

    name = property(fget,fset,fdel,'对name进行下下操作')


p1 = person()
p1.name = 'TuLing'
print(p1.name)
print('*'*30)


#__call__函数的实例
class A():
    def __init__(self,name = '杜哲'):
        print(233333)
    def __call__(self):
        print('嘻嘻嘻嘻')

a = A()
a()