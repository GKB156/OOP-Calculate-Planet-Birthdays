import datetime
import math 

today = datetime.datetime.now()

class Planet(object):
    def __init__(self, name):
        self.name = name
        
    def calculateplanetage(self, year, month, day, no_of_days=()):
        self.no_of_days = no_of_days
        self.year = year
        self.month = month
        self.day = day 
        DOB = datetime.datetime(self.year,self.month,self.day)
        Age = (today - DOB)
        convertdays = int(Age.days)
        planet_age = convertdays/no_of_days #age divided by no of earth days in planet year
        age_round = math.ceil(planet_age)
        remainder = age_round - planet_age
        no_of_planet_remainder_days = remainder * no_of_days
        date_of_next_planet_birthday = today + datetime.timedelta(days = no_of_planet_remainder_days - 0.5)
        age_next_planet_birthday = math.ceil(planet_age)

        if today == date_of_next_planet_birthday:
            print("Happy " + str(self.name) + " Birthday!!")

        '''
        #To be used to test calculations for each planet 
        print("")
        print("CALCULATION TESTING") 
        print("Planet age: " + str(planet_age))
        print("Rounded planet age: " + str(age_round))
        print("Remainder: " + str(remainder))
        print("Number of remainder planet days: " + str(no_of_planet_remainder_days))
        print("Date of next planet birthday: " + date_of_next_planet_birthday.strftime("%A %d %B %Y"))
        print("Age on next planet birthday: "+ str(age_next_planet_birthday))
        print("----------------------------")
        '''    

        print("----------------------------")
        print(self.name.upper())
        print("Your current " + self.name + " age is: " + str("%.2f" % planet_age) + " years old")
        print("The date of your next " + self.name + " birthday is: " + date_of_next_planet_birthday.strftime("%A %d %B %Y")) 

    def planet_info(self, no_of_days=()):
        print(str(no_of_days) + " days equals one year on " + str(self.name))

    def get_age(self, year, month, day):
        DOB = datetime.datetime(self.year, self.month, self.day)
        Age = (today -  DOB)
        convertdays = int(Age.days)
        AgeYears = convertdays/365.25
        print("Your birthdate: " + DOB.strftime("%A %d %B %Y"))
        print("Your current Earth age is: " + str("%.2f" % AgeYears + " years old"))
   

'''
For planet information, type the name of the planet followed by .planet_info(insert number of planet days)
For a specific planet age, using your birthday, type the name of the planet followed by .get_age(yyyy, mm, dd)
'''

mercury = Planet('Mercury')
mercury.calculateplanetage(1990, 2, 1, 87.97)

venus = Planet('Venus')
venus.calculateplanetage(1990, 2, 1, 224.7)

earth = Planet('Earth')
earth.calculateplanetage(1990, 2, 1, 365.25)

mars = Planet('Mars')
mars.calculateplanetage(1990, 2, 1, 686.98)    

jupiter = Planet('Jupiter')
jupiter.calculateplanetage(1990, 2, 1, 4332)    

saturn = Planet('Saturn')
saturn.calculateplanetage(1990, 2, 1, 10760.85) 

uranus = Planet('Uranus')
uranus.calculateplanetage(1990, 2, 1, 30685) 

neptune = Planet('Neptune')
neptune.calculateplanetage(1990, 2, 1, 60152)


    