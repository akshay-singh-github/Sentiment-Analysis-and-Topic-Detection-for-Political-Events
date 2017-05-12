import json
import csv
import io
import unicodedata
import time
import re
from nltk.tokenize import RegexpTokenizer

usernames = ["@AgriGoI",
                            "@RadhamohanBJP",
                            "@moayush",
                            "@shripadynaik",
                            "@moca_goi",
                            "@ashok_gajapathi",
                            "@coalministry",
                            "@PiyushGoyalOffc",
                            "@PiyushGoyal",
                            "@CimGOI",
                            "@nsitharaman",
                            "@dot_India",
                            "@manojsinhabjp",
                            "@consaff",
                            "@irvpaswan",
                            "@arunjaitley",
                            "@MinOfCultureGoI",
                            "@dr_maheshsharma",
                            "@SpokespersonMoD",
                            "@manoharparrikar",
                            "@MDoNER_India",
                            "@DrJitendraSingh",
                            "@nstomar",
                            "@moesgoi",
                            "@drharshvardhan",
                            "@GoI_MeitY",
                            "@rsprasad",
                            "@moefcc",
                            "@anilmdave",
                            "@MEAIndia",
                            "@SushmaSwaraj",
                            "@FinMinIndia",
                            "@MOFPI_GOI",
                            "@HarsimratBadal_",
                            "@MoHFW_INDIA",
                            "@JPNadda",
                            "@heindustry",
                            "@AnantGeeteSS",
                            "@HMOIndia",
                            "@rajnathsingh",
                            "@MoHUPA",
                            "@MVenkaiahNaidu",
                            "@HRDMinistry",
                            "@PrakashJavdekar",
                            "@MIB_India",
                            "@LabourMinistry",
                            "@Dattatreya",
                            "@minmsme",
                            "@KalrajMishra",
                            "@MinesMinIndia",
                            "@naqvimukhtar",
                            "@mnreindia",
                            "@MoPRIndia",
                            "@mpa_india",
                            "@AnanthKumar_BJP",
                            "@PetroleumMin",
                            "@dpradhanbjp",
                            "@MinOfPower",
                            "@RailMinIndia",
                            "@sureshpprabhu",
                            "@MORTHIndia",
                            "@nitin_gadkari",
                            "@PMRDF_official",
                            "@IndiaDST",
                            "@shipmin_india",
                            "@MSDESkillindia",
                            "@RajivPratapRudy",
                            "@MSJEGOI",
                            "@TCGEHLOT",
                            "@DVSBJP",
                            "@SteelMinIndia",
                            "@ChBirenderSingh",
                            "@tourismgoi",
                            "@TribalAffairsIn",
                            "@jualoram",
                            "@Moud_India",
                            "@umasribharti",
                            "@MinistryWCD",
                            "@Manekagandhibjp",
                            "@IndiaSports",
                            "@VijayGoelBJP",
                            "@DRDO_India",
                            "@isro",
                            "@narendramodi",
                            "@PMOIndia",
                            "@PIB_India",
                            "RT"
                            ]

newuser = []
for word in usernames:
    newuser.append(word.lower())

mostPopularHashtags = ['#lahukalagaan', '#bjymnec', '#vijaymallya', '#dreamzgkfraud', '#satyagrah4men',
                       '#nsel', '#transformingindia', '#privateschoolfeehikeatrocity', '#makeinindia', '#ti17curtainraiser', '#worldheritageday']
