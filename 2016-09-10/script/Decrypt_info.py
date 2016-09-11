#encoding:utf-8
import os
import sys
import binascii,pprint,json
key = [ord(i1) for i1 in "rjtmklvxckkvjvs287171"]
def array2str(array):
    s = ''
    for byte in array:
        s += chr(byte)
    return s
def decrypt(param1, param2):
    print "len(param1)=%d bytes" % len(param1)
    print "len(param2)=%d bytes" % len(param2)
    i1 = 0
    i2 = 0
    j = 0
    _arr2 = []
    _arr1 = [i1 for i1 in range(256)]
    for i1 in range(256):
        j = (j + _arr1[i1] + param1[i1 % len(param1)]) & 0xff
        k = _arr1[i1]
        _arr1[i1] = _arr1[j]
        _arr1[j] = k
    j = 0
    i1 = 0
    for i2 in range(len(param2)):
        i1 = (i1 + 1) & 0xff
        j = (j + _arr1[i1]) & 0xff
        k = _arr1[i1]
        _arr1[i1] = _arr1[j]
        _arr1[j] = k
        _arr2.append(param2[i2] ^ _arr1[(_arr1[i1] + _arr1[j]) & 0xff])
    return array2str(_arr2)
def decrypt_url(filename):
	if not filename:
		print "Cant read file"
		return None
	data = open(filename,'rb').read()
	length=int(data[0:3],16)
	ciphertxt = [ord(i) for i in data[3:length+3]]
	plaintext = decrypt(key,ciphertxt)
	return plaintext
if __name__=="__main__":
	filename = "tbsxlhvoyiqv.bin"
	text = decrypt_url(filename)
	#print text
	configinfo = json.loads(text)
	json.dump(configinfo,open('configinfo.json','w'))
	#open("configinfo.json",'w+').write(configinfo)
	print configinfo
