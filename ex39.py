states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def divide():
    print '-' * 10

divide()
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']
divide()
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

divide()
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

divide()
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

divide()
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)
divide()
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

divide()
state = states.get('Texas', None)
if not state:
    print "Sorry, no Texas."

city = cities.get('TX','Does Not Exist')
print "The city for the state 'TX' is: %s" % city




