""" 
	Concentrate vs disperse shott

	A Small Program, born from one curiosity and migrating in a more evolve way.

	1. Simple shoot version

"""

def main():
	
	# 1. Variables
	squad_size = 100	
	health = 10

	print "Both opposing squads are composed of %s men" %squad_size
	print "Each man can withstand %s shoot(s)" %health

	# Create squads

	squad1 = []
	squad2 = []

	for i in xrange(squad_size):
		squad1.append(health)
		squad2.append(health)


	print "At the beginning, the first squad as a strengh of %s" %sum(squad1)
	print "At the beginning, the second squad as a strengh of %s" %sum(squad2)

	
	# As each team shoots in the same time:
	iteration = 0

	while (sum(squad1) > 0) and (sum(squad2) >0):
		
		temp_squad1 = list(squad1)
		temp_squad2 = list(squad2)

		squad1 = concentrated_shoots(temp_squad2, temp_squad1)
		squad2 = distributed_shoots(temp_squad1, temp_squad2)

		iteration +=1

	
	print "The 'battle' ended after %s rounds" %iteration

	if sum(squad1) > sum(squad2):
		print "The distributed method was optimal"

	elif sum(squad1) < sum(squad2):
		print "The Concentrated method was optimal"

	else:
		print "It end in a draw"





def distributed_shoots(shooters, targets):

	targets = list(targets)
	shoots = nb_shoots(shooters)

	for i in xrange(shoots):
		targets[i] += (-1)

	return targets

def concentrated_shoots(shooters, targets):

	targets = list(targets)
	shoots = nb_shoots(shooters)


	for i in xrange(shoots):	
		n = get_target(targets)

		targets[n] += (-1)

	return targets


# Helper functions

def get_target(targets):
	n = 0
	for target in targets:

		if target > 0:
			return n 
		else:
			n += 1 

def nb_shoots(list):
	n = 0 

	for el in list:
		if el > 0:
			n += 1
		else:
			el = 0

	print "nb of shoots: %s" %n
	return n



main()	
