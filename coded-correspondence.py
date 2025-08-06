message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"


shift = 10

letters = [['a',1],['b',2],['c',3],['d',4],['e',5],['f',6],['g',7],['h',8],['i',9],['j',10],['k',11],['l',12],['m',13],['n',14],['o',15],['p',16],['q',17],['r',18],['s',19],['t',20],['u',21],['v',22],['w',23],['x',24],['y',25],['z',26]]
shift_letters = []

for pair in letters:
    letter = pair[0]
    number = pair[1] + shift
    if number > 26:
        number = number - 26
    shift_letters.append([letter, number])
        
#print(shift_letters)


def get_correct_letter(letter, shift_letters,letters):
    temporary = None
    for pair in shift_letters:
        if pair[0] == letter:
            temporary = pair[1]
            break
    if temporary is None:
        return None
    for output in letters:
        if temporary == output[1]:
            return output[0]
    return None
        
#print(get_correct_letter('c', shift_letters,letters))

decoded_message = ""

for char in message:
    if char.isalpha():
        decoded_char = get_correct_letter(char,shift_letters,letters)
        decoded_message += decoded_char if decoded_char else char
    else:
        decoded_message += char

#print(decoded_message)

# encrypting my message

message_send = 'Hi, this is a reply'
encoded_numbers = []

for pair in letters:
    letter = pair[0]
    number = pair[1] - shift
    if number < 1:
        number = number + 26
    encoded_numbers.append([letter, number])
        
#print(encoded_numbers)

def encode(o_char, letters, encoded_numbers):
    temporary = None
    for pair in letters:
        if pair[0] == o_char:
            original_number = pair[1]
            break
    else:
        return None  # Character not found

    # Find the letter in encoded_numbers with the shifted number
    for pair in encoded_numbers:
        if pair[1] == original_number:
            return pair[0]
    return None
        
#print(encode("h",letters,encoded_numbers))

encoded_message = ""

for o_char in message_send:
    if o_char.isalpha():
        encoded_char = encode(o_char,letters,encoded_numbers)
        encoded_message += encoded_char if encoded_char else o_char
    else:
        encoded_message += o_char

#print(encoded_message)

first_message = 'jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.'
  
second_message = 'bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!'

def decoder(message_to_decode):
    output = ""
    for char in message_to_decode:
        if char.isalpha():
            decoded_char = get_correct_letter(char,shift_letters,letters)
            output += decoded_char if decoded_char else char
        else:
            output += char
    return output
    
#print(decoder(first_message))
#print(decoder(second_message))

##

third_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

letters = [['a',1],['b',2],['c',3],['d',4],['e',5],['f',6],['g',7],['h',8],['i',9],['j',10],['k',11],['l',12],['m',13],['n',14],['o',15],['p',16],['q',17],['r',18],['s',19],['t',20],['u',21],['v',22],['w',23],['x',24],['y',25],['z',26]]
shift_letters = []

for i in range(0,26):
    shift = i
    shift_letters = []
    for pair in letters:
        letter = pair[0]
        number = pair[1] + shift
        if number > 26:
            number = number - 26
        shift_letters.append([letter, number])
    print(decoder(third_message))
    print(shift)
    print("---")        
    #print(shift_letters)

