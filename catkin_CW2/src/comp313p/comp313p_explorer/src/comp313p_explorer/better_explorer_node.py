import rospy

from better_explorer_node_base import BetterExplorerNodeBase
from math import *

# This class implements a super dumb explorer. It goes through the
# current map and marks the first cell it sees as the one to go for

class BetterExplorerNode(BetterExplorerNodeBase):

    def __init__(self):
        BetterExplorerNodeBase.__init__(self)
        # self.frontierQueue = []
        self.location = (0, 0)
        # self.blackList = []

    def calculateOctileDistance(self, source, destination):
	if source == (0, 0):
		return 0
	dX = abs(destination[0] - source[0])
	dY = abs(destination[1] - source[1])
	L = max(dX, dY) + (sqrt(2) - 1) * min(dX, dY)
	return L

    def updateFrontiers(self):
# remove non-frontier cells that are still in the list
	
        for item in self.frontierQueue:
		if self.isFrontierCell(item[0], item[1]) is False:
			self.frontierQueue.remove(item)
	for x in range(0, self.occupancyGrid.getWidthInCells()):
		for y in range(0, self.occupancyGrid.getHeightInCells()):
			candidate = (x,y)
			if self.isFrontierCell(x, y) is True:
				candidateGood = True
				# for k in range(0, len(self.blacklist)):
				#	if self.blacklist[k] == candidate:
				#		candidateGood = False
				#		break
			else:
				continue
			if candidateGood is True:
				if self.frontierQueue.count(candidate) == 0:
					self.frontierQueue.append(candidate)

    def moveAlongFrontier(self, item, distance):
	if   self.isFrontierCell(item[0], item[1] + 1) and self.calculateOctileDistance(self.location, (item[0], item[1] + 1)) >= distance:
		return (self.calculateOctileDistance(self.location, (item[0], item[1] + 1)), (item[0], item[1] + 1))
	elif self.isFrontierCell(item[0], item[1] - 1) and self.calculateOctileDistance(self.location, (item[0], item[1] - 1)) >= distance:
		return (self.calculateOctileDistance(self.location, (item[0], item[1] - 1)), (item[0], item[1] - 1))
	elif self.isFrontierCell(item[0] + 1, item[1]) and self.calculateOctileDistance(self.location, (item[0] + 1, item[1])) >= distance:
		return (self.calculateOctileDistance(self.location, (item[0] + 1, item[1])), (item[0] + 1, item[1]))
	elif self.isFrontierCell(item[0] - 1, item[1]) and self.calculateOctileDistance(self.location, (item[0] - 1, item[1])) >= distance:
		return (self.calculateOctileDistance(self.location, (item[0] - 1, item[1])), (item[0] - 1, item[1]))
	elif self.isFrontierCell(item[0] - 1, item[1] - 1) and self.calculateOctileDistance(self.location, (item[0] - 1, item[1] - 1)) >= distance:
		return (self.calculateOctileDistance(self.location, (item[0] - 1, item[1] - 1)), (item[0] - 1, item[1] - 1))
	elif self.isFrontierCell(item[0] - 1, item[1] + 1) and self.calculateOctileDistance(self.location, (item[0] - 1, item[1] + 1)) >= distance:
		return (self.calculateOctileDistance(self.location, (item[0] - 1, item[1] + 1)), (item[0] - 1, item[1] + 1))
	elif self.isFrontierCell(item[0] + 1, item[1] + 1) and self.calculateOctileDistance(self.location, (item[0] + 1, item[1] + 1)) >= distance:
		return (self.calculateOctileDistance(self.location, (item[0] + 1, item[1] + 1)), (item[0] + 1, item[1] + 1))
	elif self.isFrontierCell(item[0] + 1, item[1] - 1) and self.calculateOctileDistance(self.location, (item[0] + 1, item[1] - 1)) >= distance:
		return (self.calculateOctileDistance(self.location, (item[0] + 1, item[1] - 1)), (item[0] + 1, item[1] - 1))
	else:
		return (-1, (-1, -1))

    def chooseNewDestination(self):


#         print 'blackList:'
#         for coords in self.blackList:
#             print str(coords)
	try:
        	candidate = self.frontierQueue[0]
		# return True, candidate
	except: 
		print "Fuck"
		return False, None

	minLength = 1000000
	closestFrontier = candidate
	for candidate in self.frontierQueue:
		dist = self.calculateOctileDistance(self.location, candidate)
		if dist < minLength:
			minLength = dist
			closestFrontier = candidate
	movedAlongFrontierCount = 0
	while movedAlongFrontierCount < 6:
		(newLength, newCandidate) = self.moveAlongFrontier(closestFrontier, minLength)
		if newLength == -1:
			 if movedAlongFrontierCount == 0:
				print "Weird edge case " + str(closestFrontier) 
				break
			# 	self.frontierQueue.remove(closestFrontier)
			# 	return self.chooseNewDestination()
			 else: 
				break
		else: 
			minLength = newLength
			try:
				self.frontierQueue.remove(closestFrontier)
			except ValueError:
				print "Why is " + str(closestFrontier) + " not in the list???"
				pass
			closestFrontier = newCandidate
			movedAlongFrontierCount += 1
	if movedAlongFrontierCount == 0:
		try:
			self.frontierQueue.remove(closestFrontier)
		except ValueError:
			print "Why is " + str(closestFrontier) + " not in the list???"
			pass
		print "Recursive call of doom"
		(newBool, newFrontier) = self.chooseNewDestination()
		if newBool is False:
			return True, closestFrontier
		else:
			return True, newFrontier
	return True, closestFrontier

    def destinationReached(self, goal, goalReached):
        if goalReached is False:
#             print 'Adding ' + str(goal) + ' to the naughty step'
        	self.blackList.append(goal)
	else: 
		self.location = goal

            
