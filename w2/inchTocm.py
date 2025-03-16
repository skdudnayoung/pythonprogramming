def inch_to_cm(inch):
    return inch * 2.54

inch_value = float(input("인치 값 입력: "))

cm_value = inch_to_cm(inch_value)

print(f"{inch_value}inch = {cm_value}cm")