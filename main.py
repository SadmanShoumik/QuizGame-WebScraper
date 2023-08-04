import requests
import csv

import bs4 as beautiful_soup

import quiz

page = requests.get('https://www.includehelp.com/mcq/oops-mcqs.aspx')
soup = beautiful_soup.BeautifulSoup(page.content, 'html.parser')

#ADDING QUESTIONS TO THE GAME
questions = soup.select("p b")

qbank = []
i=0
for str in questions:
    i=i+1
    if i%3 == 1:
        qbank.append(str.text)



with open('questions.txt', 'w') as f:
    for i in range(0, 100):
        f.write(qbank[i])
        f.write("\n")


#ADDING EXPLANATIONS FOR THE QUESTION
explanations = soup.select("p")
ebank = []

str = ""
for i in range(0, 504):
    str = explanations[i].text
    if(str.__contains__("Explanation:")):
        ebank.append(explanations[i+1])


with open('explanations.txt', 'w') as f:
    for i in range(0, 100):
        f.write(ebank[i].text)
        f.write("\n")


#ADDING THE ANSWERS TO THE QUESTIONS
answers = soup.select("p")
abank = []

str = ""
for i in range(0, 504):
    str = answers[i].text
    if(str.__contains__("Answer:")):
        str = str.replace("Answer: ", "")
        abank.append(str)


with open('answers.txt', 'w') as f:
    for i in range(0, 100):
        f.write(abank[i])
        f.write("\n")

#ADDING THE OPTIONS PROVIDED TO THE PLAYER
options = soup.select("ol",)
obank = []

i=0
for str in options:
    i=i+1
    if(i==56 or i==93):
        continue
    obank.append(str.text)

with open('options.txt', 'w') as f:
    for i in range(0, 100):
        f.write((i+1).__str__())
        f.write(obank[i])


quiz.rungame()