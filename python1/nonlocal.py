#!/usr/bin/python3

def fun_out():
    a = 4
    def fun_in():
        nonlocal a
        a += 1
        print ("in:",a)
    fun_in()
    print ("out:",a)
fun_out()
