initialCapital = 20000
percent = 0.03
maxTimeYears = 10
year=0
capital=initialCapital
while year<maxTimeYears:
    year+=1
    capital=round((1+percent)*capital,2)
    print('after this year:', year,  'you will have:',capital)
else:
    print('the total revenue is', capital-initialCapital)
print('-------------------------------------------------------')

tekst='United Space Alliance: This company provides major support to NASA for\
various projects, such as the space shuttle. One of its projects is to\
create Workflow Automation System (WAS), an application designed to\
manage NASA and other third-party projects. The setup uses a central\
Oracle database as a repository for information. Python was chosen over\
languages such as Java and C++ because it provides dynamic typing and\
pseudo-code–like syntax and it has an interpreter. The result is that\
the application is developed faster, and unit testing each piece is easier.'

listOfWords=tekst.split(' ')
print(listOfWords)
shortWords=0
longWords=0
wordLength = 6

for word in listOfWords:
    if len(word)>wordLength:
        longWords+=1
    else:
        shortWords+=1
print("Words shorter than ",wordLength,":",shortWords)
print("Words longer than ",wordLength,":",longWords)
