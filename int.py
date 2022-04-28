# MUST KNOW BASIC PYTHON

# Init Method
class Sample1:
    def __init__(self, first, last, interest, phone):
        self.first = first
        self.last = last
        self.interest = interest
        self.phone = phone

g1 = Sample1("First Name", "Last Name", "Interest", 1234)
print("Guest last name: " + g1.last)