#!/usr/bin/python
import	sys,string

if len(sys.argv)<>3:
	print	'USAGE: '+sys.argv[0]+' <inputfile> <outfile>'
	exit()

InputfileHandle = open(sys.argv[1])
InputfileString = InputfileHandle.read()
InputfileHandle.close()
TempString = InputfileString.split('\n')
TempString.sort()
OutputfileHandle = open(sys.argv[2],'w')
OutputfileHandle.write(string.join(TempString,'\n'))
OutputfileHandle.close()
