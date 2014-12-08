import os.path
import sys
import getopt
import random
from PIL import Image

def destroyJPEG(min, max, p, times):
	original = Image.open(p)
	unsuffixed = '.'.join(os.path.basename(p).split('.')[0:-1])
	path = os.path.dirname(os.path.abspath(p))
	if min < 1:
		min = 1
	if max > 95:
		max = 95
	i = 1
	if type(times) is list:
		times.sort()
		while i <= times[-1]:
			if i is 1:
				original.save(path + "/" + unsuffixed + '.d.jpg', quality = random.randint(min, max))
			else:
				Image.open(path + "/" + unsuffixed + '.d.jpg').save(path + "/" + unsuffixed + '.d.jpg', quality = random.randint(min, max))
			if i in times:
				Image.open(path + "/" + unsuffixed + '.d.jpg').save(path + "/" +  unsuffixed + '.d' + str(i) +'.png')
			sys.stdout.write("\r" + str(int(float(i) * 100 / float(times[-1]))) + "%")
			sys.stdout.flush()
			i += 1
	elif type(times) is int:
		while i <= times:
			if i is 1:
				original.save(path + "/" + unsuffixed + '.d.jpg', quality = random.randint(min, max))
			else:
				Image.open(path + "/" + unsuffixed + '.d.jpg').save(path + "/" + unsuffixed + '.d.jpg', quality = random.randint(min, max))
			sys.stdout.write("\r" + str(int(float(i) * 100 / float(times))) + "%")
			sys.stdout.flush()
			i += 1

def main(argv):
	if len(argv) is 5:
		destroyJPEG(int(argv[1]), int(argv[2]), argv[3], int(argv[4]))
	elif len(argv) >= 6:
		times = []
		for t in argv[4:]:
			times.append(int(t))
		destroyJPEG(int(argv[1]), int(argv[2]), argv[3], times)
	else:
		print "python destroyjpeg.py MIN MAX INPUT savetime1 savetime2 savetime3 ... savetimen"

main(sys.argv)