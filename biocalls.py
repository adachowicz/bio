'''
Biology module helper code
'''


def alienGenetics1(case=1):
	import matplotlib.pyplot as plt
	print 'Working on getting your data...'
	print ''
	sillvar = 5

	from numpy import random as ra
	import time
	gensize = 400
	featuredict = {}
	featuredict['fingerdom'] = 0
	featuredict['fingerdiff'] = 0
	featuredict['fingersame'] = 0
	featuredict['visdom'] = 0
	featuredict['visres'] = 0
	featuredict['neckdom'] = 0
	featuredict['neckres'] = 0
	# [father finger, mom finger, father vision, mom vision, father neck, mom neck]
	if case == 1:
		fathervec = [ [1,0],[1,0],[1,1] ]
		momvec = [ [0,0],[1,0],[0,0] ]
	elif case == 2:
		fathervec = [ [1,1],[0,0],[1,0] ]
		momvec = [ [0,0],[1,0],[1,0] ]
	elif case == 3:
		fathervec = [ [0,0],[0,0],[0,0] ]
		momvec = [ [0,0],[0,0],[1,0] ]
	else:
		print 'Hm, we do not have the right data for that. Just enter 1, 2, or 3!'
		return
	for child in range(gensize):
		c1 = ra.choice(fathervec[0])
		c2 = ra.choice(momvec[0])
		if c1 == 1 and c2 == 1:
			featuredict['fingerdom'] += 1
		elif c1 + c2 == 1:
			featuredict['fingerdiff'] += 1
		else:
			featuredict['fingersame'] += 1
		c3 = ra.choice(fathervec[1])
		c4 = ra.choice(momvec[1])
		if c3 + c4 >= 1:
			featuredict['visdom'] += 1
		else:
			featuredict['visres'] += 1
		c5 = ra.choice(fathervec[2])
		c6 = ra.choice(momvec[2])
		if c5 + c6 >= 1:
			featuredict['neckdom'] += 1
		else:
			featuredict['neckres'] += 1
		cvec = [ [c1,c2],[c3,c4],[c5,c6] ]
		# print cvec
	# time.sleep(5)

	print 'Results are in for family %d!' %case
	print ''
	print 'There were a total of %d children in the brood.' %gensize
	print ''
	print 'Of these children, %d had different sized fingers, %d had equally sized fingers, and %d had partially equal sized fingers.'\
	 %(featuredict['fingerdom'], featuredict['fingersame'],featuredict['fingerdiff'])
	print ''
	print '%d had Infrared Vision ability, and %d had UV Vision ability.'\
	 %(featuredict['visdom'],featuredict['visres'])
	print ''
	print '%d had long necks, while %d had shorter necks.'%(featuredict['neckdom'],featuredict['neckres'])
	print ''
	print 'Remember, your goal is to identify the dominant, recessive, and partially '
	print 'dominant traits, as well as determine the allele pairs of the '
	print 'parents for each family.'

	return


