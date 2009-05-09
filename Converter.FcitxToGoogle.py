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
import	re,sys

if len(sys.argv)<>3:
	print	'USAGE: '+sys.argv[0]+' <inputfile> <outputfile>'
	exit()

InputfileHandle = open (sys.argv[1])
OutputfileHandle = open (sys.argv[2],'w')
p = re.compile('([a-z\']+)	(.+)')
ProgressIndex = 1
for line in InputfileHandle.readlines():
	m = p.match(line)
	if m:
		Newline = m.group(2)+'	3	'+m.group(1)+'\n'
		OutputfileHandle.write(Newline)
	if not (ProgressIndex%500):
		sys.stdout.write('.')
		if not (ProgressIndex % 5000):
			sys.stdout.write(str(ProgressIndex))
	ProgressIndex = ProgressIndex + 1;
InputfileHandle.close()
OutputfileHandle.close()
