#!/bin/bash
echo "This is a script, Hello!"

greeting="This is a script, hello!"
echo $greeting thanks for joining us!
echo "$greeting, you owe me \$20 \n"

echo Machine Type: $MACHTYPE
echo Hostname: $HOSTNAME
echo Working Dir: $PWD
echo Session Length: $SECONDS
echo Home DIR: $HOME

a=$(ip a | grep 'noprefixroute ens192'| awk '{print $2}')
echo My IP is $a
