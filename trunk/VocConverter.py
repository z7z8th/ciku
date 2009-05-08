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
	OutputfileHandle.write(ResultLine[0:len(ResultLine)-1]+' '+line)
	if not (ProgressIndex%100):
		sys.stdout.write('.')
		if not (ProgressIndex % 500):
			sys.stdout.write(str(ProgressIndex))
	ProgressIndex = ProgressIndex + 1;
OutputfileHandle.close()
InputfileHandle.close()
