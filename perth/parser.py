"""Perth Parser

All Perth commands are, in reality, Python functions. All Python functions that are used for Perth commands take a Stack value (usually named s) that
they modify in some form. Thusly, all Python functional Perth commands have the signature:

def funcName(s)

See the existing commands for example."""

import time
from implementations import *

def getTime(s): # char "T", gets time and puts it on stack
	s.pushVal(int(round(time.time())))

def prnt(s):
	print(str(s.popVal()))

def adder(s):
	v1 = s.popVal()
	v2 = s.popVal()
	if type(v1) != int or type(v2) != int:
		raise PerthError("Non-integer values {!s} and {!s} passed to +".format(v1,v2))
	s.pushVal(v1+v2)

def log(v):
	return #NO-OP
	print "[DEBUG] "+str(v)

commands = {"T":getTime,"p":prnt,"+":adder}

putstacktypes = {"i":"int","s":"str"}

def parse(prog):
	s = Stack()
	i=0
	while i < len(prog):
		cmdchar = prog[i]
		if cmdchar in ("i","s"):
			pipe = prog[i+1:].find("|")
			if pipe == -1:
				raise PerthError("Unterminated "+putstacktypes[cmdchar]+" value at char "+str(i)+"!")
			log(pipe)
			value = prog[i+1:pipe+2]
			log(value)
			if cmdchar == "i":
				try:
					s.pushVal(int(value))
				except ValueError:
					raise PerthError("Invalid "+putstacktypes[cmdchar]+" at char "+str(i)+"!")
			else:
				s.pushVal(value)
			i = pipe + 3
		else:
			if cmdchar in commands:
				commands[cmdchar](s)
			i += 1
