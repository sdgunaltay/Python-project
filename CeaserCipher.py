alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#import logo
#print(logo.logo)

loop= ""

def crypt():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if direction == "encode":
        text_list = list(text)
        encrypt = ""
        for i in text_list:
            if i in alphabet:
                shift_2 = alphabet.index(i) + shift
                shift_3 = shift_2 % 26
                if shift_2 < 27:
                    encrypt += alphabet[shift_3]
                # encrypt += " "
                # print(encrypt)
                # print(type(encrypt))
                # elif shift_2 == 26:
                #     encrypt += alphabet[shift_2]
                elif shift_2 > 26:
                    encrypt += alphabet[shift_3]
            else:
                encrypt += i
        print(encrypt)
            
    elif direction == "decode":
        text_list = list(text)
        decrypt = ""
        for i in text_list:
            if i in alphabet:
                decrypt += alphabet[alphabet.index(i) - shift]
            else:
                decrypt += i
        print(decrypt)
    
    loop = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if loop == "yes":

        crypt()
        if loop =="no":
            print("Goodbye")
    
    elif loop == "no":
        print("Goddbye")

crypt()
# loop = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()


#     print("Goddbye")
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
