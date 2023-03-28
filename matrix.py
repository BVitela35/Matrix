import os
import random
os.system("color 02")
espacio = "     "
lineac = ""
def calculate():
    for i in range(4):
        lineap1 = str(random.randint(0, 1))
        lineap2 = str(random.randint(0, 1))
        lineap3 = str(random.randint(0, 1))
        lineap4 = str(random.randint(0, 1))
        lineap5 = str(random.randint(0, 1))
        lineap6 = str(random.randint(0, 1))
        lineap7 = str(random.randint(0, 1))
        lineap8 = str(random.randint(0, 1))
        print(lineap1 + lineap2 + lineap3 + lineap4 + lineap5
                + lineap6 + lineap7 + lineap8 + espacio + lineap1 + lineap2 + lineap3 + lineap4 + lineap5
                + lineap6 + lineap7 + lineap8 + espacio + lineap1 + lineap2 + lineap3 + lineap4 + lineap5
                + lineap6 + lineap7 + lineap8 + espacio + lineap1 + lineap2 + lineap3 + lineap4 + lineap5
                + lineap6 + lineap7 + lineap8 + espacio + lineap1 + lineap2 + lineap3 + lineap4 + lineap5
                + lineap6 + lineap7 + lineap8 + espacio + lineap1 + lineap2 + lineap3 + lineap4 + lineap5
                + lineap6 + lineap7 + lineap8 + espacio + lineap1 + lineap2 + lineap3 + lineap4 + lineap5
                + lineap6 + lineap7 + lineap8 + espacio + lineap1 + lineap2 + lineap3 + lineap4 + lineap5
                + lineap6 + lineap7 + lineap8 + espacio + lineap1 + lineap2 + lineap3 + lineap4 + lineap5
                + lineap6 + lineap7 + lineap8 + espacio + lineap1 + lineap2 + lineap3 + lineap4 + lineap5
                + lineap6 + lineap7 + lineap8 + espacio + lineap1 + lineap2 + lineap3 + lineap4 + lineap5
                + lineap6 + lineap7 + lineap8 + espacio)
    print("\n")

while True:
    calculate()
