from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

#Note: Speak by a knave is always false so therefore should be using Not for what they says

#Possible Statement for A B C
#A = Knight if A != Knave
#B = Knight if B != Knave
#C = Knight if C != Knave
XORA = Biconditional(AKnight, Not(AKnave))
XORB = Biconditional(BKnight, Not(BKnave))
XORC = Biconditional(CKnight, Not(CKnave))

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO
    XORA,
    #A = Knight if A = Knight and A = Knave
    Biconditional(AKnight, And(AKnight, AKnave)),
    
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    XORA, XORB,
    #A = Knight if A,B = Knave
    Biconditional(AKnight,And(AKnave,BKnave)),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    XORA, XORB,
    #A = Knight if A & B = Knight or A & B = Knave
    Biconditional(AKnight, Or(And(AKnight, BKnight),And(AKnave,BKnave))),
    #B = Knight if A != B
    Biconditional(BKnight, Not(AKnight)),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
    XORA, XORB,XORC,
    #A = Knight or A = Knave
    Or(Biconditional(AKnight, AKnight), Biconditional(AKnave,AKnave)),
    #B = Knight if A != Knight
    Biconditional(BKnight, Not(Biconditional(AKnight, AKnight))),
    #B = Knight if C = Knave
    Biconditional(BKnight, CKnave),
    #C = Knight if A = Knight
    Biconditional(CKnight,AKnight),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
