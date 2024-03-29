# Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time
# and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dis = dict()
li = list()
for line in handle:
    if line.startswith('From'):
        words = line.strip()
        words = words.split()
        if len(words)>=3:
            time = words[5].split(':')
            hour = time[0]
            li.append(hour)

for hour in li:
    dis[hour] = dis.get(hour, 0)+1

li2 = list()
for key, value in dis.items():
    newtup = (key,value)
    li2.append(newtup)

li2 = sorted(li2)
for key,value in li2:
    print(key,value)