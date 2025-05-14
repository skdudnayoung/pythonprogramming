inFp, outFp = None, None
inStr = ""

inFp = open("C:/Users/xokny/OneDrive/Desktop/pythonprogramming/file_input_output/input.txt", "r")
outFp = open("C:/Users/xokny/OneDrive/Desktop/pythonprogramming/file_input_output/output.txt", "w")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)
    
inFp
outFp.close()
print("--- 파일이 정상적으로 복사되었음 ---")