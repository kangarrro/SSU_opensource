#!/bin/bash

param="$1"
echo "프로그램을 시작합니다"

func() {
    echo "함수안으로 들어왔음"
    if [ "$param" = "-l" ]; then
        ls -l
    else
        ls
    fi
}

func
echo "프로그램을 종료합니다."
