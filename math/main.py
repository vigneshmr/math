import generator as gen

from termcolor import colored


def train():
    print '''

    Math trainer:

    There will be 10 question in each category. Enter the answers directly:

    '''
    title('Addition')
    for i in xrange(10):
        a, b = gen.addition()
        ask_question(i, a, b, '+')

    title('Subtraction')
    for i in xrange(10):
        a, b = gen.subtraction()
        ask_question(i, a, b, '-')

    title('Multiplication')
    for i in xrange(10):
        a, b = gen.multiplication()
        ask_question(i, a, b, 'x')

    title('Squaring')
    for i in xrange(10):
        a = gen.squaring()
        ask_question(i, a, a, '**')


def ask_question(idx, a, b, op):
    print ''
    act_res_str = raw_input('{}). {} {} {} = '.format(idx + 1, a, op, b))
    act_res = str_to_int(act_res_str)
    if op == '+':
        exp_res = a + b
    elif op == '-':
        exp_res = a - b
    elif op == 'x':
        exp_res = a * b
    elif op == '**':
        exp_res = a * b
    else:
        raise 'invalid operation'

    if act_res != exp_res:
        print colored('Incorrect answer! Expected = {}'.format(exp_res), 'red')


def title(str):
    print ''
    print ''   
    print colored(str, 'green')


def str_to_int(str):
    try:
        i = int(str)
    except:
        return 0
    return i


# Entry point
if __name__ == '__main__':
    train()
