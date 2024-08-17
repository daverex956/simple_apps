
import json
import spacy
from textblob import TextBlob
from collections import Counter
import textstat
from gensim import corpora, models

# Load data from a JSON file
def load_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data['texts']

# Perform sentiment analysis
def sentiment_analysis(text):
    analysis = TextBlob(text)
    return analysis.sentiment

# Frequency analysis
def frequency_analysis(texts):
    words = " ".join(texts).split()
    frequency = Counter(words)
    most_common_words = frequency.most_common(10)
    print("Most common words:", most_common_words)

# Named Entity Recognition
def named_entity_recognition(texts):
    # Load the spaCy model
    nlp = spacy.load("en_core_web_sm")  # Make sure this matches the installed model name

    for text in texts:
        doc = nlp(text)
        for entity in doc.ents:
            print(f"Entity: {entity.text}, Type: {entity.label_}")

# Readability scores
def readability_scores(texts):
    for text in texts:
        score = textstat.flesch_reading_ease(text)
        print(f"Text: {text[:30]}... Readability Score: {score}")

# Topic Modeling
def topic_modeling(texts):
    texts = [text.split() for text in texts]
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    lda_model = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)
    topics = lda_model.print_topics(num_words=3)
    for topic in topics:
        print(f"Topic: {topic}")

# Main function to process each text
def main():
    texts = load_data('/Users/pinax/Desktop/PythonApps/text_analysis/text.json')  # Update the path to your JSON file
    print("Sentiment Analysis Results:")
    for text in texts:
        sentiment = sentiment_analysis(text)
        print(f"Text: {text}\nSentiment: Polarity={sentiment.polarity}, Subjectivity={sentiment.subjectivity}\n")
    
    print("Frequency Analysis Results:")
    frequency_analysis(texts)

    print("Named Entity Recognition Results:")
    named_entity_recognition(texts)

    print("Readability Scores Results:")
    readability_scores(texts)

    print("Topic Modeling Results:")
    topic_modeling(texts)

# Run the main function
if __name__ == "__main__":
    main()
