import datetime
import math 

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
        age_round = math.ceil(planet_age)
        remainder = age_round - planet_age
        no_of_planet_remainder_days = remainder * no_of_days
        date_of_next_planet_birthday = today + datetime.timedelta(days = no_of_planet_remainder_days - 1)
        age_next_planet_birthday = math.ceil(planet_age)

        print("----------------------------")
        print(self.name.upper())
        print("Your current " + self.name + " age is: " + str("%.2f" % planet_age) + " years old")
        print("The date of your next " + self.name + " birthday is: " + date_of_next_planet_birthday.strftime("%A %d %B %Y"))
        
        '''
        #To be used to test calculations for each birthday for error 
        print("")
        print("UNIT TESTING") 
        print("Planet age: " + str(planet_age))
        print("Rounded planet age: " + str(age_round))
        print("Remainder: " + str(remainder))
        print("Number of remainder planet days: " + str(no_of_planet_remainder_days))
        print("Date of next planet birthday: " + date_of_next_planet_birthday.strftime("%A %d %B %Y"))
        print("Age on next planet birthday: "+ str(age_next_planet_birthday))
        print("----------------------------")
        '''

    def planet_info(self, no_of_days=()):
        print(str(no_of_days) + " days equals one year on " + str(self.name))

    def get_age(self, year, month, day):
        DOB = datetime.datetime(self.year, self.month, self.day)
        Age = (today -  DOB)
        convertdays = int(Age.days)
        AgeYears = convertdays/365.25
        print("Your birthdate: " + DOB.strftime("%A %d %B %Y"))
        print("Your current Earth age is: " + str("%.2f" % AgeYears + " years old"))       
        

mercury = Planet('Mercury', 87.97, 1990, 5, 11)
mercury.calculateplanetage(1990, 5, 11, 87.97)
#mercury.planet_info(87.97) for planet information
#mercury.get_age(1990, 5, 11) for age only

venus = Planet('Venus', 224.7, 1990, 5, 11)
venus.calculateplanetage(1990, 5, 11, 224.7)

earth = Planet('Earth', 365.25, 1990, 5, 11)
earth.calculateplanetage(1990, 5, 11, 365.25)

mars = Planet('Mars', 686.98, 1990, 5, 11)
mars.calculateplanetage(1990, 5, 11, 686.98)    

jupiter = Planet('Jupiter', 4332, 1990, 5, 11)
jupiter.calculateplanetage(1990, 5, 11, 4332)    

saturn = Planet('Saturn', 10760.85, 1990, 5, 11)
saturn.calculateplanetage(1990, 5, 11, 10760.85) 

uranus = Planet('Uranus', 30685, 1990, 5, 11)
uranus.calculateplanetage(1990, 5, 11, 30685) 

neptune = Planet('Neptune', 60152, 1990, 5, 11)
neptune.calculateplanetage(1990, 5, 11, 60152)


    