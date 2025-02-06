# python-series-dictionary-printer
 Print a sequence of series in Python (better to use Pandas or some other library, probably)

Learned a little bit about formatting strings in Python this evening:

```python
def print_table(series_dictionary):
    
    # Pull the pieces of the table values out of the dictionary
    number_of_series = len(series_dictionary.items())
    headers = list(series_dictionary.keys())
    series = list(series_dictionary.values())

    # Set up format strings to be filled in in the output
    header_subunit = ["{:15}"]*number_of_series
    series_subunit = ["{:> 15g}"]*number_of_series
    header_format_string = " | ".join(header_subunit)
    series_row_format_string = " | ".join(series_subunit)
    
    # Generate header (fill in headers)
    header_string = header_format_string.format(*headers)
    header_underline = "="*len(header_string)

    print(header_string)
    print(header_underline)
    for i in range(len(series[0])):
        row_elements = [s[i] for s in series]
        row_string = series_row_format_string.format(*row_elements)
        print(row_string)
```
Example data:
```python
n_list = [1, 2, 3]
p_n_list = [1.2, 2.3, 3.4]
epsilon_list = [0.01, 0.001, 0.00001]
series_dictionary = {
    "n": n_list,
    "p_n": p_n_list,
    "epsilon": epsilon_list,
}
```
Using the function:
```python
print_table(series_dictionary)
```
Output:
```
n               | p_n             | epsilon        
===================================================
              1 |             1.2 |            0.01
              2 |             2.3 |           0.001
              3 |             3.4 |           1e-05
```

Nice thing about this version is you can give anywhere from 1 to infinity series (okay, not infinity)

Also, I like Pandas a bit better, but this was just for fun.
