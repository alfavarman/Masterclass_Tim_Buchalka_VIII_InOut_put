# with open('binary_01', 'bw') as encode:
#     encode.write(bytes(range(17)))      # bytes([i]) instead of bytes(i) which if i is num
#
# with open('binary_01', 'br') as read_code:
#     for i in read_code:
#         print(i)
#
a = 65534       # FF FE
b = 65535       # FF FF
c = 65536       # 00 01 00 00
x = 2998302     # 00 2D C0 1E

with open('binary_02', 'bw') as bytes_coding:
    bytes_coding.write(a.to_bytes(2, 'big'))
    bytes_coding.write(b.to_bytes(2, 'big'))
    bytes_coding.write(c.to_bytes(4, 'big'))
    bytes_coding.write(x.to_bytes(4, 'big'))     # most significiant byte first
    bytes_coding.write(x.to_bytes(4, 'little'))  # less significant byte first

with open('binary_02', 'br') as decoding_bytes:
    e = int.from_bytes(decoding_bytes.read(2), 'big')
    print(e)
    f = int.from_bytes(decoding_bytes.read(2), 'big')
    print(f)
    g = int.from_bytes(decoding_bytes.read(4), 'big')
    print(g)
    h = int.from_bytes(decoding_bytes.read(4), 'big')
    print(h)
    i = int.from_bytes(decoding_bytes.read(4), 'big')
    print(i)

