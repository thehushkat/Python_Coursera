'''9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.'''

fname = raw_input("Enter file name: ")
try:
    fhandle = open(fname)
except:
    print fname, "is an invalid file name. Please check your path."
    quit()

contacts = dict()
for line in fhandle:
    if line.startswith("From "):
        words = line.split()
        address = words[1]
        contacts[address] = contacts.get(address, 0) + 1

max_contact = None
max_count = None
for contact,value in contacts.items():
    if max_count is None or value > max_count:
        max_contact = contact
        max_count = value

print max_contact, max_count