#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите слово: ")
    k = 0
    for i in range(0, len(s) // 2):
       if s[i] == s[len(s) - 1 - i]:
           k += 1
    print(s)
    if k == len(s) // 2:
        print("Слово палиндром")
    else:
        print("Слово не палиндром")

