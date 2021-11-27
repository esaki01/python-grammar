class Word:

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Word!'

    def __len__(self):
        return len(self.text)

    def __add__(self, other):
        return self.text.lower() + " " + other.text.lower()

    def __eq__(self, other):
        return self.text.lower() == other.text.lower()


w = Word('Text')
w2 = Word('Text')

print(w)
print(len(w))
print(w + w2)
print(w == w2)
