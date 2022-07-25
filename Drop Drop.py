"""[Onsite Day1] Drop Drop"""

def main(grade):
    '''first impression'''
    summation = 2.00 - grade + 2.00
    if grade < 0:
        grade = 0
    elif grade > 4:
        grade = 4
    if grade < 1:
        print("I'm so sad.")
    elif grade < 2:
        print(("%.2f") %(summation))
    else:
        print("I'm so happy.")
main(float(input()))
