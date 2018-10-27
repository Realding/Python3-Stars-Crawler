import url_manager
import html_downloader
import html_parser
#import html_outpute
import sqlite_output
import sqlite_db_create
import time


class CrawlerMain(object):
    def __init__(self):
        #init database
        self.db_name = 'test.db'
        sqlite_db_create.dbcreate(self.db_name)
        
        self.urls = url_manager.Url_Manager()
        self.downloader = html_downloader.Html_Downloader()
        self.parser = html_parser.Html_Parser()
        self.outputer = sqlite_output.Sqlite_Outputer()
        #self.outputer = html_outputer.Html_Outputer()
        

    def craw(self, root_url):
        starttime = time.perf_counter()
        print("Crawler begin...")
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('crawl %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break
                count += 1
            except Exception as e:
                print('crawl failed',e)

        #self.outputer.output_html()
        print("Crawl finished")
        self.outputer.output_db(self.db_name)
        finishtime = time.perf_counter()
        print("Total time:",finishtime-starttime,"Seconds")

if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/胡歌/312718"
    obj_spider = CrawlerMain()
    obj_spider.craw(root_url)
