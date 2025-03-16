import math

def circle_area(radius):
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2 * math.pi * radius

radius_value = float(input("원의 반지름 값 입력: "))

area_value = circle_area(radius_value)
circumference_value = circle_circumference(radius_value)

print(f"반지름: {radius_value} 원의 넓이: {area_value:.2f} 원의 둘레: {circumference_value:.2f}")