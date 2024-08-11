def is_poly(init_string: str) -> bool:

    # Create dictionary with letters and count them
    letter_dict = {}
    for letter in init_string:
        # if letter in letter_dict.keys():
        #     letter_dict[letter] += 1
        # else:
        #     letter_dict[letter] = 1

        letter_dict[letter] = letter_dict.get(letter, 0) + 1

    # The number of letters that occurred an odd number of times

    odd_letter = 0
    for letter in letter_dict.keys():
        if letter_dict[letter] % 2 != 0:
            odd_letter += 1
    if odd_letter > 1:
        return False
    else:
        return True

    # return odd_letter <= 1


sting_for_poly_check = input()

if is_poly(sting_for_poly_check):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
