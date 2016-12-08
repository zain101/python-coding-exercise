import pprint
import redpandas as rpd


def task1():
	rp = rpd.RedPandas()
	df = rp.read_csv('NST-EST2015-alldata.csv')
	df = rp.filter_df(df, 'SUMLEV', (lambda a: a==40)) 
	df = rp.sort_df(df, 'POPESTIMATE2015')
	rp.display_df(df, col= ['POPESTIMATE2015','NAME' ])


def task2():
	rp = rpd.RedPandas()
	pp = pprint.PrettyPrinter(indent=2)

	df = rp.read_csv('NST-EST2015-alldata.csv')
	df = rp.filter_df(df, 'SUMLEV', (lambda a: a==40)) 
	df = rp.sort_df(df, 'POPESTIMATE2015')
	print("\nEstimated population histogram for year 2015\n")
	pp.pprint(rpd.histogram(df['POPESTIMATE2015'], 13))
	print("\nEstimated population histogram for year 2014\n")
	pp.pprint(rpd.histogram(df['POPESTIMATE2014'], 13))
	print("\nEstimated population histogram for year 2013\n")
	pp.pprint(rpd.histogram(df['POPESTIMATE2013'], 13))
	print("\nEstimated population histogram for year 2012\n")
	pp.pprint(rpd.histogram(df['POPESTIMATE2012'], 13))
	print("\nEstimated population histogram for year 2011\n")
	pp.pprint(rpd.histogram(df['POPESTIMATE2011'], 13))
	print("\nEstimated population histogram for year 2010\n")
	pp.pprint(rpd.histogram(df['POPESTIMATE2010'], 13))	


if __name__ == '__main__':
	print("="*50+" TASK-1 "+"="*50 )
	task1()
	print("="*50+" TASK-2 "+"="*50 )
	task2()