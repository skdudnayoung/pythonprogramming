inFp, outFp = None, None
inStr = ""

# 사용자로부터 파일 경로 입력 받기
inFileName = input("소스 파일명을 입력하세요: ")
outFileName = input("타깃 파일명을 입력하세요: ")

try:
    # 파일 열기
    inFp = open(inFileName, "r")
    outFp = open(outFileName, "w")

    # 내용 복사
    inList = inFp.readlines()
    for inStr in inList:
        outFp.writelines(inStr)

    print(f"--- {inFileName} 파일이 {outFileName} 파일로 복사되었음 ---")
except FileNotFoundError:
    print("--- 파일이 존재하지 않습니다. 경로를 확인하세요. ---")
except Exception as e:
    print(f"--- 오류 발생: {e} ---")
finally:
    if inFp:
        inFp.close()
    if outFp:
        outFp.close()