
'''
Endpoint handler for HTTP GET request to return text summary and id, and another endpoint that handles HTTP POST requests to add new texts. 
'''

import os
from flask import Flask, jsonify, request
from text_summarization import *

app = Flask(__name__)

# with open('./data.json') as data:
#     texts = json.load(data)

texts = [
  { 'document_id': '1', 'text': '''This book will perhaps only be understood by those
who have themselves already thought the thoughts which
are expressed in it---or similar thoughts. It is therefore
not a text-book. Its object would be attained if there
were one person who read it with understanding and to
whom it afforded pleasure.

The book deals with the problems of philosophy and
shows, as I believe, that the method of formulating these
problems rests on the misunderstanding of the logic of
our language. Its whole meaning could be summed up
somewhat as follows: What can be said at all can be said
clearly; and whereof one cannot speak thereof one must
be silent.

The book will, therefore, draw a limit to thinking,
or rather---not to thinking, but to the expression of
thoughts; for, in order to draw a limit to thinking we
should have to be able to think both sides of this limit
(we should therefore have to be able to think what cannot
be thought).

The limit can, therefore, only be drawn in language
and what lies on the other side of the limit will be simply
nonsense.

How far my efforts agree with those of other philosophers
I will not decide. Indeed what I have here
written makes no claim to novelty in points of detail;
and therefore I give no sources, because it is indifferent
to me whether what I have thought has already been
thought before me by another.

I will only mention that to the great works of Frege
and the writings of my friend Bertrand Russell I owe in
large measure the stimulation of my thoughts.

If this work has a value it consists in two things.
First that in it thoughts are expressed, and this value will
be the greater the better the thoughts are expressed. The
more the nail has been hit on the head. Here I am
conscious that I have fallen far short of the possible.
Simply because my powers are insufficient to cope with
the task. May others come and do it better.

On the other hand the truth of the thoughts communicated
here seems to me unassailable and definitive. I
am, therefore, of the opinion that the problems have in
essentials been finally solved. And if I am not mistaken
in this, then the value of this work secondly consists in the
fact that it shows how little has been done when these
problems have been solved.'''}
]

@app.route('/texts', methods=['GET'])
def get_dic():
  return jsonify(texts)

@app.route('/get', methods=['GET'])
def get_texts():
  # Summarize here
  dic_id = request.args.get("dic_id")
  y = texts
  my_dic = next((item for item in y if item['document_id'] == dic_id), None)
  if my_dic == None:
    return "No text for given id"
  else: 
    return my_dic["text"]

@app.route('/add', methods=['POST'])
def add_texts():
  texts.append(request.get_json())
  # json.dumps(texts, indent=4)
  return '', 204

@app.route('/text_summarizer', methods=['GET'])
def get_text_summarizer():
  # Summarize here
  dic_id = request.args.get("dic_id")
  y = texts
  my_dic = next((item for item in y if item['document_id'] == dic_id), None)
  if my_dic == None:
    return "No text for given id"
  else: 
    doc = my_dic["text"]
    docx, extra_words = word_processing(doc)
    os.system("clear")
    print()
    print("DOCX -------------------:")
    print(docx)
    Freq_word = word_freq(docx, extra_words)
    print()
    print("FREQ WORD --------------:")
    print(Freq_word)
    print()
    print("EXTRA WORDS ------------:")
    print(extra_words)
    sentence_strength = get_sentence_strength(docx, Freq_word)
    print()
    print("SENTENCE STRENGHT ------:")
    print(sentence_strength)
    print()
  
    string_to_add, summary = get_summary(sentence_strength)
    print()
    # for i in summary:
    #   print(i, end="")
    return string_to_add
