def print_message(message):
    print('\t'*4, '_'*len(message))
    print('\t'*3, f'  < {message} > ')
    print('\t'*4, '-'*len(message))
    print('''\t\t\t  /
     /\__/\  /
    ( ○.○ )
     > ^ <
    ''')



if __name__ == '__main__':
    message = input('Enter your message here: ')
    print_message(message)
