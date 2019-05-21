# base64解码实现
from collections import OrderedDict
base_tbl = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
# 用字典查询提升效率，有序字典只是为了顺便记录顺序
alphabet = OrderedDict(zip(base_tbl,range(64)))
def base64decode(src:bytes):
    ret = bytearray()
length = len(src)
if length % 4 != 0:
return step = 4 # 对齐的，每次取4个
for offset in range(0, length, step):
tmp = 0x00
block = src[offset:offset + step]
# 反查表，从字符到index
for i in range(4):
index = alphabet.get(block[-i-1])
if index:
# txt = "TWE="
# txt = "TQ=="
# txt = "TWFuTWE="
# txt = "TWFuTQ=="
txt = txt.encode()
print(txt)
print(base64decode(txt).decode())
# base64实现
import base64
print(base64.b64decode(txt).decode())