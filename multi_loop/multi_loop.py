import sys


def build_statement(loop_list, current_num, spaces):
    '''
    recursive function for build for statement.
    Args:
        loop_list (list): list of basic for statement
        currnt_num (int): current position of processing
        spaces (int): spaces for indentation
    Returns:
        for_statement (str): for statement
    '''
    indentation_list = [' ' * current_num *
                        spaces, ' ' * (current_num + 1) * spaces]
    if (current_num >= len(loop_list) - 1):
        return f'{loop_list[current_num]}\n{indentation_list[0]}{{\n{indentation_list[0]}}}'
    return f'{loop_list[current_num]}\n{indentation_list[0]}{{\n{indentation_list[1]}{build_statement(loop_list, current_num + 1, spaces)}\n{indentation_list[0]}}}'


def multi_loop(loop_num, loop_initializer_type, cond, loop_statement_type, number_of_spaces=4):
    '''
    print nested loop code in C++
    Default number of spaces = 4, since that's default setting in my Xcode env.
    If you like 2 spaces you could use 2.
    Args:
        loop_num (int): number of loops
        loop_initializer_type (str): type of initializer, [z | i] stands for [zero | inherited]
        cond (str): condition of loop statement
        loop_statement_type (str): type of loop statement, [i | d] stands for [increment | decrement]
        number_of_spaces (int): spaces for indentation, default = 4
    Returns:
        None
    '''
    if loop_initializer_type == 'i':
        loop_initializer_list = [
            'int i1 = 0'] + [f'int i{i} = i{i - 1}' for i in range(2, loop_num + 1)]
    elif loop_initializer_type == 'z':
        loop_initializer_list = [
            f'int i{i} = 0' for i in range(1, loop_num + 1)]
    else:
        print('wrong loop initializer type!')
        return

    cond_list = [f'i{i} {cond}' for i in range(1, loop_num + 1)]

    if loop_statement_type == 'i':
        loop_statement_list = [f'++i{i}' for i in range(1, loop_num + 1)]
    elif loop_statement_type == 'd':
        loop_statement_list = [f'--i{i}' for i in range(1, loop_num + 1)]
    else:
        print('wrong loop statement type!')
        return

    for_statement_list = [f'for ({loop_initializer}; {cond_str}; {loop_statement})' for loop_initializer,
                          cond_str, loop_statement in zip(loop_initializer_list, cond_list, loop_statement_list)]
    print(build_statement(for_statement_list, 0, number_of_spaces))


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('missing params')
        sys.exit(1)

    loop_num = int(sys.argv[1])
    loop_initializer_type = sys.argv[2]
    cond = sys.argv[3]
    loop_statement_type = sys.argv[4]
    number_of_spaces = 4
    if len(sys.argv) is 6:
        number_of_spaces = sys.argv[5]

    multi_loop(loop_num, loop_initializer_type, cond,
               loop_statement_type, number_of_spaces)
