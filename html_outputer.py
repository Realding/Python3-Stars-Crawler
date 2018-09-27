import json
class Html_Outputer(object):
	def __init__(self):
		self.datas = []

	def collect_data(self,data):
		if data is None:
			return
		self.datas.append(data)

	def output_html(self):

		#string
		fout = open("output.txt","w",encoding="utf-8")
		
		for data in self.datas:
			collection = {}
			name = data['name']
			fout.write(name)
			del data['name']
			for friend in data.values():
				fname = friend['friend_name']
				frelation = friend['friend_relationship']

				if(frelation not in collection):
					collection[frelation]=[]
				collection[frelation].append(fname)
			for rela in collection.keys():
				fout.write("\t[%s]:"%rela)
				for f in collection[rela]:
					fout.write(" %s"%f)

			fout.write("\n")
		#out.encode('utf-8').decode('unicode_escape')
		fout.close()