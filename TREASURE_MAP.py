line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
letter = position[0].lower()
print(letter)
abc = ("a", "b", "c")
letter_index = abc.index(letter)
print(letter_index)
numbers_index = int(position[1]) - 1
print(numbers_index)
map[numbers_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")