#!/usr/bin/python
import	re,sys

if len(sys.argv)<>3:
	print 'USAGE: '+sys.argv[0]+' <inputfile> <outputfile>'
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