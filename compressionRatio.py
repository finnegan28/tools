import lz4
import sys
from itertools import chain
import os


def run():
    fileDir = '/root/thermite/target/release/thermite_test_Neil'
    ratioFile_path = sys.argv[1]
    ratioList = []

    openData = open(fileDir, "rb")
    ratioFile = open(ratioFile_path, "w")	
	
    vvfd= os.open(fileDir, os.O_RDONLY)
    vvData = os.lseek(vvfd, 0, os.SEEK_END)

    upper_limit = vvData / 4096

    for x in xrange(0, upper_limit, 1):
        openData.seek(4096*x, 0)
        data = openData.read(4096)
        compOutput = lz4.compress(data)
        sys.getsizeof(compOutput)
        ratio = sys.getsizeof(compOutput) / float(sys.getsizeof(data))
        ratioFile.write(str(ratio) + '\n')

    ratioFile.close()

run()

