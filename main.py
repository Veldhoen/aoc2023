import aocd
import os


class AOC_solver():
    def __init__(self, day_number):
        self.datapath = os.path.join('data',f"{day_number}.input")
        if not os.path.exists(self.datapath):
            self.data = aocd.get_data(day=day)
            with open(self.datapath, 'w') as f:
                f.write(self.data)


