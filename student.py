#Name: Benjamin Del Barrio
#Email: Benjamin.delbarrio31@myhunter.cuny.edu

mess = input("Enter a phrase: ")
MESS = mess.upper()
print("Your Phrase in Capital Letters:", "MESS")
message = MESS.split()
acronym = ""
for i in message :
    acronym += i[0]
print("Acronym:", acronym)
