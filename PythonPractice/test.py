# from __future__ import division
# for r in range(16):
#     print(' '*int(8-(r%4*2+1*int(r/4)+1+int(r/4))/2)+'* '*(r%4*2+1*int(r/4)+1+int(r/4)))
#     print((' '*13+'* *\n')*3)

from __future__ import division

for r in range(16):
    print(' ' * int(8 - (r % 4 * 2 + 1 * int(r / 4) + 1 + int(r / 4)) / 2) + '* ' * (
            r % 4 * 2 + 1 * int(r / 4) + 1 + int(r / 4)))

    print((' ' * 13 + '* *\n') * 3)