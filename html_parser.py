from bs4 import BeautifulSoup
import re
import lxml
import urllib.parse
'''
<ul class="slider maqueeCanvas" style="left: 0px;">
<li>
<a href="/item/%E8%96%9B%E4%BD%B3%E5%87%9D/654397" target="_blank">
<img src="https://imgsa.baidu.com/zhixin/abpic/item/9a1151c2d5628535be46eb4992ef76c6a6ef63f0.jpg">
<div title="薛佳凝" class="name">前女友<em>薛佳凝</em></div>
</a>
</li>
'''
class Html_Parser(object):

	def _get_new_urls_and_data(self,page_url,soup):
		res_data = {}
		new_urls = set()

		name = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
		res_data['name'] = name.get_text()

		frienddiv = soup.find('div',class_="star-info-block relations")
		if frienddiv == None:
			return None,None
		friendlist = frienddiv.find('ul',class_="slider maqueeCanvas")
		friends = friendlist.find_all('a')
		

		for friend in friends:
			new_url = friend['href']
			new_full_url = urllib.parse.urljoin(page_url,new_url)
			new_urls.add(new_full_url)
			
			info = {}
			info['friend_name'] = friend.div['title']
			info['friend_img'] = friend.img['src']
			info['friend_relationship'] = friend.div.contents[0]
			res_data[friend.div['title']] = info

		return new_urls,res_data


	def parse(self,page_url,html_cont):
		if page_url is None or html_cont is None:
			return
		#soup = BeautifulSoup(html_cont,'html.parser')
		soup = BeautifulSoup(html_cont,'lxml')
		
		new_urls,new_data = self._get_new_urls_and_data(page_url,soup)
		return new_urls,new_data
