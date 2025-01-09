import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import SqrtRange

testfirstnumber = -10
testsecondnumber = 10
logFile = "log.log"
clearLog = True

SqrtRange.Calculate(testfirstnumber, testsecondnumber, logFile, clearLog)