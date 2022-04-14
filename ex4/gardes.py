# -*- coding: utf-8 -*-
"""
Student: Lior Silberman
ID: 316456623
Assignment no. 2
Program: grades.py
"""

def read_files(id_name, dic_grades):
    '''
    read files and return dictioneries
    '''  
    with open("students.txt") as f:
        for line in f:
            line_parts = line.split()
            if len(line_parts[0]) != 9:
                return "Illegal ID length in ID-NAME file"
            if len(line_parts) == 1:
                return "Illegal name in ID-NAME file"
            id_name[line_parts[0]] = " ".join(line_parts[1:])


    with open("grades.txt") as f:
         for line in f:
            line_parts = line.split()
            if len(line_parts[0]) != 9:
                return "Illegal ID length in ID-GRADE file"
            if len(line_parts) == 1:
                return "Illegal grades in ID-GRADE file"
            grades = [float(a) for a in line_parts[1:]]
            dic_grades[line_parts[0]] = (grades, sum(grades)/len(grades))
            
    return ""
   
    

def most_common_grades(dic_grades):
    '''
    return list of most comman grades.
    '''
    all_grades = []
    grades_counter = {}
    for grades, avg in dic_grades.values():
        for g in grades:
            all_grades.append(int(g))
    
    for g in all_grades:
        grades_counter[g] = all_grades.count(g)
        
    highest_grade_counter = 0
    for k, v in grades_counter.items():
        if v >= highest_grade_counter:
            highest_grade_counter = v
            
    highest_grades = []
    for k, v in grades_counter.items():
        if v == highest_grade_counter:
            highest_grades.append(k)
            
    print('Most common grades: ', highest_grades)
    
def get_commom_elements(students_grades):
    '''
    return list of more then once in lists elements
    '''
    common_elements = set()
    
    for grades in range(len(students_grades)-1):
        for common_grades in range(1, len(students_grades)):
            if grades == common_grades:
                continue
            x = set(students_grades[grades]) & set(students_grades[common_grades])
            common_elements |= x
    common_grades = [int(i) for i in common_elements]
    
    return common_grades
    


def main():
    
    id_name = {}
    dic_grades = {}
     
    # read files and check legal input files
    not_legal = read_files(id_name, dic_grades)
    if not_legal:
        print(not_legal)
        return
    
    # check match ID's between files
    shared_keys = set(id_name.keys()) | set(dic_grades.keys())
    if len(shared_keys) != len(set(id_name.keys())):
        print("ID's are not match between files")
        return

    # i 
    for _id, _grades in sorted(dic_grades.items(), key=lambda cmp: cmp[1][1], reverse=True):
        print(id_name[_id], _grades[1])
   
    # ii
    most_common_grades(dic_grades)
    
    # iii
    students_grades = []
    for grades, avg in dic_grades.values():
        students_grades.append(grades)
    print('Grades that more than one student got:\n', get_commom_elements(students_grades))
        
main()