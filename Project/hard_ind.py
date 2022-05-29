#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите слово: ")
    count = 0
    Max = 0
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
            if count > Max:
                Max = count
        else:
            count = 1
    print(Max)
