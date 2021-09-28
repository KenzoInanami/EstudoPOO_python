class Person(object):
    def __init__(self, name, age):
        self._name = name.title()
        self._age = int(age)

    def anniversary(self):
        self._age += 1

    @property
    def age(self):
        return self._age

    def __str__(self):
        return f'{self._name} | {self._age}'


class Student(Person):
    def __init__(self, name, age, course, semester):
        super().__init__(name, age)
        self._course = course.title()
        self._semester = semester

    def __str__(self):
        return f'{self._name} | {self._course} | {self._semester}'


class Group():
    def __init__(self, name, students):
        self.name = name
        self._group = students

    def __getitem__(self, name):
        return self._group[name]

    def __len__(self):
        return len(self._group)


def main():
    # student objects
    jonas = Student('jonas augusto', 26, 'medicine', 2)
    maria = Student('maria benedita', 21, 'medicine', 3)
    afonso = Student('afonso bennett', 22, 'medicine', 1)
    pedro = Student('pedro york', 25, 'medicine', 3)

    # person.anniversary test
    print(f'Before anniversary(): {jonas.age}')
    jonas.anniversary()
    print(f'After anniversary(): {jonas.age}')

    print()

    print('Testing group class')
    group = [jonas, maria, afonso, pedro]  # create a list
    group = Group('Group 1', group)  # create object group
    for student in group: # test iterator
        print(student)
    print(len(group))  # test __len__


main()
