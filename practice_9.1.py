fname = raw_input("Enter file name: ")
try:
    fhandle = open(fname)
except:
    print "This file is invalid. Check if it exists, or clarify its file path."
    quit()

collection = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        collection[word] = collection.get(word,0) + 1

print collection