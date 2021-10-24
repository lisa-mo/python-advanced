# # random_matrix = numpy.random.randint(min_val,max_val,(<num_rows>,<num_cols>))
# import numpy as np
#
# def create_random_matrix():
#     start = 10
#     end = 30
#     return np.random.randint(start, end, (10, 10))
#
# def my_matrix():
#     matrix = create_random_matrix()
#
#     side = 10
#     check_list_row = []
#     check_list_column = []
#
#     for row in range(side):
#         for column in range(side):
#             if matrix[row][column] == 21:
#                 check_list_row.append(row)
#                 check_list_column.append(column)
#
#     print('Минимальній элемент:', check_list_row, check_list_column)
#     print(matrix)
#
# my_matrix()
#
#
#

# To print list fansy
# names = ["Sam", "Peter", "James", "Julian", "Ann"]
# # print(*names, sep=", ")
#
# or str(my_list)[1:-1]

# To create req file
# pip freeze > requirements.txt