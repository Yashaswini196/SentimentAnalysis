import pickle
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
nltk.download('wordnet')

class EmotionModel:
    
    def __init__(self):
        self.classifier = pickle.load(open("emotion_analysis\sentiment_model1.pkl","rb"))
        self.cv = pickle.load(open("emotion_analysis\sentiment_vectorizer.pkl","rb"))
        self.lm = WordNetLemmatizer()
        self.emotions = {0:"Angry",1:"Sad",2:'Fear',3:"Surprise",4:"Joy",5:"Love"}
    
    def process_review(self, review):
        corpus = []
        text = re.sub('[^a-zA-Z]'," ",review)
        text_lower = text.lower()
        lower_list = text_lower.split()
        lower_list = [self.lm.lemmatize(i) for i in lower_list if i not in set(stopwords.words('english'))]
        clean_text = " ".join(lower_list)
        corpus.append(clean_text)
        x = self.cv.transform(corpus).toarray()
        output = self.classifier.predict(x)
        print("\n\n\noutput: ", output)
        output = self.emotions[output[0]]
        response = {}
        response['removed_special_char'] = text
        response['text_lower'] = text_lower
        response['clean_text'] = clean_text
        response['corpus'] = corpus
        response['result'] = output 

        string="""
                Natural language process take following steps:\n
                    1. Removing special charecter: "{}" \n
                    2. Lowering all words: "{}"\n
                    3. Lemmatization- It usually refers to remove inflectional endings only 
                        and to return the base: "{}"\n
                    4. Making Corpus: "{}"\n
                    5. Making Bag of words: "{}"\n
                    6. Finally prediction: "{}"\n
            """.format(text,text_lower,clean_text,corpus,x,output)
            
        return response
