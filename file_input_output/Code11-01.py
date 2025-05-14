inFp = None
inStr = ""

inFp = open("C:/Users/xokny/OneDrive/Desktop/pythonprogramming/file_input_output/input.txt", "r")

inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inFp.close()