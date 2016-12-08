
def equal_width_binning(l, bins=3):
	max = l[0]+0.1
	min = l[-1]
	w = (max-min)/bins
	val = min
	i = 1
	bucket = []
	breaks = []
	breaks.append(min)
	while True:
		val = min+(i*w)
		i+=1
		if val > max:
			break
		breaks.append(val)

	breaks.sort()    

	for i in range(len(breaks)-1):
		bucket.append((breaks[i], breaks[i+1]))
	return bucket
					  


def mapper(bucket, item):

	for value in bucket:
		if item>=value[0] and item<value[1]:
			return value
	else:
		raise "NO match found..."
	
def histogram(data_list, bins=3):
	'''
		#### Module: `histogram`
		:    histogram(data_list, bins=3)
		:    equal_width_binning(l, bins=3)
		:    mapper(bucket, item)

		Histogram: `histogram(data_list, bins=3)`
:   				It generates a histogram by transforming numerical values to categorical 
					values having equal width bins. `equal_width_binning(l, bins=3)` 
					creates the break points and returns a bucket on n-bins having equal width. 
					`mapper(bucket, item)` is responsible for counting the values that fall under 
					those bins. Finally  `histogram(data_list, bins=3)` 
					converges all these and returns a dict having keys as buckets and values as count.
	'''
	bucket = equal_width_binning(data_list, bins)
	histo = {i:0 for i in bucket}
	for i in data_list:
		key = mapper(bucket, i)
		histo[key]+=1
	return histo

