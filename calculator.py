def readNumber(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta *= 0.1
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index

def readMulti(line,index):
    token = {'type': 'MULTI'}
    return token, index + 1

def readDivi(line,index):
    token = {'type': 'DIVI'}
    return token, index + 1


def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1


def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readMulti(line, index)
        elif line[index] == '/':
            (token, index) = readDivi(line, index)
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    return tokens


def  evaluate_multi_and_divi(tokens):
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'MULTI':
           tokens[index -1]['number']= tokens[index - 1]['number']*tokens[index + 1]['number']
           del tokens[index:index+2]
           index -=1
        elif tokens[index]['type'] == 'DIVI':
            tokens[index -1]['number']= tokens[index - 1]['number']/tokens[index + 1]['number']
            del tokens[index:index+2]
            index -=1
        index += 1
    return tokens
        
def  evaluate_pulus_and_minus(tokens):
     answer = 0
     index = 1
     while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':            
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print 'Invalid syntax'
        index += 1
     return answer

def evaluate(tokens):
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token

    tokens2 = evaluate_multi_and_divi(tokens)
    answer =  evaluate_pulus_and_minus(tokens2)

    return answer


while True:
    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print "answer = %f\n" % answer
