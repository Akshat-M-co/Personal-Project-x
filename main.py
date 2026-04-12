message = input("Enter a message to encode or decode: ")  
message = message.upper()           
output = ""  
shift = eval(input("how many shifts would you like to encode/decode your message?"))
enc_or_dec = input("would you like to encode or decode a message? (enter an 'e' or a 'd')")
for letter in message:              
    if letter.isupper() and enc_or_dec == 'e':            
        value = ord(letter) + shift   
        letter = chr(value)         
        if not letter.isupper():    
            value -= 26             
            letter = chr(value)     
    if letter.isupper() and enc_or_dec == 'd':
        value = ord(letter) - shift
        letter = chr(value)
        if not letter.isupper():    
              value -= 26             
              letter = chr(value)
      
      
    output += letter                
print("Output message: ", output)  

