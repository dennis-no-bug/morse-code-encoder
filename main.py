morse_dict = {
    "a": "*- ", "b": "-*** ", "c": "-*-* ", "d": "-** ", "e": "* ", "f": "**-* ", "g": "--* ", "h": "**** ", "i": "** ",
    "j": "*--- ", "k": "-*- ", "l": "*-** ", "m": "-- ", "n": "-* ", "o": "--- ", "p": "*--* ", "q": "--*- ", "r": "*-* ", "s": "*** ",
    "t": "- ", "u": "**- ", "v": "***- ", "w": "*-- ", "x": "-**- ", "y": "-*-- ", "z": "--** ", " ": "   ",
}


def morse_code():

    while True:
        user_direction = input("Would you like to encode or decode?: ").lower()

        if user_direction == "encode":
            user_input = input("\nPlease enter a word/phrase/sentence that you would like to encode: ").lower()

            all_inputs = []
            for i in user_input:
                all_inputs.append(i)
                if i not in morse_dict:
                    raise Exception("Invalid! You are supposed to enter letter from A-Z only.")

            converted_list = []
            for x in all_inputs:
                converted_list.append(morse_dict.get(x))

            final_outputs = ""
            for code in converted_list:
                final_outputs += code

            print(f"\nHi there! Your morse codes are: {final_outputs}\n")

            proceed = input("Would you like to continue? (Yes/No): ").lower()
            if proceed == "no":
                print("\nBye bye!")
                break


morse_code()

