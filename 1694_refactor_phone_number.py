def reformatNumber(number: str) -> str:
    
    spaces_and_dashes = [" ", "-"]
    for char in spaces_and_dashes:
        number = number.replace(char, "")

    phone_number = []
    for i in range(0, len(number), 3):
        if len(number) - i != 4:
            phone_number.append(number[i:i+3])
        else:
            phone_number.extend([number[i:i+2], number[i+2:]])
            
    return "-".join(phone_number)



reformatNumber("123 4-5678")
