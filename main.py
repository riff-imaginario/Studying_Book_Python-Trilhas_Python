#!/usr/bin/env python3.*
# -*- coding: UTF-8 -*-

'''
Um jogo da velha simples.
'''

from curses import initscr, wrapper
from random import randint

def main(stdscr):
    stdscr.clear()
    stdscr.border()
    boas_vindas()
    stdscr.refresh()

    while True:
        pass

def boas_vindas(stdscr):
    stdscr.addstr(1, 1, "Bem-vindo ao Jogo da Velha.")
    stdscr.addstr(2, 1, "Pressione q para sair ou h para obter ajuda.")
    stdscr.addstr(16, 1, "Desenvolvido por: L. S. Nogueira.")
    stdscr.addstr(17, 1, "Licensa Nova BSD.")

if __name__ == '__main__':
    initscr()
    wrapper(main)