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
def decodeMorse(morseCode):
    morse = morseCode.strip(" ").split(" ")
    human = []
    for i in range(len(morse)):
        for k,v in MORSE_CODE.items():
            if morse[i]==v:
                human.append(k)
                break
            elif morse[i]=="" and morse[i+1]=="":
                human.append(" ")
                break
    return("".join(human))

print("Secret Message: %s" % (decodeMorse(input("Morse Code: "))))

