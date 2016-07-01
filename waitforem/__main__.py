from waitforem.lib import wait_for_server_socket, timeout, WaitTimeout
from argparse import ArgumentParser, HelpFormatter, ArgumentTypeError, REMAINDER
import os
import sys


def host_pairs(string):
    tokens = string.split(':')
    if not len(tokens) == 2:
        raise ArgumentTypeError('Socket must be specified as HOST:PORT')
    host = tokens[0]
    try:
        port = int(tokens[1])
    except ValueError:
        raise ArgumentTypeError('Invalid port number in socket argument: {}'.format(string))
    return (host, port)


def do_exec(args):
    if '--' in args[0:1]:
        args.pop(0)
    os.execlp(args[0], *args)


def main():
    parser = ArgumentParser(prog='waitforem',
                            formatter_class=lambda prog: HelpFormatter(prog, max_help_position=30))
    parser.add_argument('command', nargs=REMAINDER, help='Command to execute after waiting is done')
    parser.add_argument('-t', '--timeout', metavar='SECS', type=int, default=10,
                        help='Max number of seconds to wait before aborting with non-zero exit '
                             'code. Default: 10')
    parser.add_argument('-s', '--socket', action='append', metavar='H:P', type=host_pairs,
                        help='Network socket to wait for, specified as HOST:PORT')

    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit()

    args = parser.parse_args()

    if args.socket:
        host = port = None
        try:
            with timeout(args.timeout):
                for host, port in args.socket:
                    wait_for_server_socket(host, port)
            if len(args.command) > 0:
                do_exec(args.command)
        except WaitTimeout:
            sys.stderr.write("Timed out after {} seconds, waiting for {}:{}\n".format(
                args.timeout, host, port))

if __name__ == '__main__':
    main()
