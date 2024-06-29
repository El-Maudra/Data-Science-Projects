# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', 
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', " ": "   "
}
# function to translate text to morse
def translate_to_morse(text):
    """Translate text to Morse code."""
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        elif char == ' ':
            morse_code += '  '  # Separate words with double spaces
        else:
            morse_code += ''  # Ignore characters not in the Morse code dictionary
    return morse_code.strip()

# Example usage
user_choice = input("Enter English text to be translated: ")

translated_text = translate_to_morse(user_choice)
print("Morse Code:", translated_text)

