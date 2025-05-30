inFp = None
inStr = ""

# 파일 열기
inFp = open("C:/Users/xokny/OneDrive/Desktop/pythonprogramming/file_input_output/input.txt", "r")

# 파일의 모든 줄을 리스트로 읽기
inList = inFp.readlines()

# 각 줄에 대해 번호와 함께 출력
for idx, inStr in enumerate(inList, start=1):
    print(f"{idx}: {inStr}", end="")

# 파일 닫기
inFp.close()
