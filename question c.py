import array
question = raw_input('Quesion:')
# i = increment
# t = times +1
# a = append $ 
# n = navigate
# nw = number of words
# word  =  word $
# f = find $
# x
x = 0
a = []
t = 0
string = []
for i in range (0,len(question)):
    if question[i] == ' ':
        a.append(i)
        t+=1
nw = t+1
string.append(question[0:a[0]])  #first
for x in range(1,len(a)):
    if a[x]:
        string.append(question[a[x-1]+1:a[x]]) #mid
        if x + 1 == len(a):     
            string.append(question[a[x]:len(question)]) #last
print string





        




