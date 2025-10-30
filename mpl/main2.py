'''
meetings = [1,5,4,9,0]
for i in range(len(meetings)):
    print(meetings[i], end = " ")

print("\n----------")

for i in range(len(meetings)-1, -1, -1):
    print(meetings[i], end = " ")

'''
# if you change anything in the list, it mirrors
'''
def pol():
    list = [5,6,10,12,15]

    print(list)

    print("\n---------")

    listpol = []

    for i in range(len(list)-1, -1, -1):
        
        listpol.append(list[i])
    
    print(listpol)


pol()

'''

def isPoli(input = []):
    is_poli = False
    reversed = []
    for i in range(len(input)-1, -1, -1):

        reversed.append(input[i])

    print(reversed)

    if reversed == input:
        is_poli = True

    print(is_poli)

isPoli([10,5,2])
