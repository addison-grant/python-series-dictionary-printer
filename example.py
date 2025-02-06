from print_table import print_table

# Some data
n_list = [1, 2, 3]
p_n_list = [1.2, 2.3, 3.4]
epsilon_list = [0.01, 0.001, 0.00001]
series_dictionary = {
    "n": n_list,
    "p_n": p_n_list,
    "epsilon": epsilon_list,
}

print_table(series_dictionary)

"""Output
n               | p_n             | epsilon        
===================================================
              1 |             1.2 |            0.01
              2 |             2.3 |           0.001
              3 |             3.4 |           1e-05
"""
