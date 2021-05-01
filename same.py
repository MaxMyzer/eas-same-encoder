import numpy as np
from scipy.io import wavfile
import random
import sys
import subprocess # to play the resulting wave file
import datetime # EAS alerts are heavily dependent on timestamps so this makes it easy to send a thing now
import argparse

# parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--code", "-c", nargs='?', default="")
parser.add_argument("--playaudiolive", "-pal", nargs='?', default=-1)
parser.add_argument("--org", "-o", nargs='?', default="WXR")
parser.add_argument("--event", "-e", nargs='?', default="RWT")
parser.add_argument("--location", "-lo", nargs='?', default=None)
parser.add_argument("--location00", "-l00", nargs='?', default="000000")
parser.add_argument("--location01", "-l01", nargs='?', default=None)
parser.add_argument("--location02", "-l02", nargs='?', default=None)
parser.add_argument("--location03", "-l03", nargs='?', default=None)
parser.add_argument("--location04", "-l04", nargs='?', default=None)
parser.add_argument("--location05", "-l05", nargs='?', default=None)
parser.add_argument("--location06", "-l06", nargs='?', default=None)
parser.add_argument("--location07", "-l07", nargs='?', default=None)
parser.add_argument("--location08", "-l08", nargs='?', default=None)
parser.add_argument("--location09", "-l09", nargs='?', default=None)
parser.add_argument("--location10", "-l10", nargs='?', default=None)
parser.add_argument("--location11", "-l11", nargs='?', default=None)
parser.add_argument("--location12", "-l12", nargs='?', default=None)
parser.add_argument("--location13", "-l13", nargs='?', default=None)
parser.add_argument("--location14", "-l14", nargs='?', default=None)
parser.add_argument("--location15", "-l15", nargs='?', default=None)
parser.add_argument("--location16", "-l16", nargs='?', default=None)
parser.add_argument("--location17", "-l17", nargs='?', default=None)
parser.add_argument("--location18", "-l18", nargs='?', default=None)
parser.add_argument("--location19", "-l19", nargs='?', default=None)
parser.add_argument("--location20", "-l20", nargs='?', default=None)
parser.add_argument("--location21", "-l21", nargs='?', default=None)
parser.add_argument("--location22", "-l22", nargs='?', default=None)
parser.add_argument("--location23", "-l23", nargs='?', default=None)
parser.add_argument("--location24", "-l24", nargs='?', default=None)
parser.add_argument("--location25", "-l25", nargs='?', default=None)
parser.add_argument("--location26", "-l26", nargs='?', default=None)
parser.add_argument("--location27", "-l27", nargs='?', default=None)
parser.add_argument("--location28", "-l28", nargs='?', default=None)
parser.add_argument("--location29", "-l29", nargs='?', default=None)
parser.add_argument("--location30", "-l30", nargs='?', default=None)
parser.add_argument("--time", "-t", nargs='?', default="0015")
parser.add_argument("--callsign", "-cs", nargs='?', default="KEAX/NWS")
args = parser.parse_args()
######## CONFIG / constants ########

markBitFrequency = 2083 + (1/3)
spaceBitFrequency = 1562.5




print (args)


fs = 43750

# t = 1.0 / (520 + (5/6))


# f = 2083.33333

samples = np.zeros(0)


def markBit():
	global markBitFrequency

	# f = 2083.33333
	f = markBitFrequency
	t = 1.0 / (520 + (5/6))

	samples = np.arange(t * fs) / fs

	roffle = np.sin(2 * np.pi * f * samples)
	return roffle * 0.8

def spaceBit():
	global spaceBitFrequency

	# f = 1562.5
	f = spaceBitFrequency
	t = 1.0 / (520 + (5/6))

	samples = np.arange(t * fs) / fs

	return np.sin(2 * np.pi * f * samples)



signal = np.zeros(20000)


def byte(the_byte):
	sys.stdout.write(the_byte)
	sys.stdout.write(" ")
	byte_data = np.zeros(0)
	for i in range(0, 8):
		if ord(the_byte) >> i & 1:
			sys.stdout.write("1")
			byte_data = np.append(byte_data, markBit())
		else:
			sys.stdout.write("0")
			byte_data = np.append(byte_data, spaceBit())

	sys.stdout.write("\n")
	sys.stdout.flush()

	return byte_data


def extramarks(numberOfMarks):
	"""SAGE encoders seem to add a few mark bits at the beginning and end"""
	byte_data = np.zeros(0)

	for i in range(0, numberOfMarks):
		byte_data = np.append(byte_data, markBit())

	return byte_data

def preamble():
	byte_data = np.zeros(0)

	for i in range(0, 16):
		byte_data = np.append(byte_data, markBit())
		byte_data = np.append(byte_data, markBit())
		byte_data = np.append(byte_data, spaceBit())
		byte_data = np.append(byte_data, markBit())
		byte_data = np.append(byte_data, spaceBit())
		byte_data = np.append(byte_data, markBit())
		byte_data = np.append(byte_data, spaceBit())
		byte_data = np.append(byte_data, markBit())



	return byte_data


# EAS alerts are heavily dependent on timestamps so this makes it easy/fun to send a thing now
sameCompatibleTimestamp = datetime.datetime.now().strftime("%j%H%M")

LocationList = ""
# arguments are location.00 to location.30
if args.location != None:
	LocationList = "-" + args.location
else:
	Where = (args.location00, args.location01, args.location02, args.location03, args.location04, args.location05, args.location06, args.location07, args.location08, args.location09, args.location10,args.location11,args.location12, args.location13, args.location14, args.location15, args.location16, args.location17, args.location18, args.location19, args.location20, args.location21, args.location22, args.location23, args.location24, args.location25, args.location26, args.location27, args.location28, args.location29, args.location30)
	# LocationList = "-".join(Where)
	for i in range(0, 30):
		if Where[i] != None:
			LocationList+= "-" + Where[i]
		else:
			LocationList+= ""
if LocationList == "":
	LocationList = "000000"
print(LocationList)
code = "ZCZC" + "-" + args.org + "-" + args.event + "" + LocationList + "+" + args.time +  "-" + sameCompatibleTimestamp + "-" + args.callsign + "-"
if args.code != "" and args.code != None and args.code != " ":
	code = args.code


for i in range(0, 3):
	# signal = np.append(signal, extramarks(10))
	signal = np.append(signal, preamble())

	# turn each character into a sequence of sine waves
	for char in code:
		signal = np.append(signal, byte(char))

	# signal = np.append(signal, extramarks(6)) # ENDEC might not be as picky about this as I once thought

	signal = np.append(signal, np.zeros(43750)) # wait the requisite one second


# EOM (3x)
for i in range(0, 3):
	# signal = np.append(signal, extramarks(10))
	signal = np.append(signal, preamble())

	for char in "ZCZCNNNN": # NNNN = End Of Message
		signal = np.append(signal, byte(char))

	# signal = np.append(signal, extramarks(6))

	signal = np.append(signal, np.zeros(43750)) # wait the requisite one second



signal *= 32767

signal = np.int16(signal)

wavfile.write(str("same.wav"), fs, signal)


if args.playaudiolive == "1":
	subprocess.call("afplay same.wav", shell=True)
