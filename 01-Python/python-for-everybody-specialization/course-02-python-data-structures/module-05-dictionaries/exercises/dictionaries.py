name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
lst = list()
counting = dict()
#storing the 2nd word in lst list.
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    lst.append(words[1])
    
#counting the occurances of sender using dict()    
for name in lst:
    counting[name] = counting.get(name,0) + 1
    
#finding the most prolific committer.
maxCount = None
maxName = None
for key,value in counting.items():
    if maxCount is None or value > maxCount :
        maxName = key
        maxCount = value
        
print(maxName,maxCount)