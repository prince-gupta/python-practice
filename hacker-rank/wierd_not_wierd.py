# Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5 , print Not Weird
# If  is even and in the inclusive range of 6 to 20 , print Weird
# If  is even and greater than 20 , print Not Weird


class WierdNotWierd:
    def __init__(self, number):
        self.number = number

    def check_if_weird_or_not(self):
        if self.number % 2 != 0:
            print "Weird"
        elif self.number >= 2 and self.number <= 5:
            print "Not Weird"
        elif self.number >= 6 and self.number <= 20:
            print "Weird"
        else:
            print "Not Weird"

w = WierdNotWierd(20)
w.check_if_weird_or_not()