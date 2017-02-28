import numpy as np
#import matplotlib.pylab as plt
import random
'''
f = open("random_numbers.txt","w+")
for i in range(5):
	f.write(str(i+1)+"\t:\t"+str(random.randint(1,8))+"\n")
f.close
'''
inter_arrival_time = [0,8,6,1,8,3,8,7,2,3,1,1,5,6,3,8,1,2,4,5]
service_time = [4,1,4,3,2,4,5,4,5,3,3,5,4,1,5,4,3,3,2,3]

arrival_time = np.cumsum(inter_arrival_time)

waiting_time = []
idle_time = []
service_begin = []
service_end = []
time_spent = []

waiting_time[:20] = [0] * 20
idle_time[:20] = [0] * 20
service_begin[:20] = [0] * 20
service_end[:20] = [0] * 20
time_spent[:20] = [0] * 20


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


print idle_time
avg_wait = sum(waiting_time)/20.0

print "Customer\tInter Arrival Time\tArrival Time\tService Time\tService Begins\tService Ends\tWait Time"
for i in range(20):
	print str(i+1)+"\t"+str(inter_arrival_time[i])+"\t"+str(arrival_time[i])+"\t"+str(service_time[i])+"\t"+str(service_begin[i])+"\t"+str(service_end[i])+"\t"+str(waiting_time[i])

print 'Average waiting time : '+ str(avg_wait)
print 'Total waiting time : ' + str(sum(waiting_time))
print 'Total service time : ' + str(sum(service_time))
print 'Total time spent : ' + str(sum(time_spent))
print 'Total idle time : ' + str(sum(idle_time))



#print inter_arrival_time
#print service_time