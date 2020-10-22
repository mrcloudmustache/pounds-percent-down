#!/usr/bin/env python
# Pounds down calculator


startingWeight = int(input('Enter Starting Weight: '))
currentWeight = int(input('Enter Current Weight: '))
age = int(input('Enter Age: '))

if age > 49:
    poundsDown = ((startingWeight-currentWeight)+(startingWeight*.01))/startingWeight*100
elif age > 59:
    poundsDown = ((startingWeight-currentWeight)+(startingWeight*.02))/startingWeight*100
else:
    poundsDown = ((startingWeight-currentWeight)/startingWeight)*100
    
print('Total Pounds Down(percentage): ' + str(poundsDown) )

