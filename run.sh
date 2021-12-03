#!/bin/bash

printf -v dayNum "%02d" $1
cat day${dayNum}/day${dayNum}.in | python3 day${dayNum}/day${dayNum}.py
