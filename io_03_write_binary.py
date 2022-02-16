with open('binary_01', 'bw') as encode:
    encode.write(bytes(range(17)))

with open('binary_01', 'br') as read_code:
    for i in read_code:
        print(i)
