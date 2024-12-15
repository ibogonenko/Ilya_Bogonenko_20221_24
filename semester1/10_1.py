def decode_morse(morse_str):
    MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
    '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
    }
    morse_temp1 = morse_str.split('   ') # разделение сообщения на части, разделенные в сообщении пробелом
    morse_message = ''
    morse_temp2 = []
    for i in range(len(morse_temp1)): # разделение предыдущих частей на символы
        morse_temp2.append(morse_temp1[i].split())

    for i in range(len(morse_temp2)):
        for j in range(len(morse_temp2[i])):
            morse_message += MORSE_CODE[morse_temp2[i][j]] #дешифровка и запись
        morse_message += ' ' # пробел после слова
    return morse_message.strip() # strip() для того, чтобы убрать пробел в конце

def main():
    assert decode_morse('.-') == 'A'
    assert decode_morse('--...') == '7'
    assert decode_morse('...-..-') == '$'
    assert decode_morse('.') == 'E'
    assert decode_morse('..') == 'I'
    assert decode_morse('. .') == 'EE'
    assert decode_morse('.   .') == 'E E'
    assert decode_morse('...-..- ...-..- ...-..-') == '$$$'
    assert decode_morse('----- .---- ..--- ---.. ----.') == '01289'
    assert decode_morse('.-... ---...   -..-. --...') == '&: /7'
    assert decode_morse('...---...') == 'SOS'
    assert decode_morse('... --- ...') == 'SOS'
    assert decode_morse('...   ---   ...') == 'S O S'

if __name__ =="__main__":
    main()