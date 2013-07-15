import re
import sets
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


if __name__ == '__main__':
    aiofile = open('aio.txt','r')
    try:
        aio_all_text = aiofile.read()
    finally:
        aiofile.close()
    rmdict = {
      '(\,|\.|\;|\:|\?|\!)' : '',
      '(\"|\')' : ''
    }
    rmtrans = make_xlat_re(rmdict)
    rmtext = rmtrans(aio_all_text).lower()
    wsets = sets.Set(rmtext.split())
    wlist = list(wsets)
    wlist.sort()
    # print wlist
    # wtext = '\n'.join(wlist)
    aio_etm_list = []
    etm_url = 'http://www.etymonline.com/index.php?allowed_in_frame=0&search='
    for item in wlist:
        txt = "[{word}]:{baseurl}{word}".format(
                 word = item, baseurl = etm_url
                )
        aio_etm_list.append(txt)

    etm_url_txt = '\n'.join(aio_etm_list)

    aio_file_object = open('aio_etm_url.md', 'w')
    aio_file_object.write(etm_url_txt)
    aio_file_object.close()
