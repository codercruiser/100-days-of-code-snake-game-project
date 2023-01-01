class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print('doing this underwater.')


    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.breathe()

# understanding slicing
# works for both lists and turples
# example
piano_keys = ['a','b','c','d','e','f','g']

print(piano_keys[2:5])
print(piano_keys[:4])
print(piano_keys[1:])
print(piano_keys[:6])
# start from a place and omit the next
print(piano_keys[2:5:2])
# go through all list and omit one after the other
print(piano_keys[::2])
print(piano_keys[::3])
# reverse the lisat
print(piano_keys[::-1])