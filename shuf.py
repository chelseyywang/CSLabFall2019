#!/usr/bin/python
import sys
import random
import string
import argparse

class shuf:
    def __init__(self, filename):
        if filename == "-" or filename is None:
            self.lines = []
            while True:
                f = sys.stdin.readline()
                if f == '':
                    break
                self.lines.append(f)


        else:
            f = open(filename, 'r')
            self.lines = f.readlines()
            f.close()

    def chooseline(self):
        return random.choice(self.lines)
    def __getitem__(self, index):
        return self.lines[index]
    def __len__(self):
        return len(self.lines)

#done setting up!
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("FILE", nargs='?', default=None, help="files you input")
    parser.add_argument("-i", "--input-range", help="input a range you want to shuffle through", action='store', default=None)
    parser.add_argument("-n", "--head-count", help="list how many shuffled lines you want outputted", action='store', dest='head_count', default=None)
    parser.add_argument("-r", "--repeat", help="Repeat output values, that is, select with replacement.", action="store_true")

    try:
        args = parser.parse_args(sys.argv[1:])
    except:
        print("MY ERROR: ur parser is WACK")
        sys.exit(1)

    ############################
    #checking input range
    ############################
    #-i = -i, ~n, ~r

    if args.input_range:
    # and args.head_count is None and args.repeat is False and args.FILE is None:
        #check if hyphen exists
        mylen = len(args.input_range)
        ilen = int(mylen)

        if ilen == 0:
            print("MY ERROR: nothing in input :(")
            sys.exit(1)
        try:
            dashi = args.input_range.index('-')
        except:
            print("MY ERROR: unable to locate a dash! :(")
            sys.exit(1)
        #check if low and high are valid numbers
        low = ''
        high = ''
        var = None
        irange = args.input_range
        for i in irange:
            if i!='-' and var == None:
                low+=i
            elif i=='-' and var == None:
                var = True
            elif var == True:
                high+=i

        try:
            ilow = int(low)
            ihigh = int(high)
            if ilow<0:
                print("MY ERROR: negative lower bound :(")

        except:
            print("MY ERROR: invalid range :(")
            sys.exit(1)
        #executing printing random numbers
        if ilow>ihigh and (ilow-ihigh)>2:
            print("low is bigger than high??")
            sys.exit(1)
        size = ihigh-ilow+1
        randlist = random.sample(range(ilow, ihigh+1), size)
        # (-i)
        if args.head_count is None and args.repeat is False:
            for item in randlist:
                print (item)
        #(-i, -n)
        elif args.repeat is False:
            num = args.head_count
            inum = int(num)
            for i in range(inum):
                print (randlist[i])
        elif args.repeat is True and args.head_count is None:
            while args.repeat is True:
                print(random.choice(randlist))
        #(-i, -n, -r)
        elif args.repeat is True:
            num = args.head_count
            inum = int(num)
            for i in range(0, inum):
                print(random.choice(randlist))


    #####################################
    #if -i, ~n, ~r, but file is
    # if args.input_range and args.head_count is None and args.repeat is False:
    #     print("extra operand :(")
    #     sys.exit(1)

    ######################################
    #check head_count (only -n)
    ######################################

    #-n = -n, ~i, ~r
    if args.head_count and args.repeat is False and args.input_range is None:
        lines = shuf(args.FILE)
        try:
            numlines = int(args.head_count)
            if numlines<0:
                print("MY ERROR: negative amount :(")
                sys.exit(1)
        except:
            print("MY ERROR: invalid: " + str(args.head_count) + " :(")
            sys.exit(1)
        #proceeding with execution
        if int(args.head_count) > len(lines):
            numlines = len(lines)
        #making a list so i can shuffle it
        mylist = []
        for item in range(0, len(lines)):
            if item==len(lines)-1:
                mylist.append(lines[item]+'\n')
            else:
                mylist.append(lines[item])
        random.shuffle(mylist)
        for item in range(0, numlines):
            print(mylist[item], end="")
    #, end=""
    #######################
    #check repeat
    #######################
    # -r , -nr -> -r, ~n, ~i and -r, -n, ~i
    ### only -r flag (no -i) ; checking -n ###
    if args.repeat and args.input_range is None:
        if args.head_count:
            lines = shuf(args.FILE)
            try:
                numlines = int(args.head_count)
                if numlines<0:
                    print("MY ERROR: negative amount :(")
                    sys.exit(1)
                elif numlines>len(lines):
                    print("MY ERROR: you chose: " + str(args.head_count) + " too big! :(")
                    print("MY ERROR: max size: " + str(len(lines)))
                    sys.exit(1)
            except:
                print("MY ERROR: invalid: " + str(args.head_count) + " :(")
                sys.exit(1)
            #proceeding with execution
            #making a list so i can shuffle it
            mylist = []
            for item in range(0, len(lines)):
                if item==len(lines)-1:
                    mylist.append(lines[item]+'\n')
                else:
                    mylist.append(lines[item])
            for item in range(0, numlines):
                print(random.choice(mylist), end="")
                #, end=""
        if args.head_count is None:
            lines = shuf(args.FILE)
            mylist = []
            for item in range(0, len(lines)):
                if item==len(lines)-1:
                    mylist.append(lines[item]+'\n')
                else:
                    mylist.append(lines[item])
            while args.head_count is None:
                print(random.choice(mylist, end=""))
                #, end=""


    #print(args)
if __name__ == "__main__":
    main()