def alienGenetics2(f1,m1,ad,nt):
	from numpy import random as ra
	import matplotlib.pyplot as plt

	sample_size = 200
	
	def get_parent_vecs(f1):
		f1vec = []
		if f1[0] == 'F':
			f1vec.append([1,1])
		elif f1[0] == 'Ff':
			f1vec.append([1,0])
		else:
			f1vec.append([0,0])
		# if m1[0] == 'F':
		# 	m1vec.append([1,1])
		# elif m1[0] == 'Ff':
		# 	m1vec.append([1,0])
		# else:
		# 	m1vec.append([0,0])
		if f1[1] == 'V':
			t = ra.choice([0,1])
			f1vec.append([1,t])
		else:
			f1vec.append([0,0])
		# if m1[1] == 'V':
		# 	t = ra.choice([0,1])
		# 	m1vec.append([1,t])
		# else:
		# 	m1vec.append([0,0])
		if f1[2] == 'N':
			t = ra.choice([0,1])
			f1vec.append([1,t])
		else:
			f1vec.append([0,0])
		# if m1[2] == 'N':
		# 	t = ra.choice([0,1])
		# 	m1vec.append([1,t])
		# else:
		# 	m1vec.append([0,0])
		return f1vec #, m1vec

	vector_dict = {}
	for i in range(sample_size):
		vector_dict[i] = {}
		# f1v, m1v = get_parent_vecs(f1,m1)
		vector_dict[i]['f1vec'] = get_parent_vecs(f1)
		vector_dict[i]['m1vec'] = get_parent_vecs(m1)
		vector_dict[i]['avec'] = get_parent_vecs(ad)
		# print vector_dict[i]
		# print m1v
		# print ''
	# now actually do MC:
	fingerdoms = []
	fingerdiffs = []
	fingersames = []
	visdoms = []
	visress = []
	neckdoms = []
	neckress = []
	for i in range(sample_size):
		''' Get first generation statistics '''
		gensize = 400
		featuredict = {}
		featuredict['fingerdom'] = 0
		featuredict['fingerdiff'] = 0
		featuredict['fingersame'] = 0
		featuredict['visdom'] = 0
		featuredict['visres'] = 0
		featuredict['neckdom'] = 0
		featuredict['neckres'] = 0
		# [father finger, mom finger, father vision, mom vision, father neck, mom neck]
		fathervec = vector_dict[i]['f1vec']
		momvec = vector_dict[i]['m1vec']
		avec = vector_dict[i]['avec']
		cvecs = []
		for child in range(gensize):
			c1 = ra.choice(fathervec[0])
			c2 = ra.choice(momvec[0])
			if c1 == 1 and c2 == 1:
				featuredict['fingerdom'] += 1
			elif c1 + c2 == 1:
				featuredict['fingerdiff'] += 1
			else:
				featuredict['fingersame'] += 1
			c3 = ra.choice(fathervec[1])
			c4 = ra.choice(momvec[1])
			if c3 + c4 >= 1:
				featuredict['visdom'] += 1
			else:
				featuredict['visres'] += 1
			c5 = ra.choice(fathervec[2])
			c6 = ra.choice(momvec[2])
			if c5 + c6 >= 1:
				featuredict['neckdom'] += 1
			else:
				featuredict['neckres'] += 1
			cvec = [ [c1,c2],[c3,c4],[c5,c6] ]
			cvecs.append(cvec)

		bad = False
		c = 0
		while bad == False:
			newgen_choice = ra.choice(range(gensize))
			if nt == 'F':
				if sum(cvecs[newgen_choice][0]) == 2:
					bad = True
			elif nt == 'f':
				if sum(cvecs[newgen_choice][0]) == 0:
					bad = True
			elif nt == 'Ff':
				if sum(cvecs[newgen_choice][0]) == 1:
					bad = True
			elif nt == 'V':
				if sum(cvecs[newgen_choice][1]) >= 1:
					bad = True
			elif nt == 'v':
				if sum(cvecs[newgen_choice][1]) == 0:
					bad = True
			elif nt == 'N':
				if sum(cvecs[newgen_choice][2]) >= 1:
					bad = True
			elif nt == 'n':
				if sum(cvecs[newgen_choice][2]) == 0:
					bad = True
			newgen_child_vec = cvecs[newgen_choice] # pick the new generation mating pair
			c += 1
			if c > gensize:
				print 'Cannot find a child to match. Try again with a different trait or strategy.'
				return
		
		''' Get second generation statistics '''
		featuredict = {}
		featuredict['fingerdom'] = 0
		featuredict['fingerdiff'] = 0
		featuredict['fingersame'] = 0
		featuredict['visdom'] = 0
		featuredict['visres'] = 0
		featuredict['neckdom'] = 0
		featuredict['neckres'] = 0
		for child in range(gensize):
			c1 = ra.choice(newgen_child_vec[0])
			c2 = ra.choice(avec[0])
			if c1 == 1 and c2 == 1:
				featuredict['fingerdom'] += 1
			elif c1 + c2 == 1:
				featuredict['fingerdiff'] += 1
			else:
				featuredict['fingersame'] += 1
			c3 = ra.choice(newgen_child_vec[1])
			c4 = ra.choice(avec[1])
			if c3 + c4 >= 1:
				featuredict['visdom'] += 1
			else:
				featuredict['visres'] += 1
			c5 = ra.choice(newgen_child_vec[2])
			c6 = ra.choice(avec[2])
			if c5 + c6 >= 1:
				featuredict['neckdom'] += 1
			else:
				featuredict['neckres'] += 1
			cvec = [ [c1,c2],[c3,c4],[c5,c6] ]
			cvecs.append(cvec)
		fingerdoms.append(float(featuredict['fingerdom'])/float(gensize))
		fingerdiffs.append(float(featuredict['fingerdiff'])/float(gensize))
		fingersames.append(float(featuredict['fingersame'])/float(gensize))
		visdoms.append(float(featuredict['visdom'])/float(gensize))
		visress.append(float(featuredict['visres'])/float(gensize))
		neckdoms.append(float(featuredict['neckdom'])/float(gensize))
		neckress.append(float(featuredict['neckres'])/float(gensize))

	fig = plt.figure(figsize = (12,8))
	plt.hist(fingerdoms,alpha = 0.3,normed = True,label = 'Diff. Lengths')
	plt.hist(fingerdiffs,alpha = 0.3,normed = True,label = 'Partially Eq. Lengths')
	plt.hist(fingersames,alpha = 0.3,normed = True,label = 'Equal Lengths')
	plt.xlim([0,1.1])
	plt.xlabel('<-- Minimize (Percent of 2nd Generation Displaying Given Trait) Maximize -->')
	plt.legend()
	plt.show()

	fig = plt.figure(figsize = (12,8))
	plt.hist(visress,alpha = 0.3,normed = True,label = 'UV Visuals')
	plt.hist(visdoms,alpha = 0.3,normed = True,label = 'Infrared Visuals')
	plt.xlim([0,1.1])
	plt.xlabel('<-- Minimize (Percent of 2nd Generation Displaying Given Trait) Maximize -->')
	plt.legend()
	plt.show()

	fig = plt.figure(figsize = (12,8))
	plt.hist(neckdoms,alpha = 0.3,normed = True,label = 'Long Neck')
	plt.hist(neckress,alpha = 0.3,normed = True,label = 'Short Neck')
	plt.xlim([0,1.1])
	plt.xlabel('<-- Minimize (Percent of 2nd Generation Displaying Given Trait) Maximize -->')
	plt.legend()
	plt.show()





	# print f1vec
	# print m1vec


	return