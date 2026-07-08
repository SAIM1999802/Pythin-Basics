## Constructor
# from datetime import date
# from turtle import title
# from pydantic import BaseMod1

# class Employee :
#     def __init__(self , name , salary):
#         self.name = name
#         self.salary = salary

#     def calcBon(self):
#         return self.salary*0.1

# emp1 = Employee("Mohan" , 100000)
# emp2 = Employee("Mahesh" , 150000)

# print(emp2.calcBon())


# class human:
#     def __init__(self,name,birth_year) :
#          self.name = name
#          self.birth_year = birth_year
#     def get_age(self):
#         current_year = date.today().year
#         return current_year - self.birth_year
#     def intro(self):
#         return f"Asalam o alaikum my name is {self.name}. I am {self.get_age()} yrs old. I was born in {self.birth_year}"


# h1 = human("Saim" , 2004)
# h2 = human("Ahmed",2008)
# h3 = human("Furqan",2007)

# print(h1.intro())
# print(h2.intro())
# print(h3.intro())



# class recipe(BaseMod1):
#     title : str
#     calories : int


# Exercise: YouTubeChannel class
# Time to build your own blueprint! Create a class YouTubeChannel that models a channel's subscribers.
# our class should have:
# __init__(self, name) — store the channel name and start subscribers at 0.
# subscribe(self) — add 1 subscriber and print "Thanks for subscribing! Total: ".
# unsubscribe(self) — remove 1 subscriber (but never go below 0!) and print the new total.
# show(self) — print " has  subscribers".
# codebasics = YouTubeChannel("codebasics")
# codebasics.subscribe()
# codebasics.subscribe()
# codebasics.subscribe()
# codebasics.unsubscribe()
# codebasics.show()


class YtChannel:
    def __init__(self , name):
        self.name = name
        self.subscribers = 0

    def subscribe(self):
        self.subscribers += 1
        return f"Thankyou for Subscribing CodeBasics : Total Subscribers {self.subscribers}"

    def Unsubscribe(self):
        if self.subscribers > 0:
           self.subscribers -= 1
        return f"Total Subscribers {self.subscribers}"

    def show(self):
        return f"Total Subscribers for channel {self.name} are {self.subscribers}"


codebasics = YtChannel("Codebasics")
print(codebasics.subscribe())
print(codebasics.subscribe())
print(codebasics.subscribe())
print(codebasics.Unsubscribe())
print(codebasics.show())
