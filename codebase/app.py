import os
#print(os.environ['SECRET'])
f = open("/run/secrets/TOKEN", "r")
print(f.read())