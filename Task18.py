# n = 6
# steps = str('u','u','d','d','u','u')

def valleys (n, steps):
    level = 0
    valley_num = 0

    for step in steps:
        if step == 'u':
            level += 1
            if level == 0:
                valley_num += 1
        else step == 'd':
            level -= 1
return (valley_num)