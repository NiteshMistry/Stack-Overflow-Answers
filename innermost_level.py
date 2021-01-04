# Question: https://stackoverflow.com/questions/56753160/how-to-extract-string-within-the-innermost-parenthesis-in-the-multiple-parenthes/

str1 = "(a(b(c)d)(e(f)g)hi)"
str2 = "(((x12 & x20) & x05) | x02) | ((x12 & x13)) | (x13 | x20)"

def innermost_level(str1):
    level_dict = {}
    level = 0
    level_char = ''
    for s in str1:
        if s == '(':
            if level not in level_dict:
                level_dict[level] = [level_char]
            elif level_char != '':
                level_dict[level].append(level_char)
            level_char = ''
            level += 1
        elif s == ')':
            if level not in level_dict:
                level_dict[level] = [level_char]
            elif level_char != '':
                level_dict[level].append(level_char)
            level_char = ''
            level -= 1
        else:
            level_char += s
    print(level_dict) # {0: [''], 1: ['a', 'hi'], 2: ['b', 'd', 'e', 'g'], 3: ['c', 'f']}
    max_level = max(level_dict.keys())
    return level_dict[max_level]

print(innermost_level(str1)) # ['c', 'f']
print(innermost_level(str2)) # ['x12 & x20']

            