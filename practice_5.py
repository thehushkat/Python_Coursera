'''Exercise 5.1 
Write a program which repeatedly reads numbers until the user enters “done”. 
Once “done” is entered, print out the total, count, and average of the numbers. 
If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.33333333333'''

count = 0
total = 0
while True:
    number = raw_input("Enter a number:")
    if number == "done":
        break
    try:
        if number is not "done":
            n = int(number)
    except:
        print "Invalid input"
        continue
    if n is int(number):
        count = count + 1
        total = n + float(total)
print "Count: ", count, "Total value: ", total, "Average: ", total/count