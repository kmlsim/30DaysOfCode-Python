# -*- coding: utf-8 -*-
#!/bin/py =thon
scores = []

class Person():
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print "Name:", self.lastName + ",", self.firstName
		print "ID:", self.idNumber

class Student(Person, object):
# code goes here

    def __init__(self, firstName, lastName, idNumber, scores):
		super(Student, self).__init__(firstName, lastName, idNumber)
 		self.scores = scores

    def calculate(self):
		sumScore = 0
		avarage = 0

		for i in range(numScores):
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
numScores = int(raw_input()) # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()
