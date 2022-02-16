with open('binary_01', 'bw') as encode:
    for i in range(17):
        encode.write(bytes([i]))

with open('binary_01', 'br') as read_code:
    for i in read_code:
        print(i)