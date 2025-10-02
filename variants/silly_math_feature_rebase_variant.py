# app/silly_math.py (FEATURE-REBASE variant)
def fancy_add(a, b):
    # REBASE branch: return string with an emoji
    return f"{a + b}✨"

if __name__ == "__main__":
    print(fancy_add(2, 3))
