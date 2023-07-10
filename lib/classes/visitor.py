class Visitor:

    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        # underscore with name becasue if it was self.name, it would be an infinite loop of getting the name from the __init__.
        # also to let other programmers know it's a private attribute.
        return self._name

    def set_name(self, name):
        # Prevents the name from being changed
        if hasattr(self, '_name'):
            raise Exception("Cannot change the visitor's name.")
        else:
            # If the type of name is a string that is between 1 and 15 characters: set self._name to name and return it.
            if type(name) == str and len(name) >=1 and len(name) <= 15:
                self._name = name
                return self._name
            else: 
                raise Exception("Name must be a string between 1 and 15 characters long.")

    name = property(get_name, set_name)


    # returns a list of all a visitor's trips
    def trips(self, new_trip=None):
        from classes.trip import Trip
        # create an empty list for the visitor's trip(s) to go into.
        trip_list = []
        # for each trip in the list of trips:
        for trip in Trip.all:
            # if the visitor from a trip is self: add that trip to the list
            if trip.visitor == self:
                trip_list.append(trip)
        return trip_list
    

    # returns a list of all the parks a vistor has visited
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        # create an empty list for the visitor's park(s) to go into.
        park_list = []
        # for each trip in the visitor's list of trips: append the park name to the park list.
        for trip in self.trips():
            park_list.append(trip.national_park)
        return park_list 

