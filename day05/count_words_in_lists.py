celestial_objects = [
    'Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid'
]

# Get unique words in the order of their first appearance
unique_words = []
found = False
for word in celestial_objects:
    for i in range(len(unique_words)):
        if unique_words[i][0] == word:
            unique_words[i][1] += 1
            found = True
            break
    if not found:
        unique_words.append([word, 1])

for item in unique_words:
    print(f"{item[0]:<10} {item[1]}")
