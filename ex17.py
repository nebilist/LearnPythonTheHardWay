from os.path import exists

script, from_file, to_file = sys.argv

output = open(to_file, 'w').write(open(from_file).read())

