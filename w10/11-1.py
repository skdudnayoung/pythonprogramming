inFp = None
inStr = ""
lineNum = 1  # 행 번호 변수 추가

inFp = open("C:/Users/xokny/OneDrive/Desktop/pythonprogramming/file_input_output/input.txt", "r")

while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print("%d: %s" % (lineNum, inStr), end="")  # 행 번호와 문자열 출력
    lineNum += 1  # 행 번호 증가

inFp.close()
