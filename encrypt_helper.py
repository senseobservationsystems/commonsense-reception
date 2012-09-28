"""
Copyright (C) [2012] Sense Observation Systems B.V.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
 
http://www.apache.org/licenses/LICENSE-2.0
 
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

"""
getHexStr() and getByteStr() were inspired by/copied from 
http://code.activestate.com/recipes/510399-byte-to-hex-and-hex-to-byte-string-conversion/
Thanks to Simon Peverett! 
"""

def getHexStr (s):
	return ''.join( [ "%02X" % ord( x ) for x in s ] )

def getByteStr (s):
	b = []
	for i in range(0, len(s), 2):
		b.append( chr( int (s[i:i+2], 16 ) ) )
	return ''.join( b )

def rsa_encrypt (text, rsa):
	return rsa.encrypt(text, 0)[0]

def aes_encrypt (text, aes):
	while len(text) % 16 != 0:
		text += '0'
	return aes.encrypt(text)
