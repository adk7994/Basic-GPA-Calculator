#gpaOne=4
#creditsOne=6
gpaOne=int(input("First grade: "))
creditsOne=int(input("How many credits was that class worth?"))
#gpaTwo=3
#creditsTwo=5
gpaTwo=int(input("Second grade: "))
creditsTwo=int(input("How many credits was that class worth?"))
#gpaThree=2
#creditsThree=1
gpaThree=int(input("Third grade: "))
creditsThree=int(input("How many credits was that class worth?"))

totalCredits = creditsOne+creditsTwo+creditsThree

weightedOne=gpaOne*creditsOne
weightedTwo=gpaTwo*creditsTwo
weightedThree=gpaThree*creditsThree

totalWeighted=weightedOne+weightedTwo+weightedThree

finalGPA=round(
totalWeighted/totalCredits, 2)
#finalGPA=round( (weightedOne+weightedTwo+weightedThree)/(creditsOne+creditsTwo+creditsThree), 2)

print ("Your GPA is: ", finalGPA)


