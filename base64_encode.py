# 自己实现对一段字符串进行base64编码
alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
print(alphabet)
src = 'abcd'
def base64encode(src:str):
    ret = bytearray()
    if isinstance(src, str):
        _src = src.encode()
    else:
        return
    length = len(_src)
    for offset in range(0, length, 3):
        triple = _src[offset:offset+3] # 切片可以超界
        #print(triple)
        r = 3 - len(triple)
        if r:
         triple += b'\x00' * r # 便于计算先补零
        #print(triple, r)
        # bytes和 bytearray都是按照字节操作的，需要转换为整数才能进行位运算
        # 将3个字节看成一个整体转成字节bytes，大端模式
        # abc => 0x616263
        b = int.from_bytes(triple, 'big')
        #print(b, hex(b))
        # 01100001 01100010 01100011 # abc
        # 011000 010110 001001 100011 # 每6位断开
        for i in range(18, -1, -6):
            #print(hex(b), i)

            index = b >> i if i == 18 else b >> i & 0x3F
            #print(index, alphabet[index])
            ret.append(alphabet[index])
            # 替换等号
        if r:
            ret[-r:] = b'=' * r # 从索引-r到末尾使用右边的多个元素依次替换
    return bytes(ret)
import base64
strlist = ['a', '`', 'ab', 'abc', 'abcd', "ManMa", '教育a']
for x in strlist:
    print(x)
    print(base64encode(x))
    print(base64.b64encode(x.encode()))