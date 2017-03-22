import numpy as np
import time
import random
n = input("Enter the value of n : ")
customers=input("Enter the number of customers : ")
time_duration,time_increment = (int(x) for x in raw_input("Enter the time duration & increment step(separate by space) : ").split(" "))
print '\n\n'

print 'S No.'+'\t'+'Iterations'+'\t'+'Duration'+'\t'+'AAWT'

for k in range(n):
	average_awt=0
	iterations = 0

	if(k>0):                  #_____ start to increment time after the first iteration _____#
		time_duration += time_increment

	t_end = time.time() + time_duration
	while time.time() < t_end:         #_______ run the loop for specified seconds ____#
		iterations += 1                #_______ count the iterations done in that time _____#
		inter_arrival_time=[]
		service_time=[]


		#_____ to generate the random numbers__________#
		for i in range(customers):
			inter_arrival_time.append(random.randint(1,8))
			service_time.append(random.randint(1,6))

		#print inter_arrival_time,service_time


		arrival_time = np.cumsum(inter_arrival_time)		#find the cumulative sum

		waiting_time = []
		idle_time = []
		service_begin = []
		service_end = []
		time_spent = []

		# initializing all arrays to 0

		waiting_time[:customers] = [0] * customers
		idle_time[:customers] = [0] * customers
		service_begin[:customers] = [0] * customers
		service_end[:customers] = [0] * customers
		time_spent[:customers] = [0] * customers

		# simulation for the first customer

		service_begin[0] = inter_arrival_time[0]
		service_end[0] = service_begin[0] + service_time[0]
		time_spent[0] = service_end[0] - arrival_time[0]
		idle_time[0] = 0
		waiting_time[0] = service_begin[0] - arrival_time[0]


		for i in range(1,customers):
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
		avg_wait_time=sum(waiting_time)/float(customers)
		average_awt = average_awt + avg_wait_time
		#print  str(j)+"\t\t\t"+str(avg_wait_time)
		#print 'Total waiting time :\t' + str(sum(waiting_time))
		#print 'Average service time :\t' + str(sum(service_time)/20.0)
		#print 'Average time spent :\t' + str(sum(time_spent)/20.0)
		#print 'Total idle time :\t' + str(sum(idle_time))


	print str(k)+'\t\t'+str(iterations)+'\t\t'+str(time_duration)+'\t\t'+"{0:.2f}".format(average_awt/iterations)
	#print inter_arrival_time
	#print service_time
