import sys

def day_name(Num):
    if Num == 1:
        return 'Monday'
    if Num == 2:
        return 'Tuesday'
    if Num == 3:
        return 'Wednesday'
    if Num == 4:
        return 'Thursday'
    if Num == 5:
        return 'Friday'
    if Num == 6:
        return 'Saturday'
    if Num == 0:
        return 'Sunday'


def day_num(Name):
    if Name == 'Monday':
        return 1
    if Name == 'Tuesday':
        return 2
    if Name == 'Wednesday':
        return 3
    if Name == 'Thursday':
        return 4
    if Name == 'Friday':
        return 5
    if Name == 'Saturday':
        return 6
    if Name == 'Sunday':
        return 0
    
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
def test_suite():
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num('Thursday')) == 'Thursday')
    test(day_num("Halloween") == None)
    
test_suite()

