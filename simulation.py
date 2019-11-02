import random
import numpy as np
import queue
import copy
import matplotlib.pyplot as plt
import statistics
queuesTimes={1:[],2:[],3:[],4:[],5:[],6:[]}
groups={1:[],2:[],3:[]} #leaving time for each group

avgByIat=[]
ST_rate=50
noisyAvg=[]

noOfJobs=1500
for IAT_rate in range(10,500):
    avgByIat=[]


    for j in range(1,200):
        respTime=[]



        queuesTimes={1:[],2:[],3:[],4:[],5:[],6:[]}
        groups={1:[],2:[],3:[]} #leaving time for each group
        respTime=[]
        IAT=[]
        for i in range(noOfJobs):
            temp = np.random.exponential(1/IAT_rate)
            if i==0:
                IAT.append(0)
            else:
                IAT.append(temp)

        AT=[]
        for i in range(noOfJobs):
            try:
                if i == 0:
                    AT.append(IAT[0])
                else:
                    AT.append(AT[i-1] + IAT[i])

            except:
                break
        #job1
        t=random.randint(1,3)
        groups[t].append(min(np.random.exponential(1/ST_rate),np.random.exponential(1/ST_rate)))
        respTime=[min(np.random.exponential(1/ST_rate),np.random.exponential(1/ST_rate))]


        for jobs in range (1,500):
            #is any group empty
            con=0

            for t in range (1,4):
                if(len(groups[t])==0 or groups[t][-1]<= AT[jobs]):
                    con=1
                    groups[t].append(min(np.random.exponential(1/ST_rate),np.random.exponential(1/ST_rate))+AT[jobs])
                    respTime.append(min(np.random.exponential(1/ST_rate),np.random.exponential(1/ST_rate)))
                    break
            if con==0:
                #no group empty
                t=random.randint(1,3)
                WT=groups[t][-1]-AT[jobs]
                respTime.append(min(np.random.exponential(1/ST_rate),np.random.exponential(1/ST_rate))+WT)
                groups[t].append(min(np.random.exponential(1/ST_rate),np.random.exponential(1/ST_rate))+WT+AT[jobs])
        avgByIat.append(statistics.mean(respTime))
    noisyAvg.append(statistics.mean(avgByIat))



plt.plot([i for i in range(10, 500)], noisyAvg)
plt.show()


