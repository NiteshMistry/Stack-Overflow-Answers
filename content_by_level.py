str1 = "(a(b(c)d)(e(f)g)hi)"

def content_by_level(str1, l):
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
    return level_dict[l]

print(content_by_level(str1,0)) # ['']
print(content_by_level(str1,1)) # ['a', 'hi']
print(content_by_level(str1,2)) # ['b', 'd', 'e', 'g']
print(content_by_level(str1,3)) # ['c', 'f']


            