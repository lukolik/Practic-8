# # class User():

# #     countUser = 0

# #     def __init__(self, firestName, age):
# #         User.countUser += 1
# #         self.__firestName = firestName
# #         self.__age = age

# #     def getCU(self):
# #         return self.countUser
    

# # u = User("User1", 12)
# # u2 = User("User2", 22)


# # print(u2.getCU())  




# # class Human():
    
# #     counter = 0

# #     def __init__(self, name):
# #         Human.counter += 1
# #         self._name = name
    
# #     def getName(self):
# #         return self._name

# #     def setName(self, name):
# #         self._name = input()

# #     def getCounter(self):
# #         return Human.counter
    
# #     def out(self):
# #         print("Human = " , self._name)



# # class Builder(Human):
    
# #     counter = 0
    
# #     def __init__(self, name, prof):
# #         super().__init__(name)
# #         Builder.counter += 1
# #         self.__prof = prof
    
# #     def getName(self):
# #         return self.__prof

# #     def setName(self, name):
# #         self.__prof = input()

# #     def getCounter(self):
# #         return Builder.counter
    
# #     def out(self):
# #         print("Bulder = ", self.__prof)




# # class Sailor(Human):
    
# #     counter = 0

# #     def __init__(self, name, prof):
# #         super().__init__(name)
# #         Sailor.counter += 1
# #         self.__prof = prof

# #     def getName(self):
# #         return self.__prof

# #     def setName(self, name):
# #         self.__prof = input()

# #     def getCounter(self):
# #         return Sailor.counter
    
# #     def out(self):
# #         print("Soilor = " , self.__prof)

        


# # class Pilot(Human):
    
    
# #     counter = 0

# #     def __init__(self, name, reis):
# #         super().__init__(name)
# #         Pilot.counter += 1
# #         self.__reis = reis

# #     def getName(self):
# #         return self.__reis

# #     def setName(self, name):
# #         self.__reis = input()

# #     def getCounter(self):
# #         return Pilot.counter
    
# #     def out(self):
# #         print("Pilot = ", self.__reis)

# # list = [Human("User"), Builder("builder", "welder"), Sailor("Jack", "Cap"), Pilot("Ivan", 100)]

# # def out(list):
# #     for el in list:
# #         el.out()

# # out(list)
# # print()

# # def getCounter(list):
# #     for el in list:
# #         print(el.getCounter())

# # getCounter(list)

# class Passport:

#     counter = 0

#     def __init__(self, firstName, lastName, city, adress, age, birsday, registr, famaly, gender):
        
#         Passport.counter += 1
        
#         self._firstName = firstName
#         self._lastName = lastName
#         self._city = city
#         self._adress = adress
#         self._age = age
#         self._birsday = birsday
#         self._registr = registr
#         self._famaly = famaly
#         self._gender = gender
        



#     def getCounter(self):
#         return Passport.counter

    
    
    
#     def getfirstName(self):
#         return self._firstName
    
#     def setfirstName(self, firstName):
#          self._firstName = firstName
    
#     property(getfirstName, setfirstName)



#     def getlastName(self):
#         return self._lastName
    
#     def setlastName(self, lastName):
#          self._lastName = lastName
    
#     property(getlastName, setlastName)



#     def getcity(self):
#         return self._city
    
#     def setcity(self, city):
#          self._city = city
    
#     property(getcity, setcity)



#     def getadress(self):
#         return self._adress
    
#     def setadress(self, adress):
#          self._adress = adress
    
#     property(getadress, setadress)



#     def getage(self):
#         return self._age
    
#     def setage(self, age):
#          self._age =  age
    
#     property(getage, setage)



#     def getbirsday(self):
#         return self._birsday
    
#     def setbirsday(self, birsday):
#          self._birsday = birsday
    
#     property(getbirsday, setbirsday)




#     def getregistr(self):
#         return self._registr
    
#     def setregistr(self, registr):
#          self._registr =  registr
    
#     property(getregistr, setregistr)



#     def getfamaly(self):
#         return self._famaly
    
#     def setfamaly(self, famaly):
#          self._famaly = famaly
    
#     property(getfamaly, setfamaly)

    
    
#     def getgender(self):
#         return self._gender
    
#     def setgender(self, gender):
#          self._gender = gender
    
#     property(getgender, setgender)

    
   

    
    
#     def out(self):
#         print(self._firstName,  self._lastName, self._city, self._adress, self._age, self._birsday,
#               self._registr, self._famaly, self._gender)
        
    
        


# class ForeignPassport(Passport):

#     counter = 0

#     def __init__(self, firstName, lastName, city, adress, age, birsday, registr, famaly, gender, nomerForeing, viza):
#         super().__init__(firstName, lastName, city, adress, age, birsday, registr, famaly, gender)
#         self.__nomerForeing = nomerForeing
#         self.__viza  = viza
    
#     def getCounter(self):
#         return ForeignPassport.counter
    
#     def getnomerForeing(self):
#         return self.__nomerForeing
    
#     def setnomerForeing(self, nomerForeing):
#         self.__nomerForeing =  nomerForeing

#     property(getnomerForeing, setnomerForeing)


#     def getviza(self):
#         return self.__viza
    
#     def setviza(self, viza):
#         self.__viza = viza

#     property(getviza, setviza)


#     def out(self):
#         print(self.__nomerForeing, self.__viza)
        

# list = [Passport("Misha", "lukin", "sochi", "1233", 22, "test", 2314, "test", "test"), ForeignPassport( "Misha", "lukin", "sochi", "1233", 22, "test", 2314, "test", "test", 12, 2222) ]

# def out(list):
#     for el in list:
#         el.out()

# out(list)


# print()

# def getCounter(list):
#     for el in list:
#         print(el.getCounter())

# getCounter(list)

        
# class Figur():
#     def __init__(self, a, b, h, d1, d2, S):
#         self.a = a
#         self.b = b
#         self.h = h
#         self.d1 = d1
#         self.d2 = d2
#         self.S = S

#     def getOut(self):
#         return self.S
    
#     def setOut(self, a, b, h, d1, d2, S):
#         input1 = input("1 Square, 2 Triangle, 3 Rhomb")

#         if input1 == 1:
#             self.S =  self.a * self.a
#         elif input1 == 2:
#             self.S =  (1/2) * self.h * self.a
#         else:
#             self.S = (1/2) * self.d1 * self.d2
        
#     figur =   property(getOut, setOut)


                
        
    




        