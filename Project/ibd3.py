#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите слово: ")

    for i in range(0, len(s)):
        if s[i] == 'о':
            s = s.replace('о', '', 1)
            break
    for i in range(len(s) - 1, 0, -1):
        if s[i] == 'л':
            s = s.replace('л', '', 1)
            break
    print(s)
