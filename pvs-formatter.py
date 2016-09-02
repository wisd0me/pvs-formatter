#!env python3
#written by wisd0me

import sys
import argparse

PVS_LOG_DIV = '<#~>'

def process(input, output, encoding):
    '''
    Formats PVS-Studio static analyzer log into human-readable form

    Input log format looks like this:
    Viva64-EM<#~>full<#~>LINE-NUM<#~>PATH<#~>error<#~>V631<#~>Consider inspecting the 'unlink' function call. Defining an absolute path to the file or directory is considered a poor style.<#~>false<#~>3<#~><#~> unlink(PIDFILE);<#~><#~>
    ... and so on
    '''

    with open(input, mode='r', encoding=encoding, errors='replace') as input, \
         open(output, mode='w', encoding=encoding) as output:
        for line in input:
            if line.find('Renew') !=  -1:
                continue

            tokens = line.split(PVS_LOG_DIV)
            if len(tokens) < 11:
                continue

            linefmt = '{}:{}\n{} <{}>: {}\ncode: {}\n\n'.format(
                tokens[3], tokens[2],
                tokens[4], tokens[5], tokens[6],
                tokens[10])
            output.write(linefmt)


# known arguments
argp = argparse.ArgumentParser(description='formats PVS-Studio log file into human-readable form')
argp.add_argument('-i', '--input', dest='input', required=True,
                  help='PVS-Studio log input file')
argp.add_argument('-o', '--output', dest='output',
                  help='output file; if omitted, \'.out\' suffix will be appended to input file name')
argp.add_argument('-e', '--encoding', dest='encoding', default='utf8',
                  help='file encoding; by default, utf8 is used')


if __name__ == '__main__':
    args = argp.parse_args()

    if (args.output == None):
        args.output = args.input + '.out'

    try:
        process(**dict(args._get_kwargs()))
    except OSError as errno:
        print("error: {}".format(errno))
    except:
        print("Unexpected error:", sys.exc_info()[0])
