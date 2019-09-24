
class Student:

    school = "Sajjad University"

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def average(self):
        return (self.m1 + self.m2)/2
    
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3
    def __gt__(self, other):
        r1 = self.m1 + self.m1
        r2 = other.m1 + other.m2
        
        if r1 > r2:
            return True
        else:
            False



s1 = Student(23, 33)
s2 = Student(44, 585)
if s1 > s2:
    print("I am s1")
else:
    print("I am s2")

s3 = s1 + s2
print(s3.m1)