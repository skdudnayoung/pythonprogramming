outFp = None
outStr = ""
fName = ""

# 저장할 파일명 입력
fName = input("저장할 파일명을 입력하세요: ")

# 파일 열기 (쓰기 모드)
outFp = open(fName, "w")

# 사용자로부터 입력을 받아 파일에 쓰기
while True:
    outStr = input("내용 입력 : ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

# 파일 닫기
outFp.close()
print("--- 정상적으로 파일에 씀 ---")
