items=["one","two", "threee"]

with open("testdataa.txt", "w") as fis:
    for item in items:   
        fis.write(item)
        fis.write("\n")