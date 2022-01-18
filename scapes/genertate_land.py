# adapted from SuperHi's Intro to Python Coursework
import random 

from termcolor import colored
from noise import pnoise2

def generate_land(rows=10, cols=10, noise_level=30):
    
    data = ["🌱","🌼", "🌺", "🍄", "🌻", "🌸", "🌿", "🌿",  "🌸", "🌻", "🍄", "🌺", "🌼", "🌱"]
    seed = random.randint(0, 100)
    land = ""


    print(f"genertate a landscape which is {cols} by {rows}")

    for row in range(rows):
        for col in range (cols):
            n = pnoise2(row / rows, col / cols, base = seed, octaves=5)
            n *= noise_level
            n = round(n)
            n = n % len(data)

            land += data[n]
        land += "\n"

    print("generation done : )")
    return land

def ask_for_number(question):

    tries = 0

    while tries  < 3 :
        answer = input(colored(question, "green"))

        if answer == "quit" :
            quit()

        elif answer.isnumeric():
            return int(answer)

        else:
            print("Oops this didn't make sense : (")
            tries += 1
    print(colored("this is no longer fun.... goodbye", "red"))
    quit()
        
if __name__ == "__main__" : 
    
    cols = ask_for_number("How many cols? ")
    rows = ask_for_number("how many rows? ")

    output = generate_land(rows, cols)

    print(output)