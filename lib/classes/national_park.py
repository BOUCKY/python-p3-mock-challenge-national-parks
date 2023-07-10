class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []

    def get_name(self):
        # underscore with name becasue if it was self.name, it would be an infinite loop of getting the name from the __init__.
        # also to let other programmers know it's a private attribute.
        return self._name

    def set_name(self, name):
        # we want to check if the attribute(self aka the park) has a certain property(the name of the park)
        # if self already has a name, raise exception, if it does not, set the name.
        # hasattr() returns boolean. If true, raise exception. If false, set the name.
        if hasattr(self, "_name"):
            raise Exception("Cannot change the name of the park.")
        else: 
            # If the type of name is a string: set self._name to name and return it.
            if type(name) == str:
                self._name = name
                return self._name
            else: raise Exception("Name of park must be a string.")

    name = property(get_name, set_name)

    # returns a list of all trips taken at this park
    def trips(self, new_trip=None):
        from classes.trip import Trip
        # create an empty list for the visitor's trip(s) to go into.
        trip_list = []
        # for each trip in the list of trips:
        for trip in Trip.all:
            # if the visitor from a trip is self: add that trip to the list
            if trip.national_park == self:
                trip_list.append(trip)
        return trip_list


    # returns a unique list of visitors the park has recieved
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        # t.visitor(visitor from the trip) is what will end up in the set
        # for t is a variable we're declaring to represent one of the trips in self.trips()

        # we're using a set because it will filter out duplicates in case one visitor has visited the park more than once. That visitor will only show up once
        visitor_set = {t.visitor for t in self.trips()}
        # turn the set into a list.
        return list(visitor_set)
    

    # returns the number of total visits at a park
    def total_visits(self):
        # return the length of the list for specified park
        return len(self.trips())
    
    
    # returns the best visitor(the visitor who has visited the park the most) at a park
    def best_visitor(self):
        # create dictionary with a key of visitor and value of how many times they've visited the park
        memory = {}
        # for each trip at this park: If the visitor's name is already there, add 1 to their count. If not, make their count 1.
        for t in self.trips():
            if memory[t.visitor.name]:
                memory[t.visitor.name]
            else:
                memory[t.visitor.name] = 1
        # set the winner's visits to 0
        winner = {'total' : 0}
        # for each visitor and their number of visits in memory, if the visitor's number of visits is greater than the winner, they are now the winner. Otherwise, go to the next visitor and compare.
        for name, amount in memory.items():
            if amount > winner['total']:
                winner['name'] = name
                winner['total'] = amount
        return winner['name']
