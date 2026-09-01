# mini project love calculator by using ASCII values of name

print(f"{'Welcome To Love Calculator':^{50}}")
# formatting the text for center alignment

print(48 * "=")
# printing 48 '='

name1 = (input("Enter your name :- ").lower()).strip()
# taking the input as lower case and stripping any unwanted spaces or tabs

name2 = (input("Enter your partners name :- ").lower()).strip()
# taking the input as lower case and stripping any unwanted spaces or tabs

name1_score = 0

name2_score = 0

for letters in name1:
    name1_score += ord(letters)
    # getting the summation of each letters ASCII value

for letters in name2:
    name2_score += ord(letters)
    # getting the summation of each letters ASCII value

total = name1_score + name2_score

difference = abs(name1_score - name2_score)

couple_match = (total - difference) / total * 100
# Used normalise difference ratio in percentage
# Which means finding out the gap between two numbers in percentage

if couple_match > 85:
    print("\n💍 Soulmate written in stars!")

elif couple_match > 65:
    print("\n💘 There is a strong connection")

elif couple_match > 40:
    print("\n😕 Could work! Need effort")

else:
    print("\n🙂 Might be better as friends")
