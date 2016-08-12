## DailyProgrammer Task 276 Intermediate. ##
#Author:    Ryan Wagner
#Purpose:   Write a function (key) that can perform multiple tasks
#           on data, including key summations, key/value pairing,
#           and key/value nubbing.
#           Correct output resembles reddit dailyprogrammer output.

def key(elements, keys, function):
    if function == 'histogram':
        return histogram(elements)
    elif function == 'sum':
        return sum(elements, keys)
    else:
        return nub(elements, keys)

def histogram(elements):
    out = {}
    for e in elements:
        out[e] = out.get(e, 0) + 1
    return out

def sum(elements, keys):
    out = {}
    for i in range(len(elements)):
        out[keys[i]] = out.get(keys[i], 0) + elements[i]
    return out

def nub(elements, keys):
    out = {}
    for i in range(len(elements)):
        if keys[i] not in out:
            out[keys[i]] = elements[i]
    return out


elements = [5, 3, 5, 2, 2, 9, 7, 0, 7, 5, 9, 2, 9, 1, 9, 9, 6, 6, 8, 5, 1, 1, 4, 8, 5, 0, 3, 5, 8, 2, 3, 8, 3, 4, 6, 4, 9, 3, 4, 3, 4, 5, 9, 9, 9, 7, 7, 1, 9, 3, 4, 6, 6, 8, 8, 0, 4, 0, 6, 3, 2, 6, 3, 2, 3, 5, 7, 4, 2, 6, 7, 3, 9, 5, 7, 8, 9, 5, 6, 5, 6, 8, 3, 1, 8, 4, 6, 5, 6, 4, 8, 9, 5, 7, 8, 4, 4, 9, 2, 6, 10]
list_keys = [('a', 14), ('b', 21), ('c', 82), ('d', 85), ('a', 54), ('b', 96), ('c', 9, ), ('d', 61), ('a', 43), ('b', 49), ('c', 16), ('d', 34), ('a', 73), ('b', 59), ('c', 36), ('d', 24), ('a', 45), ('b', 89), ('c', 77), ('d', 68)]
els2 = [i[1] for i in list_keys] 
keys = [i[0] for i in list_keys] 

print(key(elements, None, 'histogram'))
print(key(els2, keys, 'sum'))
print(key(els2, keys, 'nub'))
