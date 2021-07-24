questionNumber = input("Question Number: ")
nameOfQuestion = input("Name of Question: ")
linkOfQues = input("Link Of Question: ")
difficultyOfQuestion = input("Difficulty Level: ")
from datetime import date
today = date.today()
d1 = today.strftime("%d_%m_%Y")
questionSolved = [questionNumber, nameOfQuestion, linkOfQues, difficultyOfQuestion]
fileName = d1 + ".csv"
import os
from csv import writer
if(os.path.exists(fileName)):
    print("[*] Appending Question...\n")
    with open(fileName, 'a+', newline='') as write_obj:
        writer_obj = writer(write_obj)
        writer_obj.writerow(questionSolved)
    print("[*] Success!!\n")
else:
    print("[*] File Does not exist, creating file...\n")
    with open(fileName, 'w', newline='') as write_obj:
        writer_obj = writer(write_obj)
        writer_obj.writerow(questionSolved)
    print("[*] Success.\n")
os.system("git add ./")
s = "git commit -m " + "\"" + "Question " + questionNumber + " " + nameOfQuestion + " " + linkOfQues + " " + difficultyOfQuestion + " " + d1 + "\""
os.system(s)
input()





