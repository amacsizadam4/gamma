
'''
meetings = [3, 4, 6, 1]
print(meetings)
meetings.append(10)
print(meetings)
#------------------
total = 0
# for i in range(len(meetings)):
  #  print(i, meetings[i], total)
  #  total +=meetings[i]

total = sum(meetings)

print(total)

print("avg number of people at a metting: " + str(round(total/len(meetings))))
'''

import random

meeting = []
for i in range(4):
    rand = random.randint(1,50)
    meeting.append(rand)

print(meeting)