#!/bin/bash

source .sessionkey
printf -v dayNum "%02d" $1
curl -b session=${sessionkey} https://adventofcode.com/2021/day/$1/input > day${dayNum}/day${dayNum}.in || exit
cp template.py day${dayNum}/day${dayNum}.py
cat day${dayNum}/day${dayNum}.in
