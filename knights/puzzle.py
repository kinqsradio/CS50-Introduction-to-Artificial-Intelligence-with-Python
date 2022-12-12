from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

#Note: Speak by a knave is always false so therefore should be using Not for what they says

#Possible statements for A,B and C
XORA = And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))) #AKnight or AKnave but cannot be both
XORB = And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))) #BKnight or BKnave but cannot be both
XORC = And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))) #CKnight or CKnave but cannot be both


# Puzzle 0
# A says "I am both a knight and a knave."
ASays = And(AKnight,AKnave) #Both knight and knave
knowledge0 = And(
    # TODO
    XORA,
    Implication(AKnight,ASays),
    Implication(AKnave,Not(ASays))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
ASays = And(AKnave,BKnave) #A and B are both knaves
knowledge1 = And(
    # TODO
    XORA, 
    XORB,
    Implication(AKnight, ASays),
    Implication(AKnave, Not(ASays)),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
ASays = Or(And(AKnight, BKnight), And(AKnave,BKnave)) #Same kind Knight or Knave
BSays = Or(And(AKnight, BKnave), And(AKnave, BKnight)) #Of different kinds
knowledge2 = And(
    # TODO
    XORA,
    XORB,
    Implication(AKnight, ASays),
    Implication(AKnave, Not(ASays)),
    Implication(BKnight, BSays),
    Implication(BKnave, Not(BSays)),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
    XORA,
    XORB,
    XORC,
    Or(Biconditional(AKnight, AKnight), Biconditional(AKnight,AKnave)), #A is a knight if "I am a knight" or "I am a knave" is true
    Biconditional(BKnight, Biconditional(AKnight, AKnave)), #B is a knighht if "A said 'I am a knave'." is true
    Biconditional(BKnight,CKnave), #If B is a Knight, "C is a knave" is true
    Biconditional(CKnight,AKnight), #If C is a Knight, "A is a knight" is true
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
