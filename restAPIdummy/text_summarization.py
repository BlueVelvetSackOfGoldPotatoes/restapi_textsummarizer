import spacy
import os
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

def word_processing(text):
    extra_words=list(STOP_WORDS)+list(punctuation)+['\n']
    os.system("python -m spacy download en_core_web_sm")
    nlp=spacy.load("en_core_web_sm")
    docx = nlp(text)
    return docx, extra_words

def word_freq(docx, extra_words):
  all_words=[word.text for word in docx]
  Freq_word={}
  for w in all_words:
        w1=w.lower()
        if w1 not in extra_words and w1.isalpha():
            if w1 in Freq_word.keys():
                Freq_word[w1]+=1
            else:
                Freq_word[w1]=1
  return Freq_word

def get_sentence_strength(docx, word_freq):
  sent_strength={}
  for sent in docx.sents:
        for word in sent :
              if word.text.lower() in word_freq.keys():
                  if sent in sent_strength.keys():
                      sent_strength[sent]+=word_freq[word.text.lower()]
                  else:
                      sent_strength[sent]=word_freq[word.text.lower()]
              else: 
                  continue
  return sent_strength

def get_summary(sent_strength):
  summary=[]
  top_sentences=(sorted(sent_strength.values())[::-1])
  top30percent_sentence=int(0.3*len(top_sentences))
  top_sent=top_sentences[:top30percent_sentence]
  for sent,strength in sent_strength.items():
        if strength in top_sent:
            summary.append(sent)
        else:
            continue
  string_to_add = ""
  print("SUMMARY ----------------:")
  for i in summary:
    string_to_add += str(print(i,end=""))
  return string_to_add, summary