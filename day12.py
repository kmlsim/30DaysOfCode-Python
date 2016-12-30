# -*- coding: utf-8 -*-
#!/bin/py =thon

class Person(object):
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print "Name:", self.lastName + ",", self.firstName
		print "ID:", self.idNumber

class Student(Person):
# code goes here

    sumScore = 0

    def __init__(self, firstName, lastName, idNumber, scores):
        #self.numScores = numScores
        self.scores = []

    def calculate(self):

        for i in numScores:
            sumScore = sumScore + scores[i]

        avarage = sumScore / numScores

        if (avarage >= 90 and avarage <= 100):
            return "O"
        elif (avarage >= 80 and avarage < 90):
            return "E"
        elif (avarage >= 70 and avarage < 80):
            return "A"
        elif (avarage >= 55 and avarage < 70):
            return "P"
        elif (avarage >= 40 and avarage < 55):
            return "D"
        else:
            return "T"


line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
#numScores = int(raw_input()) # not needed for Python
scores = map(int, raw_input().split())
print scores
numScores = len(scores)

if (firstName < 4 and firstName > 10):
    print "Your first name is out of range."

if (lastName < 4 and lastName > 10):
    print "Your last name is out of range."

if (len(idNum) != 7):
    print "Id must have 7 digits."

if (scores < 0 and scores > 100):
    print "Score out of range."

if (numScores < 0 and numScores > 100):
    print "Number of scores out of range."

s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()
