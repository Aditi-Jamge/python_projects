with open("story.txt","r") as f:
    story = f.read()

start = "<"
end = ">"
word_index = -1
words = set()

for i,char in enumerate(story):
    if char == start:
        word_index = i

    if char == end and word_index != -1:
        word = story[word_index : i + 1]
        words.add(word)
        word_index = -1

answers = {}

for word in words:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer

for word in words:
    story = story.replace(word,answers[word])

print(story)





