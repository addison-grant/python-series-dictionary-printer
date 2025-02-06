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
