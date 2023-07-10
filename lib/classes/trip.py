class Trip:
    # set an empty list to add all the trips to
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        # append the trip to the list on initialization
        Trip.all.append(self)

    def get_visitor(self):
        return self._visitor

    def set_visitor(self, new_visitor):
        from classes.visitor import Visitor
        # if the new visitor is the same type as Visitor: set the new visitor
        if isinstance(new_visitor, Visitor):
            self._visitor = new_visitor
        else: 
            raise Exception("Must include Visitor instance")

    visitor = property(get_visitor, set_visitor)


    def get_national_park(self):
        return self._national_park

    def set_national_park(self, new_park):
        from classes.national_park import NationalPark
        # if the new park is the same type as NationalPark: set the new park
        if isinstance(new_park, NationalPark):
            self._national_park = new_park
        else: 
            raise Exception("Must include National Park instance")

    national_park = property(get_national_park, set_national_park)