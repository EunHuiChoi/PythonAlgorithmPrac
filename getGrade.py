
def total_score_calculator():

def grader():


component_weight_dict = {'Midterm': .20, 'Final': .20, 'Practice': .60}
student_score_dict = {}

student_score_dict_total = total_score_calculator(student_score_dict, component_weight_dict)
student_score_dict_grade = grader(student_score_dict_total)

print(student_score_dict_grade)