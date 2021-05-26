import re
from argparse import ArgumentParser

def getParse():
    # setup arguments
    parser = ArgumentParser()
    parser.add_argument('-f', '--path', dest='path', help='Enter path to TEXT file.')
    parser.add_argument('-m', '--mails', dest='mails', help='get mails.', action='store_true')
    parser.add_argument('-n', '--numbers', dest='numbers', help='get phone numbers.', action='store_true')
    # check arguments
    arguments = parser.parse_args()
    if not arguments.path:
        parser.error('[!] Specify INPUT file --help for more information')
    elif not arguments.mails and not arguments.numbers:
        parser.error('[!] Specify OUTPUT method --help for more information')
    else:
        with open(arguments.path, 'r') as file:
            data = file.read()
            f = open("output.txt","w")
            out = ""
            if arguments.numbers:
                phones = getPhones(data)
                for phone in phones:
                    num = ''.join(phone) + "\n"
                    out += num
            if arguments.mails:
                mails = getMails(data)
                for mail in mails:
                    out += mail + "\n"
            f.write(out)
            
def getMails(txt):
    # Regex email object.
    mailReg = re.compile(r'''
    [a-zA-z0-9_.+]+    # name part
    @                  # @ symbol part
    [a-zA-z0-9_.+]+    # domain part 
    ''',re.VERBOSE)
    return mailReg.findall(txt)

def getPhones(txt):
    # Regex phone number object.
    phoneReg = re.compile(r'''
    ((\d\d)|(\d\d\d))?   # house line or mobile phone
    (\s|-)?              # follow by space or dash
    (\d\d\d\d\d\d\d)    # last digits
    ''',re.VERBOSE)
    return phoneReg.findall(txt)

if __name__ == "__main__":
    getParse()
