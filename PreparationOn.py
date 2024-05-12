with open("Frankenstein Or The Modern Prometheus.txt",encoding= 'utf-8') as f: #I open file as a string. Method open takes text and mode ("r" is read mode).
    words = [word.lower() # Every word is changed to the lower case.
             for line in f
             for word in line.split() if word not in punctuation] #With method .split() I split a string into a list of words and I check if the word is punctuation. 
eng_stopwords = set(stopwords.words('english')) #I define a set which contains all the stopwords.
without_stopwords = [w for w in words if not w in eng_stopwords] #I remove stopwords from the text.
stemi = PorterStemmer() #I called stemi, which will change words into their infinitive.
stemmed_words = [stemi.stem(word) for word in without_stopwords] #With method stemi, which changes letters into infinitives, I reduce inflected words to these stems.
pairs = [(x, stemmed_words.count(x)) for x in set(stemmed_words)]
#I define a list of pairs, which contains a word and the number of word repetitions.
sorted_pairs = sorted(pairs, key=lambda pair: pair[1], reverse = True)
#I use the sorted method, which sorts the list of pairs based on the value of the second element of each pair. If reverse=True, it sorts the list in descending order.
filtered_pairs = [(word, freq) for word, freq in sorted_pairs if freq > 100]
# I filter out words with a frequency greater than 100.
print(filtered_pairs) # I print the filtered pairs.