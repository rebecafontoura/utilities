import string
import re

destino = open("prefixes_objects.txt", "a")

f = open("combined_objects.csv", "r")

prefixes = []

for line in f:
    n = re.split('(\d+)',line)
    k = n[0]
    if k not in prefixes:
        prefixes.append(k)
        destino.write(k + "\n")

