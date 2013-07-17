import re

if __name__ == '__main__':
    aiofile = open('aio.txt','r')
    try:
        aio_all_text = aiofile.read()
    finally:
        aiofile.close()
    # text = 'He grinned and said, "I make lots of money. On weekdays I receive an average of 50 orders a day from all over the globe via the Internet."'
    trtxt = re.sub(r'\b([a-zA-z]+)\b', r'[\1] ', aio_all_text) # 2 space needed

    aio_file_object = open('aio_etm_txt.md', 'w')
    aio_file_object.write(trtxt)
    aio_file_object.close()
