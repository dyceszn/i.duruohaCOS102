# Fuctions Catalogue

def collectWaec(dept): # Function to collect WAEC RESULT
    if dept == 'Computer Science':
        # Math, English, Physics, Chemistry, Biology
        grade1 = input('Enter grade for Math:')
        grade2 = input('Enter grade for English:')
        grade3 = input('Enter grade for Physics:')
        grade4 = input('Enter grade for Chemistry:')
        grade5 = input('Enter grade for Biology:')
        waec_result = [grade1, grade2, grade3, grade4, grade5]
        return waec_result

    elif dept == 'Mass Communication':
        grade1 = input('Enter grade for Subject 1:')
        grade2 = input('Enter grade for Subject 2:')
        grade3 = input('Enter grade for Subject 3:')
        grade4 = input('Enter grade for Subject 4:')
        grade5 = input('Enter grade for Subject 5:')
        waec_result = [grade1, grade2, grade3, grade4, grade5]
        return waec_result
    else:
        print('Invalid Input')

def validateWaec(arr): # Function to validate WAEC RESULT
    waec_status = False
    for element in arr:
        if element == 'A' or element == 'B' or element == 'C':
            waec_status = True
        else:
            waec_status = False
            break
    return waec_status

# Catalogue ends here

# MAIN CODE

admitted = []
not_admitted = []

name = input('Enter you name:')
dept = input('Enter your department of choice:')
score = int(input('Enter your Jamb Score:'))
interview = input ('PASS or FAIL:')
waec_result = collectWaec(dept)
waec_status = validateWaec(waec_result)

if score >= 250 and waec_status and interview == 'PASS':
    print(f'Congratulations {name}! You have been admitted into{dept}.')
    student_arr = [name, score, waec_result, interview]
    admitted.append(student_arr)
else:
    print('I am sorry to inform you...')
    student_arr = [name, score, waec_result, interview]
    not_admitted.append(student_arr)

# print(admitted)
# print(not_admitted)




