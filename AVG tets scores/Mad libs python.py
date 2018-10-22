
##adj1= input("enter a  adjective")
##adj2= input("enter a adjective")
##bird= input("enter a type of bird")
##room= input("enter a room in a house")
##pastverb= input("enter a verb in past tense")
##verb1= input("enter a verb")
##name1= input("enter a relativ's name")
##noun1= input("enter a noun")
##liquid= input("enter a liquid")
##verbing= input("enter a ver ending in -ing")
##bodyparts= input("enter a part of the body (plural)")
##pluralNoun= input("enter a plural noun")
##verbing2= input("enter a verb ending in -ing")
##noun2= input("enter a noun")
##
##
##print("It was a "+adj1+", cold Nevember day. I woke up to the "+adj2+" smell of "+bird+" roasting in the "+room+" downstairs. I "+pastverb+" down the stairs to see if I could help "+verb1+" the dinner. My mom said, 'See if"+name1+
##      " needs a fresh",noun1,
##      ".' So I carried a tray of glasses full of "+liquid+" into the "+verbing+" room. When I got there, I couldn't believe my "+bodyparts+ "! There were "+pluralNoun+ verbing2+" on the "+noun2+"!")


score1=input("score")
score2=input("score")
score3=input("score")
score4=input("score")
score5=input("score")
score6=input("score")
sumx = int(score1)+int(score2)+int(score3)+int(score4)+int(score5)+int(score6)
avg=sumx / 6

def grade():

    if avg >= 90:
        grade = "A"
        return grade
    elif avg >= 80 and avg< 90:
        grade = "B"
        return grade
    elif avg >= 70 and avg< 80:
        grade = "C"
        return grade
    elif avg >= 60 and avg< 70:
        grade = "D"
        return grade
    else:
        grade = "F"
        return grade
 
print ("your grade is an: ", grade())

input()
      
