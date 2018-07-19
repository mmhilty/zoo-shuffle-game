
#ZooConfusion

import random

maxAnimalNumber = 4
masterlist = []
loopsofinput = 0

while loopsofinput < maxAnimalNumber:
  listingElement = raw_input("What's one of the animals in your zoo?")
  masterlist.append(listingElement)
  loopsofinput = loopsofinput + 1


print "Oh no, the animals got out! Nobody wanted to stay in their own cage, so they switched themselves around! Can you guess who went where?"

shuffleList = list(masterlist)
random.shuffle(shuffleList)

rightanswers = 0
thingposition = 0
while rightanswers < loopsofinput:
  UserAnswer = raw_input("Who do you think is in Habitat " + str(thingposition + 1)+ "?")
  if UserAnswer == shuffleList[thingposition]:
    print ("You are correct!")
    if shuffleList[thingposition] == masterlist[thingposition]:
      print("It looks like the " + str(shuffleList[thingposition]) + " was too comfy to move. Let's go find the others.")
    else:
      print("You found the " + str(shuffleList[thingposition]) + " in Habitat " + str(thingposition + 1) + " instead of the " + masterlist[thingposition] + ". What a silly place for it to be!")
    rightanswers = rightanswers + 1
    thingposition = thingposition + 1
  else:
    print ("Nope! Try again.")



print ("You found all of the animals! Good job! Now it's time to get them back in their correct habitats. Uh oh...")
print ("Here's your zoo:")
print (masterlist)
