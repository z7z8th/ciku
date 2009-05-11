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
import	sys,re,getopt

def	usage():
	print	'USAGE:	$python '+sys.argv[0]+' -t TYPE -s INPUT -d OUTPUT'
	print	'		TYPE	f/g:Convert To Fcitx/Google Thesaurus'
	print	'		INPUT	Filename Of Sogou Thesaurus File'
	print	'		OUTPUT	Filename Of Output File'
	print	'EG:	$python ',sys.argv[0],' -t f -s sogou.txt -d fcitx.txt'
	print	'	$python ',sys.argv[0],' -t g -s sogou.txt -d google.txt'
	sys.exit()
	
def	loaddict():
	DictfileHandle = open('gbkpy.org')
	p = re.compile('^([a-z]+) ([^\r]+)([\r\n]+)')
	Dict = {}
	for line in DictfileHandle.readlines():
		m = p.match(line)
		if m:
			key = m.group(2)
			Dict[key] = m.group(1)
	DictfileHandle.close()
	return	Dict

def	main(argv):
	try:
		opts,args = getopt.getopt(argv,'ht:s:d:',['help'])
	except getopt.GetoptError:
		print	'ERROR: Unkonwn Arguments'
		usage()
	for opt,arg in opts:
		if opt in ('-h','--help'):
			usage()
		elif opt in ('-t'):
			type = arg
		elif opt in ('-s'):
			inputfile = arg
		elif opt in ('-d'):
			outputfile = arg
		else:
			print	'ERROR: Unkonwn Arguments'
			usage()
	Dict = loaddict()
	if not Dict:
		print	'ERROR:	Failed To Load gbkpy.org'
		sys.exit()
	InputfileHandle = open(inputfile)
	OutputfileHandle = open (outputfile,'w')
	ProgressIndex = 1
	for line in InputfileHandle.readlines():
		NewLine = ''
		key = ''
		for c in line:
			if ord(c)<128:
				if c<>'\r' and c<>'\n':
					NewLine = NewLine + c
				key = ''
				continue
			else:
				key = key + c
				if Dict.has_key(key):
					NewLine = NewLine + Dict[key]+'\'';
				else:
					continue
				key = ''
		if type=='f':
			OutputfileHandle.write(NewLine[0:len(NewLine)-1]+' '+line)
		elif type=='g':
			OutputfileHandle.write(line[0:len(line)-1]+'\t3\t'+NewLine[0:len(NewLine)]+'\n')
		else:
			print	'TYPE ERROR.Currently Only f(Fcitx)/g(Google) Are Supported\n'
			sys.exit()
		if not (ProgressIndex%100):
			sys.stdout.write('.')
			if not (ProgressIndex % 500):
				sys.stdout.write(str(ProgressIndex))
		ProgressIndex = ProgressIndex + 1;
	print	'Completed!',ProgressIndex,' items converted\n'	
	OutputfileHandle.close()
	InputfileHandle.close()

if __name__=="__main__":
	main(sys.argv[1:])
