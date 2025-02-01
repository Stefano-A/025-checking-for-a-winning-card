# def check_card(dict_card):
#     # check columns
#     for n_column in dict_card.values():
#         # if is_win:
#         #     break
#         # else:
#         # for c in n_column:
#         for index, number in enumerate(n_column):
#             if number != 0:
#                 break
#             if index+1 == len(n_column):
#                 return
#             # if len(n_column)-1 == n_column.index(c):
#             #     return

#             #     is_win = True
#             # else:
#             #     is_win = False
#             #     break
#     # check rows
#     is_win = False
#     if not is_win:
#         for i in range(len(dict_card)):
#             # if is_win:
#             #     break
#             # else:
#                 n_row = list(item[i] 
#                             for item in dict_card.values())
#                 for r in n_row:
#                     if r == 0:
#                         is_win = True
#                     else:
#                         is_win = False
#                         break
#     # check diagonals
#     a = [[1,2,3],[4,5,6]]
#     print(a[1][2])
#     if not is_win:
#         diagonal_1 = dict_card['B'][0], dict_card['I'][1], dict_card['N'][2], dict_card['G'][3], dict_card['O'][4]
#         for d in diagonal_1:
#             if d == 0:
#                 is_win = True
#             else:
#                 is_win = False    
#                 diagonal_2 = dict_card['B'][4], dict_card['I'][3], dict_card['N'][2], dict_card['G'][1], dict_card['O'][0]
#                 for d in diagonal_2:
#                     if d == 0:
#                         is_win = True
#                     else:
#                         is_win = False
#                         break
#                 break    
#     return is_win            

# card_1 = {
#     'B':[0,1,6,12,0],
#     'I':[16,20,0,18,25],
#     'N':[0,45,0,33,38],
#     'G':[51,48,55,53,46],
#     'O':[61,75,68,73,65]
# }

# card_2 = {
#     'B':[0,0,0,0,0],
#     'I':[16,20,0,18,25],
#     'N':[0,45,0,33,38],
#     'G':[51,48,55,53,46],
#     'O':[61,75,68,73,65]
# }

# card_3 = {
#     'B':[0,1,0,12,0],
#     'I':[16,20,0,18,25],
#     'N':[0,45,0,33,38],
#     'G':[51,48,0,53,46],
#     'O':[61,75,0,73,65]
# }
    
# card_4 = {
#     'B':[0,1,6,12,0],
#     'I':[16,20,0,0,25],
#     'N':[0,45,0,33,38],
#     'G':[51,0,55,53,46],
#     'O':[0,75,68,73,65]
# }

# check_1 = check_card(card_1)
# check_2 = check_card(card_2)
# check_3 = check_card(card_3)
# check_4 = check_card(card_4)
# list_check = [check_1, check_2, check_3, check_4]

# for n_card in range(0,4):
#     if list_check[n_card]:
#         print(f'Card {n_card+1} is winner')
#     else:
#         print(f'Card {n_card+1} is loser')



def check_card_elements(card):
    x = len(card[0])
    y = len(card)
    to_print = [
        [[],[],[],[],[]],
        [[],[],[],[],[]],
        [[],[]]
        ]
    for row in range(x):
        for column in range(y):
            to_print[0][row].append(card[row][column])
            to_print[1][row].append(card[column][row])
           
            if row == column:
                to_print[2][0].append(card[column][row])
                
            if row + column == 4:
                to_print[2][1].append(card[column][row])
    for element in to_print:
        for sub_element in element:
            if sum(sub_element) == 0:
                print(sub_element)
                print(*sub_element)
                return True
            
    return False        

   
card_1 = [[0,1,6,12,0],[16,20,0,18,25],[0,45,0,33,38],[51,48,55,53,46],[61,75,68,73,65]]

card_4 = [[0,1,6,12,0], 
          [16,20,0,0,25], 
          [0,45,0,33,38], 
          [51,0,55,53,46], 
          [0,75,68,73,65]]

print(check_card_elements(card_4))



