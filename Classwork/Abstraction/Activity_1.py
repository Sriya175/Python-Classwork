from abc import ABC, abstractmethod

class Abclass(ABC):

    def print(self,x):
        print("Passed value: ", x)

    @abstractmethod
    def task(self):
        print("We are inside Abclass task")

class test_class(Abclass):
    def task(self):
        print("We are inside the test_class task")

test_obj = test_class()
test_obj.task()
test_obj.print(100)

