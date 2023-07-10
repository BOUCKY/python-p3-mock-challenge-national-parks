#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    v1 = Visitor('Adam')
    v2 = Visitor('Emiley')

    np1 = NationalPark("Yosemite")
    np2 = NationalPark(' Grand Canyon')

    t1 = Trip( v1, np1, 'last week', 'tomorrow')
    t2 = Trip( v1, np2, 'last month', 'next week')
    t3 = Trip( v1, np2, 'next month', 'two months')

    t4 = Trip( v2, np1, 'last month', 'next week')
    t5 = Trip( v2, np2, 'last week', 'tomorrow')


    ipdb.set_trace()
