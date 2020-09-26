"""Build Tower

Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *
    Python: return a list;

Have fun!

for example, a tower of 3 floors looks like below
[
  '  *  ',
  ' *** ',
  '*****'
]

and a tower of 6 floors looks like below
[
  '     *     ',
  '    ***    ',
  '   *****   ',
  '  *******  ',
  ' ********* ',
  '***********'
]
"""


def tower_builder(n_floors):
    tower = []
    width = (n_floors - 1) * 2 + 1
    for floor in range(1, n_floors + 1):
        star = floor * 2 - 1
        space = int((width - star) / 2)
        s = ' ' * space + '*' * star + ' ' * space
        tower.append(s)
    return tower
