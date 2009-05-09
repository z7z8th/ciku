#[BSD Licence]
#Copyright (c) 2009, Dong Hu
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#    * Neither the name of the <ORGANIZATION> nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#!/usr/bin/python
import	sys,re

if len(sys.argv)<>3:
	print	'USAGE: '+sys.argv[0]+' <inputfile> <outfile>'
	exit()

DictfileHandle = open( 'gbkpy.org' )
p = re.compile('([a-z]+) (.+)')
DictName = {}
for line in DictfileHandle.readlines():
	m = p.match(line)
	if m:
		key = m.group(2)
		DictName[key] = m.group(1)
DictfileHandle.close()

InputfileHandle = open(sys.argv[1])
OutputfileHandle = open (sys.argv[2],'a')
ProgressIndex = 1
for line in InputfileHandle.readlines():
	ResultLine = ''
	key = ''
	for c in line:
		if ord(c)<128:
			if c<>'\r' and c<>'\n':
				ResultLine = ResultLine + c
			continue
		else:
			key = key + c
			if len(key)==2:
				if DictName.has_key(key):
					ResultLine = ResultLine + DictName[key]+'\'';
				else:
					print	 '\nError in Line:'+str(ProgressIndex)
					continue
				key=''
	OutputfileHandle.write(line+'\t3\t'+ResultLine[0:len(ResultLine)-1])
	if not (ProgressIndex%100):
		sys.stdout.write('.')
		if not (ProgressIndex % 500):
			sys.stdout.write(str(ProgressIndex))
	ProgressIndex = ProgressIndex + 1;
OutputfileHandle.close()
InputfileHandle.close()
