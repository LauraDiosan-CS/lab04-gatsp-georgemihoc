# input:
#
# first line: number of cities (n)
# second line: distances between the first city and all the other cities (n real values)
# third line: distances between the second city and all the other cities (n real values)
# ...
# n + 1 line: distances between the n-th city and all the other cities (n real values)

# 4
# 0,1,2,4
# 1,0,3,15
# 2,3,0,6
# 4,15,6,0

#
#
# solution:
# first line: number of cities (n)
# second line: the optimal traversing path (indexes of cities, starting by 1)
# third line: the length of the optimal path (real value)
#
# 4
# 1,2,3,4
# 14

from ui import UI

class Main(object):
    def run(self):
        ui = UI()
        ui.run()

main = Main()
main.run()

