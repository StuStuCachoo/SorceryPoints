#1st	2
#2nd	3
#3rd	5
#4th	6
#5th	7

def AddToAllSlots(allSlots, curSlots, slotToAdd):
	for i in range(len(curSlots)):
		if(slotToAdd >=0 and slotToAdd <=4):
			curSlots[i][slotToAdd]+=1
		allSlots.append(curSlots[i])
	return allSlots
	
def OneSlot(spLimit, spLeft, rechargesLeft):
	if(spLimit >= spLeft+2 and rechargesLeft != 0):
		return OneSlot(spLimit, spLeft+2, rechargesLeft-1)
	allSlots = []
		
	if(rechargesLeft > 0 and spLimit > spLeft):
		#At this point we know spLeft is spLimit-1
		curSlots = OneSlot(spLimit, spLeft+1, rechargesLeft-1)
		allSlots = AddToAllSlots(allSlots, curSlots, -1)
	
	if(spLeft >= 7):
		curSlots = OneSlot(spLimit, spLeft-7, rechargesLeft)
		allSlots = AddToAllSlots(allSlots, curSlots, 4)
	
	if(spLeft >= 6):
		curSlots = OneSlot(spLimit, spLeft-6, rechargesLeft)
		allSlots = AddToAllSlots(allSlots, curSlots, 3)
		
	if(spLeft >= 5):
		curSlots = OneSlot(spLimit, spLeft-5, rechargesLeft)
		allSlots = AddToAllSlots(allSlots, curSlots, 2)
		
	if(spLeft >= 3):
		curSlots = OneSlot(spLimit, spLeft-3, rechargesLeft)
		allSlots = AddToAllSlots(allSlots, curSlots, 1)
		
	if(spLeft >= 2):
		curSlots = OneSlot(spLimit, spLeft-2, rechargesLeft)
		allSlots = AddToAllSlots(allSlots, curSlots, 0)
	
	if(rechargesLeft == 0 and spLeft < 2):
		return [[0,0,0,0,0]]
	return allSlots
	
finalSlots = OneSlot(int(raw_input("SP Limit: ")), 0, int(raw_input("Hours of downtime: "))*2)
finalSlots = [finalSlots[i] for i in range(len(finalSlots)) if i == 0 or finalSlots[i] != finalSlots[i-1]]     #removes duplicate elements
print(finalSlots)
