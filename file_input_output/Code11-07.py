outFp = None
outStr = ""

outFp = open("C:/Users/xokny/OneDrive/Desktop/pythonprogramming/file_input_output/output.txt", "w")

while True:
    outStr = input("내용 입력 : ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break
    
outFp.close()
print("--- 정상적으로 파일에 씀 ---")