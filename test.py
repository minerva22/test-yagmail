# Copied from example
import yagmail
import yaml

# read emailTo from command line
# https://docs.python.org/3.3/library/argparse.html
import argparse

parser = argparse.ArgumentParser(description='Send attachment to some emails.')
parser.add_argument('--emailTo', type=str, nargs='+', help='emails to send to', default='m.moawad@ffaprivatebank.com' )

args = parser.parse_args()

stream = open('credentials.yml', 'r')
credentials = yaml.load(stream)

yag = yagmail.SMTP(credentials['username'], credentials['password'])

contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.', 'attachment.txt']

print('emailTo: ',args.emailTo)
yag.send(args.emailTo, 'subject', contents)
