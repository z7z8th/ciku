#!/usr/bin/python
import	sys,string

if len(sys.argv)<>3:
	print	'USAGE: '+sys.argv[0]+' <inputfile> <outfile>'
	exit()

OutputfileHandle = open(sys.argv[1])
lines = [line for line in OutputfileHandle]
OutputfileHandle.close()
slines = set(lines)
OutputfileHandle2 = open (sys.argv[2],'w')
OutputfileHandle2.write(string.join(slines,''))
OutputfileHandle2.close()
