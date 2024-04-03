# Using arrays

# girlsNames = ['Evelyn', 'Jessica', 'Somto', 'Edith', 'Liza', 'Madonna', 'Waje', 'Tola', 'Aisha', 'Latifa']
# girlsAges = [17,16,17,18,16, 18,17,20,19,17]
# girlsHeights = [5.5,6.0,5.4,5.9,5.6,5.5,6.1,6.0,5.7,5.5]
# girlsScores = [80,85,70,60,76,66,87,95,50,49]


# boysNames = ['Chinedu', 'Liam', 'Wale', 'Gbenga', 'Abiola', 'Kola', 'Kunle', 'George', 'Thomas', 'Wesley']
# boysAges = [19,16,18,17,20,19,16,18,17,19]
# boysHeights = [5.7,5.9,5.8,6.1,5.9,5.5,6.1,5.4,5.8,5.7]
# boysScores = [74,87,75,68,66,78,87,98,54,60]

# print('Table for Girls')
# print('Name | Age | Height | Scores\n')

# for i in range(0,10):
#     print(f'{girlsNames[i]} | {girlsAges[i]} | {girlsHeights[i]} | {girlsScores[i]}')

# print('\nTable for Boys')
# print('Name | Age | Height | Scores\n')

# for i in range(0,10):
#     print(f'{boysNames[i]} | {boysAges[i]} | {boysHeights[i]} | {boysScores[i]}')


# # # Using dictionary


girls = {'Evelyn': [17, 5.5, 80], 'Jessica': [16, 6.0, 85], 'Somto': [17, 5.4, 70], 'Edith': [18, 5.9, 60], 'Liza': [16, 5.6, 76], 'Madonna': [18, 5.5, 66], 'Waje': [17, 6.1, 87], 'Tola': [20, 6.0, 95], 'Aisha': [19, 5.7, 50], 'Latifa': [17, 5.5, 49]}

boys = {'Chinedu': [19, 5.7, 74], 'Liam': [16, 7.5, 87], 'Wale': [18, 5.8, 75], 'Gbenga': [17, 6.1, 68], 'Abiola': [20, 5.9, 66], 'Kola': [19, 5.5, 78], 'Kunle': [16, 6.1, 87], 'George': [18, 5.4, 98], 'Thomas': [17, 5.8, 54], 'Wesley': [19, 5.7, 60]}

print("\nTable for Girls")
print('Name | Age | Height | Scores\n')

for femme in girls:
    print(f'{femme} | {girls[femme][0]} | {girls[femme][1]} | {girls[femme][2]}')

print("\nTable for Boys")
print('Name | Age | Height | Scores\n')

for homme in boys:
    print(f'{homme} | {boys[homme][0]} | {boys[homme][1]} | {boys[homme][2]}')