f = open("My Clippings.txt","r")   #写书签的文件地址  write your own clippings txt file
lines = f.readlines()
l = len(lines)
i = 0

shelf = []

while(i<l):
    d ={}
    d["name"] = lines[i]
    d["time"] = lines[i+1][-24:]
    i = i + 3
    sen = []
    while(i<l and lines[i] != "==========\n"):
        sen.append(lines[i])
        i = i + 1
    if i ==l:
        sen = sen.append(lines[l-1])
    d["sentence"] = sen
    shelf.append(d)
    i = i + 1


names = []

shelf2 = {}
for book in shelf:
    t = False
    for name in names:
        if name == book["name"]:
            t = True
    if t == False:
        names.append(book["name"])
        timeNword = []
        timeNword.append(book["time"])
        timeNword.append(book["sentence"])
        shelf2[book["name"]] = [timeNword]
    else:
        timeNword = []
        timeNword.append(book["time"])
        timeNword.append(book["sentence"])
        a = shelf2[book["name"]]
        a.append(timeNword)
        shelf2[book["name"]] = a



for name in names:
    s1 = name.find("(")
    s2 = name.find("（")
    if s1>0 and s2>0:
        s3 = min(s1,s2)
    elif (s1*s2)<0:
        s3 = max(abs(s1),abs(s2))
    else:
        s3 = -1
    name1 = name[:s3]
    #print(name1,s1,s2,s3)
    s = "/Users/apple/Desktop/clip/" + name1 + ".txt"   #写要存放txt的文件夹名 write your clip floder name
    file = open(s,"a")
    timeNwords = shelf2[name]
    name1 = name1 + "\n"
    file.write(name1)
    file.write("\n")
    for timeNword in timeNwords:
        time,words = timeNword
        for word in words:
            file.write(word)
        file.write("\n")

