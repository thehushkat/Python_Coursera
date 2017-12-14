#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = raw_input('Enter file name: ')
try:
    fhandle = open(fname)
except:
    print fname, "is not a valid file. Please check file path or if file exists."
    quit()

hours = dict()
for line in fhandle:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        t = time.split(":")
        hour = t[0]
        hours[hour] = hours.get(hour, 0) + 1

tmp = list()
for k,v in hours.items():
    tmp.append((k,v))
    tmp.sort()

for k,v in tmp:
    print k,v