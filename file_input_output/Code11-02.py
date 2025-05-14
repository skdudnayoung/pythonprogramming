inFp = None
inStr = ""

inFp = open("C:/Users/xokny/OneDrive/Desktop/pythonprogramming/file_input_output/input.txt", "r")

while True:
    inStr = inFp.readline()
    if inStr == "":
        break;
    print(inStr, end = "")

inFp.close()