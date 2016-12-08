from operator import itemgetter
import collections

class RedPandas:
	''' 
		#### Class: `RedPandas`

		ReadCSV: `read_csv(self, filepath, sep=',')`
		:    It reads the *sv file and stores them as a python dict. 
			 with column headers as keys and values as list of those keys.
		:    example `read_csv('NST-EST2015-alldata.csv', sep='\t')`

		Filter DataFrame: `filter_df(self, df, filter_element, condition)`
		:    It takes input as dataframe which is the output of `read_csv` and filters a 
			particular colunm based of the condition specified in the lamda expression.
		:    example `filter_df(df, 'SUMLEV', (lambda a: a==40))`

		Sort DataFrame: `sort_df(self, df, sort_element, reverse=True)`
		:    It takes input as the dataframe and column-name which is to be sorted.
			 When that particular column is being sorted along with that all the other 
			 column values gets shuffled with respect to that column index
		:    example `sort_df(df, 'POPESTIMATE2015')`

		Display DataFrame: `display_df(self, df, col)`
		:    It takes dataframe and columns names as list and displays in tabular format
		:     example `display_df(df, col= ['POPESTIMATE2015','NAME' ])`

	'''

	def __init__(self):
		pass


	def read_csv(self, filepath, sep=','):
		flag = True
		df = []
		with open(filepath, 'r') as f:
			results = []
			for line in f:
					words = line.split(sep)
					words.append(words.pop(-1).strip('\n'))
					if flag:
						df = collections.OrderedDict((key,[]) for key in words)

					if not flag:
						for i,j in enumerate(df):
							try:
								df[j].append(float(words[i]))
							except:
								df[j].append(words[i])
					flag=False
					results.append(( words[:]))
		return df

	def filter_df(self, df, filter_element, condition):
		srt_key = [ i for i, j in enumerate(df[filter_element]) if condition(j)]
		new_df = collections.OrderedDict()
		for k,v in df.items():
			new_df[k] = list(itemgetter(*srt_key)(v))
		return new_df

	def sort_df(self, df, sort_element, reverse=True):
		srt_key = [i for i, e in sorted(enumerate(df[sort_element]), key=itemgetter(1), reverse=reverse)]
		new_df = collections.OrderedDict()
		for k,v in df.items():
			new_df[k] = list(itemgetter(*srt_key)(v))
		
		return new_df

	def display_df(self, df, col):
		if col:
			str_template = ""
			inner_template = ""
			for i,j in enumerate(col):
				str_template = str_template+"{:10}\t\t"
				inner_template = inner_template+"{:10}\t\t"
			str_template = str_template.format(*col)

			print("INDEX\t\t"+str_template)
			for i in range(len(df['NAME'])):
				print(str(i)+"\t\t", inner_template.format(*[(lambda co: str(df[co][i]))(co) for co in col  ] ))
