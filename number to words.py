# $ pip install inflect
# Numbers to words
import inflect
n=inflect.engine()
words=n.number_to_words(12345,group=1)
print(words)
words=n.number_to_words(n.ordinal(12345))
print(words)
words = n.number_to_words(123456, group=1)
print(words)
words = n.number_to_words(1234667, group=2)
print(words)

#import num2word
#num2word.to_card(16)
