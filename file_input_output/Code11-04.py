inFp = None
inStr = ""

inFp = open("C:/Users/xokny/OneDrive/Desktop/pythonprogramming/file_input_output/input.txt", "r")


inList = inFp.readlines()
for inStr in inList :
    print(inStr, end = "")


inFp.close()