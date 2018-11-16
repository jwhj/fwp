from c import *
import argparse
parser=argparse.ArgumentParser(description='blablabla')
parser.add_argument('-i',type=str,required=1)
parser.add_argument('-a',type=str)
parser.add_argument('-k',type=int,default=0)
parser.add_argument('-o',type=str,default='output.png')
parser.add_argument('-d',action='store_true')
args=parser.parse_args()
if (args.d):
	a=cv2.imread(args.i)
	a=decode(a,args.k)
	cv2.imwrite(args.o,a)
else:
	if (args.a is None):
		args.a=args.i
	a=cv2.imread(args.i)
	b=cv2.imread(args.a)
	a=encode(a,b,args.k)
	cv2.imwrite(args.o,a)
