
def get_summ(one, two, delimiter='&'):
    one_str = str(one)
    two_str = str(two)
    together = one_str + delimiter + two_str
    return together

name1 = 'learn'
name2 = 'python'
s = get_summ(name1, name2, "+")
print(s.capitalize())