def parse_json():
    res = dict()
    temp = []
    temp_str = ''
    opened = False
    global pos
    for position in range(pos, len(result)):
        if position != pos:
            continue
        pos += 1
        if result[position] == '"':
            if opened:
                temp.append(temp_str)
                temp_str = ''
                opened = False
            else:
                opened = True
        elif result[position] == '}':
            return res
        elif (result[position] == ':' or result[position] == ',' or result[position] == ' ') and not opened:
            continue
        elif result[position] == '{':
            temp.append(parse_json())
        else:
            temp_str += result[position]
        if len(temp) % 2 == 0 and len(temp) >= 2:
            res.update({str(temp[-2]): temp[-1]})
    return res


def print_tabs(tabs):
    global f_out
    while tabs > 0:
        f_out.write(' ')
        tabs -= 1


def print_dict(tabs, to_print):
    global f_out
    global TABSIZE
    for key, value in to_print.items():
        if type(value) is str:
            print_tabs(tabs)
            f_out.write(key + ':' + ' "' + value + '"\n')
        else:
            print_tabs(tabs)
            f_out.write(key + ' {\n')
            print_dict(tabs + TABSIZE, value)
            print_tabs(tabs)
            f_out.write('}\n')


f_in = open("input", "r")
f_out = open("output", "w")
pos = 1
TABSIZE = 4
result = ''

for x in f_in:
    result += x.strip()

json_doc = parse_json()

print_dict(0, json_doc)
