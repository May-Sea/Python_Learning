class GrandFather: # 基类
    def eat(self):
        print('吃的 方法')
        pass
    pass
class Father(GrandFather): # 派生类
    def eat(self): # 因为父类中已经存在这个方法 在这里相当于 方法重写【方法覆盖了】
        print('爸爸经常吃海鲜')
        pass
    pass
class Son(Father):
    pass

son=Son()
print(Son.__mro__)
son.eat() # 此方法 是从GrandFather继承过来的
G=GrandFather()
G.eat()