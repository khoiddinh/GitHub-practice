# app/silly_math.py (MAIN-side change idea)
def fancy_add(a, b):
    # MAIN: round down the sum
    return int(a + b)

if __name__ == "__main__":
    print(fancy_add(2, 3))
