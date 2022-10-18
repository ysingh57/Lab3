#!/usr/bin/env python3

def enter_a_name_for_file():

    f = open("name.txt" , "w+")
    f.write("Yuvraj Singh")
    f.close()

if __name__ ==" __main__":
    enter_a_name_for_file()
