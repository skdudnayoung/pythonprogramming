def kg_to_pound(kg):
    return kg * 2.20462

kg_value = float(input("kg 값 입력: "))

pound_value = kg_to_pound(kg_value)

print(f"{kg_value}kg = {pound_value}pound")