FIZZ = 3
BUZZ = 5
FIZZBUZZ = FIZZ * BUZZ
#in add42
def main():
    for i in range(1, 101):
        if i % FIZZBUZZ == 0:
            print("Fizzbuzz")
        elif i % FIZZ == 0:
            print("Fizz")
        elif i % BUZZ == 0:
            print("Buzz")
        elif i == 42:
            print("Answer to the Ultimate Question of Life, the Universe, and Everything")
        else:
            print(i)
        



if __name__ == '__main__':
    main()
