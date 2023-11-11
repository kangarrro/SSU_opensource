#!/bin/bash

echo "리눅스가 재미있나요?(y/n)"
read ans

case $ans in
    Y | y | Yes | yes)
        echo "Yes";;
    N | n | No | no)
        echo "NO";;
    *)
        echo "yes or no 로 입력해주세요";;
esac