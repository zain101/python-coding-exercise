import pandas as pd


population_dataset = pd.read_csv("NST-EST2015-alldata.csv")
result_df = population_dataset[ (population_dataset['SUMLEV'] == 40)].sort_values('POPESTIMATE2015', ascending=False)
print(result_df)
print("="*50,"Minimize result set","="*50,)
print(result_df[['NAME','POPESTIMATE2015']])


class OrderedStates:

	def __init__(self, filepath='NST-EST2015-alldata.csv'):
		self.population_dataset = pd.read_csv(filepath)

	def data_orderby(self):
		result_df = population_dataset[ (population_dataset['SUMLEV'] == 40)].sort_values('POPESTIMATE2015', ascending=False)

	def display_data(self):
		print(result_df)
		print("="*50,"Minimize result set","="*50,)
		print(result_df[['NAME','POPESTIMATE2015']])



if __name__ == "__main__":
	orderedPop = OrderedStates()
	orderedPop.data_orderby()
	orderedPop.display_data()
