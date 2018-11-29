import datetime

today = datetime.datetime.now()

class Planet(object):
    def __init__(self, name, no_of_days, year, month, day):
        self.name = name
        self.no_of_days = no_of_days
        self.year = year
        self.month = month
        self.day = day

    def calculateplanetage(self, year, month, day, no_of_days=()):
        DOB = datetime.datetime(self.year,self.month,self.day)
        Age = (today - DOB)
        convertdays = int(Age.days)
        planet_age = convertdays/no_of_days #age divided by no of earth days in planet year
        age_round = round(planet_age)
        remainder = age_round - planet_age
        no_of_planet_remainder_days = remainder * no_of_days
        date_of_next_planet_birthday = today + datetime.timedelta(days = no_of_planet_remainder_days - 1)
        age_next_planet_birthday = round(planet_age)

        print("----------------------------")
        print(self.name.upper())
        print("Your current " + self.name + " age is: " + str("%.2f" % planet_age) + " years old")
        print("The date of your next " + self.name + " birthday is: " + date_of_next_planet_birthday.strftime("%A %d %B %Y"))
        print("----------------------------")    

class Birthday(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day 
    
    def get_age(self, year, month, day):    
        DOB = datetime.datetime(self.year,self.month,self.day)
        Age = (today - DOB)
        convertdays = int(Age.days)
        AgeYears = convertdays/365.25
        print("Your birthdate: " + DOB.strftime("%A %d %B %Y"))
        print("Your current Earth age is: " + str("%.2f" % AgeYears) + " years old.")
        
        
class Mercury(Planet, Birthday):
    def __init__(self):
        #change birthday as desired
        Planet.__init__(self, 'Mercury', no_of_days=(), year=1980, month=01, day=01)

    def planet_info(self, no_of_days=()):
        no_of_days = 87.97
        print(str(no_of_days) + " days equals one year on " + str(self.name))

mercury = Mercury()
mercury.calculateplanetage(1980, 01, 01, 87.97) #call your birthday and no_of_days as yyyy, mm, dd, no_of_days respectively
#mercury.planet_info()
#mercury.get_age(1980, 01, 01)


class Venus(Planet, Birthday):
    def __init__(self):
        Planet.__init__(self, 'Venus', no_of_days=(), year=1980, month=01, day=01)

    def planet_info(self, no_of_days=()):
        no_of_days = 224.7
        print(str(no_of_days) + " days equals one year on " + str(self.name))

venus = Venus()
venus.calculateplanetage(1980, 01, 01, 224.7)



class Earth(Planet, Birthday):
    def __init__(self):
        Planet.__init__(self, 'Earth', no_of_days=(), year=1980, month=01, day=01)

    def planet_info(self, no_of_days=()):
        no_of_days = 365.25
        print(str(no_of_days) + " days equals one year on " + str(self.name))

earth = Earth()
earth.calculateplanetage(1980, 01, 01, 365.25)



class Mars(Planet, Birthday):
    def __init__(self):
        Planet.__init__(self, 'Mars', no_of_days=(), year=1980, month=01, day=01)

    def planet_info(self, no_of_days=()):
        no_of_days = 686.98
        print(str(no_of_days) + " days equals one year on " + str(self.name))

mars = Mars()
mars.calculateplanetage(1980, 01, 01, 686.98)    


class Jupiter(Planet, Birthday):
    def __init__(self):
        Planet.__init__(self, 'Jupiter', no_of_days=(), year=1980, month=01, day=01)

    def planet_info(self, no_of_days=()):
        no_of_days = 4332
        print(str(no_of_days) + " days equals one year on " + str(self.name))

jupiter = Jupiter()
jupiter.calculateplanetage(1980, 01, 01, 4332)    


class Saturn(Planet, Birthday):
    def __init__(self):
        Planet.__init__(self, 'Saturn', no_of_days=(), year=1980, month=01, day=01)

    def planet_info(self, no_of_days=()):
        no_of_days = 10761
        print(str(no_of_days) + " days equals one year on " + str(self.name))

saturn = Saturn()
saturn.calculateplanetage(1980, 01, 01, 10761) 


class Uranus(Planet, Birthday):
    def __init__(self):
        Planet.__init__(self, 'Uranus', no_of_days=(), year=1980, month=01, day=01)

    def planet_info(self, no_of_days=()):
        no_of_days = 60152
        print(str(no_of_days) + " days equals one year on " + str(self.name))

uranus = Uranus()
uranus.calculateplanetage(1980, 01, 01, 60152) 


class Neptune(Planet, Birthday):
    def __init__(self):
        Planet.__init__(self, 'Neptune', no_of_days=(), year=1980, month=01, day=01)

    def planet_info(self, no_of_days=()):
        no_of_days = 90411
        print(str(no_of_days) + " days equals one year on " + str(self.name))

neptune = Neptune()
neptune.calculateplanetage(1980, 01, 01, 90411) 


#why does next planet birthday stop calculating when no_of_days = 16031?    
    