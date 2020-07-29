class Person(object):
    def __init__(self, name):
        self.name = name


p1 = Person(name='coco')
setattr(p1, 'age', 10)
print(p1.age)
