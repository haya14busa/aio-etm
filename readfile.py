import re
class make_xlat:
    def __init__(self, *args, **kwds):
        self.adict = dict(*args, **kwds)
        self.rx = self.make_rx()
    def make_rx(self):
        return re.compile('|'.join(map(re.escape, self.adict)))
    def one_xlat(self, match):
        return self.adict[match.group(0)]
    def __call__(self, text):
        return self.rx.sub(self.one_xlat, text)

class make_xlat_re(make_xlat):
    def make_rx(self):
        return re.compile('|'.join(self.adict))
    def dedictkey(self, text):
        for key in self.adict.keys():
            if re.search(key, text):
                return key
    def one_xlat(self, match):
        return self.adict[self.dedictkey(match.group(0))]


aiofile = open('aio.txt','r')
try:
    aio_all_text = aiofile.read()
finally:
    aiofile.close()

print aio_all_text
# aio_list = []
# for line in input.readlines():
#     aio_list.append(line)
# 
# print '\n'.join(aio_list)
