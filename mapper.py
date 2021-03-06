import sys
import io
import re
import nltk
import string
nltk.download('stopwords',quiet=True)
from nltk.corpus import stopwords
signes = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

stop_words = stopwords.words('english') + stopwords.words('spanish') + stopwords.words('italian') 
stop_words = set(stop_words)
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
for line in input_stream:
  line = line.strip()
  line = re.sub(r'[^\w\s]', '',line)
  line = line.lower()
  for x in line:
    if x in signes:
      line=line.replace(x, " ") 

  words=line.split()
  for word in words: 
    if word not in stop_words:
        letra = word[0:1]
        if letra in list('abcdefghijklmnñopqrstuvwxyzç'):
          print('%s\t%s' % (letra, 1))
