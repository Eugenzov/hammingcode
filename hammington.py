

def is_even(bits):
    #takes a bitsream and returns true if even otherwise false
    counter = 0
    for i in ((bits)):
        if i == 1:
            counter += 1
    if counter%2 == 0:
        return True
    else:
        return False

def decimal_to_binary_bitstream(decimal_number):
    if decimal_number == 0:
        return [0]  # Special case for 0
    
    binary_bitstream = []
    while decimal_number > 0:
        binary_bitstream.append(decimal_number % 2)
        decimal_number //= 2
    
    # Reverse the list to get the correct bitstream order
    binary_bitstream.reverse()
    return binary_bitstream

def encodeHAM74(b): 
    #takes a number and encodes a message for PPMPMMM logic
    #remove incomplete messages
    if len(b)%4 !=0:
        b = b[:-int(len(b)%4)]
    c = []
    for i in range(int(len(b)/4)):
        tempbitstream = [1,1,b[i*4],1,b[1+i*4],b[2+i*4],b[3+i*4]]
        if is_even([b[i*4],b[1+i*4],b[3+i*4]]) == True:
            tempbitstream[0] = 0
        if is_even([b[i*4],b[2+i*4],b[3+i*4]]) == True:
            tempbitstream[1] = 0
        if is_even([b[1+i*4],b[2+i*4],b[3+i*4]]) == True:
            tempbitstream[3] = 0
        c.append(tempbitstream)
    return c 

def encodeHAM1511(b): 
    if len(b)%11 !=0:
        b = b[:-int(len(b)%11)]
    c = []
    for i in range(int(len(b)/11)):
        tempbitstream = [1,1,b[i*11],1,b[1+i*11],b[2+i*11],b[3+i*11],1,b[4+i*11],b[5+i*11],b[6+i*11],b[7+i*11],b[8+i*11],b[9+i*11],b[10+i*11]]
        print(len(tempbitstream))
        if is_even([b[i*11],b[1+i*11],b[3+i*11],b[4+i*11],b[6+i*11],b[8+i*11],b[10+i*11]]) == True:
            tempbitstream[0] = 0
        if is_even([b[i*11],b[2+i*11],b[3+i*11],b[5+i*11],b[6+i*11],b[9+i*11],b[10+i*11]]) == True:
            tempbitstream[1] = 0
        if is_even([b[1+i*11],b[2+i*11],b[3+i*11],b[7+i*11],b[8+i*11],b[9+i*11],b[10+i*11]]) == True:
            tempbitstream[3] = 0
        if is_even(b[4:]) == True:
            tempbitstream[7]=0
        c.append(tempbitstream)
    return c 

def decodeHAM74(c): 
    pass

def decodeHAM1511(c): 
    pass

print(encodeHAM74([0,1,1,0]))
print(encodeHAM1511([1,1,0,0,1,0,0,1,0,1,0]))