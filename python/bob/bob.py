#
# Skeleton file for the Python "Bob" exercise.
#

def hey(what):    

    #check for no string
    if what.strip() == '':
        return 'Fine. Be that way!'
            
    if what.upper() == what and not what.lower() == what:
        return 'Woah, chill out!'
            
    if what.endswith('?'):
        return 'Sure.'

    return 'Whatever.'
