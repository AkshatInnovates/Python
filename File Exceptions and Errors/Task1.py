try:
    file1 = open('sample.txt','r')
    reading = file1.readline()
    print("Reading file content:")
    print("Line 1: ",reading)
    reading2 = file1.readline()
    print("Line 2: ",reading2)
    file1.close()
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")