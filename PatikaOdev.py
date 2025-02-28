#Soru-1
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Örnek kullanım:
input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output_list = flatten(input_list)
print(output_list)

#Soru-2
def reverse_nested(lst):
    reversed_list = []
    for item in lst:
        if isinstance(item, list):
            reversed_list.append(reverse_nested(item))
        else:
            reversed_list.append(item)
    return list(reversed(reversed_list))

# Örnek kullanım:
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse_nested(input_list)
print(output_list)