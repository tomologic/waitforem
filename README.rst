Wait For Them *(Wait for 'em)*
==============================

A service startup synchronizer for network services, which delays the execution of a command until one or more dependent network services are available on some host(s).

The script will try to connect to TCP network ports at a set of host and once it succeeds it will either exit with a return value or zero, or exec_ into a specified program supplied as an argument to the script.

This is a pure python implementation in the same vein as the shell script wait-for-it.sh_.

It was created to solve startup order orchestration between dependent services, for when a service needs one or more *other* network based services before it can start, such as a database and / or an MQ broker.

Usage
-----
::

  usage: waitforem [-h] [-t SECS] -s H:P [-s H:P] [command...]

  positional arguments:
    command                  Command to execute after waiting is done

  optional arguments:
    -h, --help               show this help message and exit
    -t, --timeout SECS       Max number of seconds to wait before aborting with
                             non-zero exit code. Default: 10
    -s, --socket H:P         Network socket to wait for, specified as HOST:PORT


Basics
^^^^^^
Wait for the SSH service to become available on host *foo* at port *22*::

  python -m waitforem --socket foo:22

or alternatively using the wrapper script installed as part of the python package::

  waitforem --socket foo:22

The script waits for the specified socket to open for a configurable amount of time (default 10 seconds) before aborting with a non-zero exit code. If connection establishment is possible within the timeout period, then the script exits with exit code zero. 

Chained command
^^^^^^^^^^^^^^^
It is possible to provide a command to execute on successful socket connection.
As mentioned in the introduction, the script will then exec_ into that command, such that it replaces the entire python interpreter and the waitforem script. ::

  waitforem --socket mq:5672 /usr/src/app/run_uwsgi.sh

Any flag or argument following the wrapped command will be fowarded as-is to the wrapped command. ::

  SVC=service waitforem --socket mq:5672 sh -c 'echo $SVC is up'
  => service is up

Standard input will also be passed on::

  waitforem --socket mq:5672 cat <<EOS
  from stdin!
  EOS
  => from stdin!

Wait for several services
^^^^^^^^^^^^^^^^^^^^^^^^^
It is possible to specify the *socket* argument several times, in order to wait for a set of dependent services to become available. For example, waiting for both an MQ broker and a database to come up. ::

  waitforem -s mq:5672 -s db:5432 /opt/myapp

Why another one?
----------------
We're using very stripped OS instances, including `alpine linux`_, with pretty much only base python installed. The shell script variant doesn't work on alpine so we rolled our own as a pip package, since we install such packages as part of our pipeline.

.. _wait-for-it.sh: https://github.com/vishnubob/wait-for-it
.. _exec: http://man7.org/linux/man-pages/man3/exec.3.html
.. _alpine linux: http://www.alpinelinux.org/
