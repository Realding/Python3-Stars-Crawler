import html_parser
import html_downloader
import time

st = time.process_time()
parser = html_parser.Html_Parser()
downloader = html_downloader.Html_Downloader()

url = "https://baike.baidu.com/item/胡歌/312718"

html = downloader.download(url)
print(time.process_time()-st)
st = time.process_time()
#print(html.decode('utf-8'))
print(parser.parse("https://baike.baidu.com/",html))
print(time.process_time()-st)
