import time
score= 0
print('Your title')
print()
print()
time.sleep(1)
print('Your first question is:')
time.sleep(1)
print('What is Ubuntu 13 known as')
time.sleep(1)
print('a. Trusty Tahr')
print('b. Saucy Salamander')
print('c. Precise Pangolin')
answer = input('Make your choice\n: ')
if answer == "b":
    print("Correct")
    score +=1
else:
        print('Incorrect')
          
time.sleep(2)
print('---------')
print('TEST COMPLETED')
print('--------')
time.sleep(1)
print('Your final score was %s' %(score))
          
          
