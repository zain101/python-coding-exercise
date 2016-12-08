
# Python exercise.
Jupyter notebooks and individual scripts included.

exercise using core python.
--------------------------------------
[core python implementation](https://github.com/zain101/python-coding-exercise/tree/master/core-python-implementation)
I created a small library called redpandas which have the following features

#### Class: `RedPandas`

#### ReadCSV: `read_csv(self, filepath, sep=',')`

:    It reads the *sv file and stores them as a python dict. with column headers as keys and values as list of those keys.
:    example `read_csv('NST-EST2015-alldata.csv', sep='\t')`

#### Filter DataFrame: `filter_df(self, df, filter_element, condition)`

:    It takes input as dataframe which is the output of `read_csv` and filters a particular colunm based of the condition specified in the lamda expression.
:    example `filter_df(df, 'SUMLEV', (lambda a: a==40))`

#### Sort DataFrame: `sort_df(self, df, sort_element, reverse=True)`

:    It takes input as the dataframe and column-name which is to be sorted. When that particular column is being sorted along with that all the other column values gets shuffled with respect to that column index
:    example `sort_df(df, 'POPESTIMATE2015')`

#### Display DataFrame: `display_df(self, df, col)`

:    It takes dataframe and columns names as list and displays in tabular format
:     example `display_df(df, col= ['POPESTIMATE2015','NAME' ])`



#### Module: `histogram`

:    histogram(data_list, bins=3)
:    equal_width_binning(l, bins=3)
:    mapper(bucket, item)

#### Histogram: `histogram(data_list, bins=3)`

:    It generates a histogram by transforming numerical values to categorical values having equal width bins. `equal_width_binning(l, bins=3)` creates the break points and returns a bucket on n-bins having equal width. `mapper(bucket, item)` is responsible for counting the values that fall under those bins. Finally  `histogram(data_list, bins=3)` converges all these and returns a dict having keys as buckets and values as count.

#### [python-exercise.py](https://github.com/zain101/python-coding-exercise/blob/master/core-python-implementation/python-exercise.py)  `python-exercise.py`
:    It is the main script which demonstrates the task-1 and task-1 in action.

Jupyter Files:

:    [Task-1](https://github.com/zain101/python-coding-exercise/blob/master/core-python-implementation/core-python-task-1.ipynb)

:    [Task-2](https://github.com/zain101/python-coding-exercise/blob/master/core-python-implementation/core-python-task-2.ipynb)


exercise using pandas and numpy
---------------------------------------------------
## Task-1
....[preview](https://github.com/zain101/python-coding-exercise/blob/master/Task-1/python-coding-exercise-task1.md)

## Task-2
....[preview](https://github.com/zain101/python-coding-exercise/blob/master/Task-2/python-coding-exercise-task2.md)

