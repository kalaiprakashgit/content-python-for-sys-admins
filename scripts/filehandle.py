#!/bin/python

import os

# family_file = open('member')
# for line in family_file:
#     print(line)

# family_file = open('member')
# print(family_file.read())



# family_file = open('members', 'r+')
# family_file.seek(-1, os.SEEK_END)
# family_file.write("\nSailaja\n")
# family_file.write("Kishore\n")
# family_file.write("Prakash\n")
# family_file.write("Kalai\n")


# family_file = open('member', 'a')
# family_file.writelines(['car1\n', 'car2\n'])
#
# family_file.close()

with open('member', 'a')  as family_file:
    family_file.write("CAR1\n")