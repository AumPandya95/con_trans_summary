import spacy
from spacy.matcher import Matcher 
from spacy.tokens import Span 


def main():
    nlp = spacy.load("en_core_web_sm")

    # sample text 
    text = "GDP in developing countries such as Vietnam will continue growing at a high rate." 

    # create a spaCy object 
    doc = nlp(text)

    return doc

if __name__ == "__main__":
    check = main()
