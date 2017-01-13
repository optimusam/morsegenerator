MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }
def encodeMorse(simpletext):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    text = simpletext.strip(" ").upper()
    morse = []
    for i in range(len(text)):
        for k,v in MORSE_CODE.items():
            if text[i]==k:
                morse.append(v)
                morse.append(" ")
                break
            elif text[i]==" ":
                morse.append("   ")
                break
    return("".join(morse))

print("Morse Code: %s" % (encodeMorse(input("Text: "))))
