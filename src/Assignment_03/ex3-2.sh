#!/bin/sh

read num_0 op num_1

case $op in
    "+")
	    echo $(expr $num_0 + $num_1);;
	"-")
	    echo $(expr $num_0 - $num_1);;
esac
