from __future__ import print_function
import sys
import Soros
import codecs
from os import path
#
# test input_file input_stream output_stream [conditional_language_codes...]
#
program_file = sys.argv[1]
if not path.exists(program_file):
    # search in data
    program_file = '../data/' + program_file
prg = codecs.open(program_file, encoding="UTF-8").read()
inp = codecs.open(sys.argv[2], encoding="UTF-8").readlines()
out = codecs.open(sys.argv[3], "wb", encoding="UTF-8")
s = {}
langs = ["default"] + sys.argv[4:]
for l in langs:
    s[l] = Soros.compile(prg, l)
ll = len(langs)
for l in langs:
    print("Language: " + l, file=sys.stderr)
    if ll > 1:
        print("Language: " + l, file=out)
    for i in inp:
        print(s[l].run(i.strip()), file=out)

