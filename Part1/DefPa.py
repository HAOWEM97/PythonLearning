def greet (lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

print('language option: es fr en')
lan = input('Input language choise:')
greet(lan)
