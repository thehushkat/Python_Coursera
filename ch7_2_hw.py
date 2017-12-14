'''Write a program that prompts for a file name, then opens that file and reads through the file, 
looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those 
values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.'''

linecount = 0
xdspam = 0
fname = raw_input("Enter file name: ")
try:
    fhandle = open(fname)
except:
    print "File cannot be opened:", fname
    quit()

for line in fhandle:
    if line.startswith("X-DSPAM-Confidence:"):
        linecount = linecount + 1
        xdval = float(line[20:])
        xdspam = xdval + float(xdspam)
print "Average spam confidence:", xdspam/float(linecount)