import re
handles = open('01-Python/python-for-everybody-specialization/course-03-python-to-access-web-data/module-02-regular-expressions/exercises/sample-data.txt', 'r')
sum = 0
for line in handles:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) > 0:
        for number in stuff:
            sum = sum + int(number)
print(sum)