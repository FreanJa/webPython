import json
import ast
# def set_code(instructions):
#     source_code = ''
#     sub_code = []
#     for instruction in instructions:
#         if instruction[1][0] != 0:
#             sub_code.append(instruction)
#             continue
#
#
#     return source_code


# [
#     ["start",[[0]]],
#     ["repeat",[[0]],"\"20\""],
#     ["num",[[1,0]]],
#     ["",[[2,2]],"i","0"],
#     ["comment",[[1,1]],"Comment..."],
#     ["print",[[3,3]],"hello"]
# ]

# [
#     ["start",[[0]]],
#     ["repeat",[[0]],"20"],
#     ["num",[[1,0]]],
#     ["",[[2,2]],"i","0"],
#     ["comment",[[1,1]],"Comment..."],
#     ["print",[[3,3]],"hello"]
# ]

# [
#     ["repeat", [0], "8767589"],
#     ["print", [0], "hello"],
#     ["arithmetic", [1, 1], "abab"],
#     ["getInput", [2, 2]],
#     ["getInput", [1, 0]],
#     ["getInput", [1, 1]],
#     ["", [3, 3], "i", "0"]
# ]

def set_code(items):
    num = 0
    info = []
    codes = []
    final = []
    # items = json.load(items)
    # items = ast.listeral_eval(items)

    for item in items:
        print(type(item))
        # print(type(items))
        print(item)
        print("=============")
        id = item[0]
        indentation = item[1]
        param = item[2:]
        print("===== %d ====="%(num))

        print(id)
        print(indentation)
        print(param)
        code = translate(id, param)
        codes.append([num, code, indentation])
        num += 1
    print(codes)
    order = []
    for code in codes:
        if code[2][0] == 0:
            order.append(code)
            continue
        if code[2][0] == 1:
            # order.insert()
            index = code[2][1]
            pos = -1

            for i in range(len(order)):
                if index == order[i][0]:
                    pos = i
                    continue
                # if pos != -1 & order[i][1] == index:
                #     pos += 1
                # elif pos != -1:
                #     break
                # print(len(order[i]))
                if pos != -1 & len(order[i][2]) == 2:
                    print('run')
                    print(order[i][2][1])
                    if order[i][2][1] == index:
                        print('increase')
                        pos += 1
                    else:
                        break

            if pos == -1:
                return 'error'
            order.insert(pos+1, code)
    print(order)
    text = ''
    for code in order:
        for i in range(code[2][0]):
            text = text + '\t'
        text = text + code[1]

    print(text)

    # code = ''
    # if id == 'print':
    #     code = ''
    return text


def translate(id, param):
    code = ''
    if id == 'repeat':
        if len(param) != 1:
            return 'error'
        code = 'for __count in range (' + param[0] + '):\n'
    elif id == 'print':
        code = 'print('
        for p in param:
            code = code + p
        code = code + ')\n'
    elif id == 'comment':
        code = '#'
        for p in param:
            code = code + p
        code = code + "\n"
    elif id == 'input':
        code = 'input()\n'
    elif id == 'ask':
        code = 'input("' + param[0] + '")\n'
    elif id == 'set':
        code = param[0] + '=' + param[1] + '\n'
    elif id == 'increase':
        code = param[0] + '+=' + param[1] + '\n'
    return code





# [
#     ["print",
#      [[0],"hello"]
#      ],
#     ["count",
#      [[0],"i","Hello"]
#      ],
#     ["",
#      [[1,1],"i","0"]
#      ]
# ]

if __name__ == "__main__":
    # items = [["set",[0],"i","0"],["repeat",[0],"20"],["print",[1,1],"i"],["increase",[1,1],"i","1"]]
    items = [["set",[0],"i","-10"],["repeat",[0],"30"],["print",[1,1],"d"],["increase",[1,1],"i","1"]]
    set_code(items)
    # i = 0
    # for __count in range(20):
    #     i += 1
    #     print(i)