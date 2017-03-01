import numpy as np
import random
iterations=input("Enter the number of trials : ")
print '\n'

print 'Iteration Number \tAverage waiting time '
print '__________________________________________'

for j in range(iterations):
	inter_arrival_time=[]
	service_time=[]

	for i in range(20):
		inter_arrival_time.append(random.randint(1,8))
		service_time.append(random.randint(1,6))
	inter_arrival_time[0]=0

	#inter_arrival_time = [0,8,6,1,8,3,8,7,2,3,1,1,5,6,3,8,1,2,4,5]
	#service_time = [4,1,4,3,2,4,5,4,5,3,3,5,4,1,5,4,3,3,2,3]

	arrival_time = np.cumsum(inter_arrival_time)		#find the cumulative sum

	waiting_time = []
	idle_time = []
	service_begin = []
	service_end = []
	time_spent = []

	# initializing all arrays to 0

	waiting_time[:20] = [0] * 20
	idle_time[:20] = [0] * 20
	service_begin[:20] = [0] * 20
	service_end[:20] = [0] * 20
	time_spent[:20] = [0] * 20

	# simulation for the first customer

	service_begin[0] = inter_arrival_time[0]
	service_end[0] = service_begin[0] + service_time[0]
	time_spent[0] = service_end[0] - arrival_time[0]
	idle_time[0] = 0
	waiting_time[0] = service_begin[0] - arrival_time[0]


	for i in range(1,20):
		a=service_end[i-1]
		b=arrival_time[i]
		service_begin[i]=(max(a,b))
		service_end[i] = service_begin[i] + service_time[i]
		waiting_time[i] = service_begin[i] - arrival_time[i]
		time_spent[i] = service_end[i] - arrival_time[i]
		idle_time[i] = arrival_time[i] - service_end[i-1]

	idle_time = np.asarray(idle_time)		#covert to array
	idle_time[idle_time < 0] = 0			#set negative values to 0

	'''
	print "C\tIAT\tAT\tST\tSB\tSE\tWT\tIT"
	for i in range(20):
		print str(i+1)+"\t"+str(inter_arrival_time[i])+"\t"+str(arrival_time[i])+"\t"+str(service_time[i])+"\t"+str(service_begin[i])+"\t"+str(service_end[i])+"\t"+str(waiting_time[i])+"\t"+str(idle_time[i])

	print "\t"+str(sum(inter_arrival_time))+"\t"+str(sum(arrival_time))+"\t"+str(sum(service_time))+"\t"+str(sum(service_begin))+"\t"+str(sum(service_end))+"\t"+str(sum(waiting_time))+"\t"+str(sum(idle_time))
	'''

	print  str(j)+"\t\t\t"+str(sum(waiting_time)/20.0)
	#print 'Total waiting time :\t' + str(sum(waiting_time))
	#print 'Average service time :\t' + str(sum(service_time)/20.0)
	#print 'Average time spent :\t' + str(sum(time_spent)/20.0)
	#print 'Total idle time :\t' + str(sum(idle_time))



#print inter_arrival_time
#print service_time