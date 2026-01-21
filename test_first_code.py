
first_file=open('hello world.txt','w')
first='hello world !'
first_file.write(first)
first_file.close()
with open('hello world.txt','r') as first_read :
    print(first_read.read())
