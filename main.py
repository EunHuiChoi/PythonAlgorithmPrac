# Calculate total score of three students
# input : weight of components, scores of students per components

component_weight_dict = {'Midterm': .20, 'Final': .20, 'Practice': .60}  # total weight = 100
student_score_dict = {
    'Tom': {'Midterm': 100, 'Final': 100, 'Practice': 50, 'Total': 0},
    'Lisa': {'Midterm': 50, 'Final': 50, 'Practice': 100, 'Total': 0},
    'Brad': {'Midterm': 100, 'Final': 100, 'Practice': 50, 'Total': 0}
}

# calculating total scores
for score_dict_key in student_score_dict:
    for score_key in student_score_dict.get(score_dict_key):
        if score_key != 'Total':
            student_score_dict[score_dict_key]['Total'] += \
                student_score_dict[score_dict_key][score_key]*component_weight_dict[score_key]

print(student_score_dict)