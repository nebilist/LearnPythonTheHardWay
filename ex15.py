from sys import argv

script, filename = argv

#"txt" holds the txtfile
txt = open(filename)

#prints the filename
print "Here's your file %r:" % filename
#reads the file's contents
print txt.read()

#prompts for a txt file
print "Type the filename again:"
file_again = raw_input("> ")

#"txt_again" holds another txtfile
txt_again = open(file_again)

#prints the contents
print txt_again.read()
