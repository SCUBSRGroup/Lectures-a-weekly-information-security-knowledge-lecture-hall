import os
import sys
import zipfile
import binascii,pprint,json
import zlib

deflate_decompress = lambda d : zlib.decompress(d, -15)
blobs = os.listdir('binaryData')
blobs = [os.path.join('binaryData',f) for f in blobs]
keystr = "xbvspdwjtgdehq523128"
key = [ord(i1) for i1 in keystr]
# helper to convert an array to a string
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


def get_data(blobname):
	for b in blobs:
		if blobname in b:
			data = open(b,'rb').read()
			return [ord(c) for c in data]
	print "ERROR:cannot read %s" % blobname
	return None

def decrypt_file():
	nw18_html_rc4=get_data("nw18_html_rc4$6213d19f7f711f6adecb4bd50c85b060-1722720879");
	#print nw18_html_rc4
	content=decrypt(key,nw18_html_rc4);
	data = deflate_decompress(content)
	open('nw18_html_rc4_decompress','wb').write(data)
	nw22_swf_rc4 = get_data('2_nw22_swf_rc4$341acf8a38c7ef2cbe35c674750c202b-394312611');
	content = decrypt(key,nw22_swf_rc4);
	#data = deflate_decompress(content);
	print "hahahah"
        #data = deflate_decompress(content);
	open('nw22_swf_decompress','wb').write(content);
        #open('nw22_swf_decompress','wb').write(data);
	nw23_swf = get_data('3_nw23_swf_rc4$ff09886f44cb2db0af6cdbff7a01061f2083705692')
	content = decrypt(key,nw23_swf)
        #nw23_swf = get_data('3_nw23_swf_rc4$ff09886f44cb2db0af6cdbff7a01061f2083705692');
        #content = decrypt(key,nw23_swf);
	#data = deflate_decompress(content);
	open('nw23_swf_decompress','wb').write(content);
	#nw2_html_rc4= get_data('4_nw2_html_rc4$1ac42c440ee054681c013a3a3f4c7c791142556130')
	nw2_html_rc4 = get_data('4_nw2_html_rc4$1ac42c440ee054681c013a3a3f4c7c791142556130')
	content = decrypt(key,nw2_html_rc4)
        #content = decrypt(key,nw2_html_rc4)
	data = deflate_decompress(content)
	open('nw2_html_rc4_decompress','wb').write(data);
	nw7_html_rc4= get_data('5_nw7_html_rc4$d73edc68888fb8485c1a384f273328d9-1886692465')
	content = decrypt(key,nw7_html_rc4)
	data =deflate_decompress(content)
	open('nw_html_rc4_decompress','wb').write(data);
	nw8_html_rc4 = get_data('6_nw8_html_rc4$839751a392981f1ce098a727b1bcb875-2109608792')
	content = decrypt(key,nw8_html_rc4)
	data= deflate_decompress(content)
	open('nw8_html_rc4_decompress','wb').write(data)

if __name__=="__main__":
        decrypt_file()