CommonPath = "D:/EXPERIMENT/Timing/"
for tag in mostPopularHashtags:
    #########################################################################################################################
    with open('D:/EXPERIMENT/tweetsDB_day1_18APR_7_45AM_8_45AM.json', "r") as tweet_data1:
        json_data1 = json.load(tweet_data1)
    tweet_data1.close()
    newOutputFilePath1 = CommonPath+tag+"/"+"tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
    with open(newOutputFilePath1, "a") as f1:
        for line in json_data1:
            try:
                text_words = line['text'].split()
                small_text_words = []
                for word in text_words:
                    small_text_words.append(word.lower())
                newText = []
                for word in small_text_words:
                    word = re.sub(r'^https?:\/\/.*[\r\n]*', '', word, flags=re.MULTILINE)
                    word = re.sub(r'^http?:\/\/.*[\r\n]*', '', word, flags=re.MULTILINE)
                    word = word.replace("…", "").replace(",", "").replace(".", "")
                    if word not in newuser:
                        if len(word) > 0:
                            newText.append(word)
                for t in newText:
                    if t.find(tag) != -1:
                        result = " ".join(newText)
                        f1.write(result)
                        f1.write("\n")
            except BaseException as e:
                print(str(e))
    f1.close()
    #########################################################################################################################
    with open('D:/EXPERIMENT/tweetsDB_day1_18APR_7_30PM_9_30PM.json', "r") as tweet_data2:
        json_data2 = json.load(tweet_data2)
    tweet_data2.close()
    newOutputFilePath2 = CommonPath+tag+"/"+"tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
    with open(newOutputFilePath2, "a") as f2:
        for line in json_data2:
            try:
                text_words = line['text'].split()
                small_text_words = []
                for word in text_words:
                    small_text_words.append(word.lower())
                newText = []
                for word in small_text_words:
                    word = re.sub(r'^https?:\/\/.*[\r\n]*', '', word, flags=re.MULTILINE)
                    word = re.sub(r'^http?:\/\/.*[\r\n]*', '', word, flags=re.MULTILINE)
                    word = word.replace("…", "").replace(",", "").replace(".", "")
                    if word not in newuser:
                        if len(word) > 0:
                            newText.append(word)
                for t in newText:
                    if t.find(tag) != -1:
                        result = " ".join(newText)
                        f2.write(result)
                        f2.write("\n")
            except BaseException as e:
                print(str(e))
    f2.close()
    #########################################################################################################################
    with open('D:/EXPERIMENT/tweetsDB_day1_18APR_10_00PM_12_00PM.json', "r") as tweet_data3:
        json_data3 = json.load(tweet_data3)
    tweet_data3.close()
    newOutputFilePath3 = CommonPath+tag+"/"+"tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
    with open(newOutputFilePath3, "a") as f3:
        for line in json_data3:
            try:
                text_words = line['text'].split()
                small_text_words = []
                for word in text_words:
                    small_text_words.append(word.lower())
                newText = []
                for word in small_text_words:
                    word = re.sub(r'^https?:\/\/.*[\r\n]*', '', word, flags=re.MULTILINE)
                    word = re.sub(r'^http?:\/\/.*[\r\n]*', '', word, flags=re.MULTILINE)
                    word = word.replace("…", "").replace(",", "").replace(".", "")
                    if word not in newuser:
                        if len(word) > 0:
                            newText.append(word)
                for t in newText:
                    if t.find(tag) != -1:
                        result = " ".join(newText)
                        f3.write(result)
                        f3.write("\n")
            except BaseException as e:
                print(str(e))
    f3.close()
    #########################################################################################################################
    with open('D:/EXPERIMENT/tweetsDB_day1_19APR_12_00AM_02_00AM.json', "r") as tweet_data4:
        json_data4 = json.load(tweet_data4)
    tweet_data4.close()
    newOutputFilePath4 = CommonPath+tag+"/"+"tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
    with open(newOutputFilePath4, "a") as f4:
        for line in json_data4:
            try:
                text_words = line['text'].split()
                small_text_words = []
                for word in text_words:
                    small_text_words.append(word.lower())
                newText = []
                for word in small_text_words:
                    word = re.sub(r'^https?:\/\/.*[\r\n]*', '', word, flags=re.MULTILINE)
                    word = re.sub(r'^http?:\/\/.*[\r\n]*', '', word, flags=re.MULTILINE)
                    word = word.replace("…", "").replace(",", "").replace(".", "")
                    if word not in newuser:
                        if len(word) > 0:
                            newText.append(word)
                for t in newText:
                    if t.find(tag) != -1:
                        result = " ".join(newText)
                        f4.write(result)
                        f4.write("\n")
            except BaseException as e:
                print(str(e))
    f4.close()



