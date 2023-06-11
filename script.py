COMMANDS = {
    'hello': greeting_func,
    'add': add_func,
    'change': change_func,
    'phone': phone_func,
    'show-all': show_all_func
}

MEMORY = {}

def print_help():
    message = "You can only input commands:\nhello\nadd\nphone\nshow-all\nchange\nIf you want exit from programm - input: [good bay] or [exit] or [close]\nFor work with propram, you must enter in the format:\ncommand [enter] | command[hello, show-all]\ncommand [space] name [enter] | command[phone]\ncommand [space] name [space] phone number | command[add, change]"
    return message


def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
        except (KeyError, ValueError, IndexError) as err:
            result = f'Error input data - {err} try again'
        return result
    return inner


def greeting_func(*args):
    return "How can I help you?"


@input_error
def add_func(*args):
    key = MEMORY.get(args[0][1], '')
    if key == '':
        MEMORY[args[0][1]] = args[0][2]
        result = 'User added'
    else:
        result = 'User in memory'
    return result


@input_error
def change_func(*args):
    key = MEMORY.get(args[0][1], '')
    if key:
        MEMORY[args[0][1]] = args[0][2]
        result = 'Number is change'
    else:
        result = 'User not find'
    return result


@input_error
def phone_func(*args):
    if args[0][1] in MEMORY:
        result = MEMORY[args[0][1]]
    else:
        result = 'User not find'
    return result


def show_all_func(*args):
    report = ''
    if not MEMORY:
        result = 'Memory is empty'
    else:
        for k, v in MEMORY.items():
            report += (f'{k} {v}' + '\n')
        result = report
    return result


def get_handler(command):
    return COMMANDS[command]


def main():

    while True:
        input_text = input('...').casefold()
        if input_text == '':
            print(print_help())
            continue
        elif input_text in ['exit', 'close', 'good bay']:
            break

        else:
            item_text = input_text.split(' ')
            if item_text[0] in COMMANDS:
                func_run = get_handler(item_text[0])
                result_func = func_run(item_text)
                if result_func:
                   print(result_func)
                   continue
            else:
                print(print_help())
                continue

    print('Good bay!')


if __name__ == '__main__':
    main()

