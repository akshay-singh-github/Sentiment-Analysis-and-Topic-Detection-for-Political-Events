import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import gensim
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import os
import time
import pymysql
import mysql.connector
import datetime
import xlsxwriter
import sys
import time
import json
import csv
import io

tokenizer = RegexpTokenizer(r'\w+')
# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

doc_set = []
CorpusFilesPath = "D:/EXPERIMENT/Files1"
File_list = os.listdir(CorpusFilesPath)
for file in File_list:
    file_path_name = CorpusFilesPath + "/" + file
    with open(file_path_name,"r") as f:
        data = f.read()
        doc_set.append(data)

"""
# create sample documents
doc_a =
doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
doc_e = "Health professionals say that brocolli is good for your health."
"""
# compile sample documents into a list
#doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]


user_id = ["AgriGoI",
           "RadhamohanBJP",
           "moayush",
           "shripadynaik",
           "moca_goi",
           "ashok_gajapathi",
           "coalministry",
           "PiyushGoyalOffc",
           "PiyushGoyal",
           "CimGOI",
           "nsitharaman",
           "dot_India",
           "manojsinhabjp",
           "consaff",
           "irvpaswan",
           "arunjaitley",
           "MinOfCultureGoI",
           "dr_maheshsharma",
           "SpokespersonMoD",
           "manoharparrikar",
           "MDoNER_India",
           "DrJitendraSingh",
           "nstomar",
           "moesgoi",
           "drharshvardhan",
           "GoI_MeitY",
           "rsprasad",
           "moefcc",
           "anilmdave",
           "MEAIndia",
           "SushmaSwaraj",
           "FinMinIndia",
           "MOFPI_GOI",
           "HarsimratBadal_",
           "MoHFW_INDIA",
           "JPNadda",
           "heindustry",
           "AnantGeeteSS",
           "HMOIndia",
           "rajnathsingh",
           "MoHUPA",
           "MVenkaiahNaidu",
           "HRDMinistry",
           "PrakashJavdekar",
           "MIB_India",
           "LabourMinistry",
           "Dattatreya",
           "minmsme",
           "KalrajMishra",
           "MinesMinIndia",
           "naqvimukhtar",
           "mnreindia",
           "MoPRIndia",
           "mpa_india",
           "AnanthKumar_BJP",
           "PetroleumMin",
           "dpradhanbjp",
           "MinOfPower",
           "RailMinIndia",
           "sureshpprabhu",
           "MORTHIndia",
           "nitin_gadkari",
           "PMRDF_official",
           "IndiaDST",
           "shipmin_india",
           "MSDESkillindia",
           "RajivPratapRudy",
           "MSJEGOI",
           "TCGEHLOT",
           "DVSBJP",
           "SteelMinIndia",
           "ChBirenderSingh",
           "tourismgoi",
           "TribalAffairsIn",
           "jualoram",
           "Moud_India",
           "umasribharti",
           "MinistryWCD",
           "Manekagandhibjp",
           "IndiaSports",
           "VijayGoelBJP",
           "DRDO_India",
           "isro",
           "narendramodi",
           "PMOIndia",
           "PIB_India"]
new_user_id = []
for word in user_id:
    new_user_id.append(word.lower())

# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:
    # clean and tokenize document string
    raw = i.lower()

    #print (raw)
    tokens = tokenizer.tokenize(raw)
    badWordsRemoved = []
    stop_words = ["rt", "http"]
    for k in tokens:
        if k not in stop_words:
            badWordsRemoved.append(k)
    new_tokens = []
    for g in badWordsRemoved:
        if g not in new_user_id:
            new_tokens.append(g)
    # remove stop words from tokens
    longer_tokens = []
    for h in new_tokens:
        if len(h)>2:
            longer_tokens.append(h)
    stopped_tokens = []
    for i in longer_tokens:
        if i not in en_stop:
            stopped_tokens.append(i)


    # stem tokens
    stemmed_tokens = []
    for i in stopped_tokens:
        stemmed_tokens.append(p_stemmer.stem(i))

    # add tokens to list
    texts.append(stemmed_tokens)


# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)

# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word = dictionary, passes=500)

print(ldamodel.print_topics(num_topics=3, num_words=10))
