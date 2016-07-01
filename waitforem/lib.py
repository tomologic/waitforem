#!/usr/bin/env python
from contextlib import contextmanager
from time import sleep
import errno
import os
import signal
import socket


def wait_for_server_socket(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        result = sock.connect_ex((host, port))
        if result == 0:
            break
        else:
            sleep(0.1)


@contextmanager
def timeout(seconds):
    def timeout_handler(*args):
        raise WaitTimeout(os.strerror(errno.ETIME))
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


class WaitTimeout(Exception):
    pass
