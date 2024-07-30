import torch
import torch.nn as nn

# Bài 1


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        exp = torch.exp(x)
        sum_exp = exp.sum(dim=0)
        return exp / sum_exp


class Softmaxstable():
    def __init__(self):
        super(Softmaxstable, self).__init__()

    def forward(self, x):
        max_x = x.max(dim=0, keepdim=True)[0]
        exp = torch.exp(x - max_x)
        sum_exp = exp.sum(dim=0, keepdim=True)
        return exp / sum_exp

# Bài 2


class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    # Abstract method
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(
            f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")


class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.people:
            person.describe()

    def count_doctor(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))

    def sort_age(self):
        self.people.sort(key=lambda person: person.yob)

    def compute_average(self):
        teachers = [
            person for person in self.people if isinstance(person, Teacher)]
        if not teachers:
            return 0
        total_yob = sum(teacher.yob for teacher in teachers)
        return total_yob / len(teachers)

# Bài 3


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.my_stack = []

    def is_empty(self):
        return len(self.my_stack) == 0

    def is_full(self):
        return len(self.my_stack) == self.capacity

    def pop(self):
        if self.is_empty():
            raise IndexError("Empty stack")
        return self.my_stack.pop()

    def push(self, value):
        if self.is_full():
            raise OverflowError("Full stack")
        self.my_stack.append(value)

    def top(self):
        if self.is_empty():
            raise IndexError("Empty stack")
        return self.my_stack[-1]

# Bài 4


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.my_queue = []

    def is_empty(self):
        return len(self.my_queue) == 0

    def is_full(self):
        return len(self.my_queue) == self.capacity

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty queue")
        return self.my_queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Full queue")
        self.my_queue.append(value)

    def front(self):
        if self.is_empty():
            raise IndexError("Empty queue")
        return self.my_queue[0]
