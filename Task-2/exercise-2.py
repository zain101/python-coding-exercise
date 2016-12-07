import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class PopulationHistogram:
	'''Generates a histogram of of estmated population n buckets having equal width '''
	
	result_df = None
	res_newdf  = None

	def __init__(self, filepath='NST-EST2015-alldata.csv', bucket=13):
		self.population_dataset = pd.read_csv(filepath)
		self.bucket=bucket

	def filter_states(self):
		self.result_df = self.population_dataset[ (self.population_dataset['SUMLEV'] == 40)]

	def data_orderby(self, ascending=False):
		self.result_df = self.result_df.sort_values('POPESTIMATE2015', ascending=ascending)

	def calculate_mean(self):
		self.result_df['mean_years_10_15'] = self.result_df[[
																'POPESTIMATE2015',
																'POPESTIMATE2014',
																'POPESTIMATE2013', 
																'POPESTIMATE2012', 
																'POPESTIMATE2011', 
																'POPESTIMATE2010']].mean(axis=1)
		

	def generate_buckets(self):
		self.result_df['buckets'] = pd.cut(np.array(self.result_df['mean_years_10_15']), 13)

	def plot_data(self):
		self.res_newdf = self.result_df[['buckets','mean_years_10_15']].groupby('buckets').count()
		print(self.res_newdf)
		self.res_newdf.plot(kind='bar')
		plt.show()

		plt.hist(self.result_df['mean_years_10_15' ], bins=13)
		plt.show()



if __name__ == '__main__':
	ph = PopulationHistogram(bucket=13)
	ph.filter_states()
	ph.data_orderby(ascending=False)
	ph.calculate_mean()
	ph.generate_buckets()
	ph.plot_data()

