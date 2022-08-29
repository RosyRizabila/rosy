# class Person:
#     def say_hi(self):
#         print('Hello, how are you?')

# p = Person()
# p.say_hi()

class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)
p = Person('Rosy')
p.say_hi()