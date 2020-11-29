def greet (lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
nam= input('what is your name: ')
print('language option: es fr en')
lan = input('Input language choise:')
print(greet(lan),nam)
