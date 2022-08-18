read_data=open("TestData.txt", "r")
contentdata=read_data.read()
print(contentdata)

for line in contentdata:
    print(line)