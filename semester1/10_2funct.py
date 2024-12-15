def decodeBits(bits):
    bits = bits.strip('0')
    one_bits = bits.split('0')
    zero_bits = bits.split('1')
    one_bits = list(filter(lambda x: x != '', one_bits))
    if '0' in bits:
        zero_bits = list(filter(lambda x: x != '', zero_bits))
    else:
        zero_bits = ('')
    if zero_bits != '':
        if len(min(one_bits, key = len)) <= len(min(zero_bits, key = len)):
            dot_len = min(one_bits, key = len)
            dash_len = '1' * len(dot_len) * 3
            word_space_len = '0' * len(dot_len) * 7
            symbol_space_len = '0' * len(dot_len) * 3
            elem_space_len = '0' * len(dot_len)
        else:
            elem_space_len = min(zero_bits, key = len)
            dash_len = '1' * len(elem_space_len) * 3
            word_space_len = '0' * len(elem_space_len) * 7
            symbol_space_len = '0' * len(elem_space_len) * 3
            dot_len = '1' * len(elem_space_len)
    else:
        dot_len = min(one_bits, key = len)
        dash_len = '1' * len(dot_len) * 3
        word_space_len = '0' * len(dot_len) * 7
        symbol_space_len = '0' * len(dot_len) * 3
        elem_space_len = '0' * len(dot_len)

    useful_bits = bits.replace(word_space_len, '   ')

    useful_bits = useful_bits.replace(symbol_space_len, ' ')

    useful_bits = useful_bits.replace(dash_len, '-')

    useful_bits = useful_bits.replace(dot_len, '.')

    useful_bits = useful_bits.replace(elem_space_len, '')

    return useful_bits
def decodeMorse(morse_code):
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
    morse_temp1 = morse_code.split('   ') # разделение сообщения на части, разделенные в сообщении пределом
    morse_message = ''
    morse_temp2 = []
    for i in range(len(morse_temp1)): # разделение предыдущих частей на символы
        morse_temp2.append(morse_temp1[i].split())
    for i in range(len(morse_temp2)):
        for j in range(len(morse_temp2[i])):
            morse_message += MORSE_CODE[morse_temp2[i][j]] #дешифровка и запись
        morse_message += ' ' # пробел после слова
    return morse_message.strip() # strip() для того, чтобы убрать пробел в конце




assert decodeMorse(decodeBits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')) == 'HEY JUDE'

assert decodeMorse(decodeBits('1')) == 'E'
assert decodeMorse(decodeBits('101')) == 'I'
assert decodeMorse(decodeBits('10001')) == 'EE'
assert decodeMorse(decodeBits('10111')) == 'A'
assert decodeMorse(decodeBits('1110111')) == 'M'

assert decodeMorse(decodeBits('111')) == 'E'
assert decodeMorse(decodeBits('1111111')) == 'E'
assert decodeMorse(decodeBits('110011')) == 'I'
assert decodeMorse(decodeBits('111000111')) == 'I'
assert decodeMorse(decodeBits('111110000011111')) == 'I'
assert decodeMorse(decodeBits('111000000000111')) == 'EE'
assert decodeMorse(decodeBits('11111100111111')) == 'M'
assert decodeMorse(decodeBits('111000111000111')) == 'S'
assert decodeMorse(decodeBits('111111000000111111000000111111000000111111000000000000000000111111000000000000000000111111111111111111000000111111000000111111111111111111000000111111111111111111000000000000000000000000000000000000000000111111000000111111111111111111000000111111111111111111000000111111111111111111000000000000000000111111000000111111000000111111111111111111000000000000000000111111111111111111000000111111000000111111000000000000000000111111')) == 'HEY JUDE'

assert decodeMorse(decodeBits('01110')) == 'E'
assert decodeMorse(decodeBits('000000011100000')) == 'E'

assert decodeMorse(decodeBits('00011100010101010001000000011101110101110001010111000101000111010111010001110101110000000111010101000101110100011101110111000101110111000111010000000101011101000111011101110001110101011100000001011101110111000101011100011101110001011101110100010101000000011101110111000101010111000100010111010000000111000101010100010000000101110101000101110001110111010100011101011101110000000111010100011101110111000111011101000101110101110101110')) == 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'
assert decodeMorse(decodeBits('11111111111111100000000000000011111000001111100000111110000011111000000000000000111110000000000000000000000000000000000011111111111111100000111111111111111000001111100000111111111111111000000000000000111110000011111000001111111111111110000000000000001111100000111110000000000000001111111111111110000011111000001111111111111110000011111000000000000000111111111111111000001111100000111111111111111000000000000000000000000000000000001111111111111110000011111000001111100000111110000000000000001111100000111111111111111000001111100000000000000011111111111111100000111111111111111000001111111111111110000000000000001111100000111111111111111000001111111111111110000000000000001111111111111110000011111000000000000000000000000000000000001111100000111110000011111111111111100000111110000000000000001111111111111110000011111111111111100000111111111111111000000000000000111111111111111000001111100000111110000011111111111111100000000000000000000000000000000000111110000011111111111111100000111111111111111000001111111111111110000000000000001111100000111110000011111111111111100000000000000011111111111111100000111111111111111000000000000000111110000011111111111111100000111111111111111000001111100000000000000011111000001111100000111110000000000000000000000000000000000011111111111111100000111111111111111000001111111111111110000000000000001111100000111110000011111000001111111111111110000000000000001111100000000000000011111000001111111111111110000011111000000000000000000000000000000000001111111111111110000000000000001111100000111110000011111000001111100000000000000011111000000000000000000000000000000000001111100000111111111111111000001111100000111110000000000000001111100000111111111111111000000000000000111111111111111000001111111111111110000011111000001111100000000000000011111111111111100000111110000011111111111111100000111111111111111000000000000000000000000000000000001111111111111110000011111000001111100000000000000011111111111111100000111111111111111000001111111111111110000000000000001111111111111110000011111111111111100000111110000000000000001111100000111111111111111000001111100000111111111111111000001111100000111111111111111')) == 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'

print("Passed")