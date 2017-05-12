import re
import tweepy
import os
from tweepy import OAuthHandler
from textblob import TextBlob


mostPopularHashtags = ['#lahukalagaan', '#bjymnec', '#vijaymallya', '#dreamzgkfraud', '#satyagrah4men',
                       '#nsel', '#transformingindia', '#privateschoolfeehikeatrocity', '#makeinindia',
                       '#ti17curtainraiser', '#worldheritageday']

CommonPath = "D:/EXPERIMENT/Timing/"

#Sentiment Analysis
#################################################################################################################################################################################
lahukalagaan_path = "D:/EXPERIMENT/Timing/#lahukalagaan"
lahukalagaan_file1 = "D:/EXPERIMENT/Timing/#lahukalagaan/tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
lahukalagaan_file2 = "D:/EXPERIMENT/Timing/#lahukalagaan/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
lahukalagaan_file3 = "D:/EXPERIMENT/Timing/#lahukalagaan/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
lahukalagaan_file4 = "D:/EXPERIMENT/Timing/#lahukalagaan/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_lahukalagaan_file1 = "D:/EXPERIMENT/Timing/#lahukalagaan/sentiment_tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
with open(lahukalagaan_file1, "r") as a:
    data_a = a.read().splitlines()
a.close()
lahukalagaan_file1_positive = 0
lahukalagaan_file1_neutral = 0
lahukalagaan_file1_negative = 0
with open(sentiment_lahukalagaan_file1, "a") as b:
    for c in data_a:
        analysis = TextBlob(c)
        if analysis.sentiment.polarity > 0:
            lahukalagaan_file1_positive += 1
            b.write("%s : %s" % (c, "4"))
            b.write("\n")
        elif analysis.sentiment.polarity == 0:
            lahukalagaan_file1_neutral += 1
            b.write("%s : %s" % (c, "2"))
            b.write("\n")
        else:
            lahukalagaan_file1_negative += 1
            b.write("%s : %s" % (c, "0"))
            b.write("\n")
    Total_number_sentiment_file_1 = (lahukalagaan_file1_positive + lahukalagaan_file1_neutral + lahukalagaan_file1_negative)
    lahukalagaan_file1_positive_percentage = (lahukalagaan_file1_positive*100) / float(1+Total_number_sentiment_file_1)
    lahukalagaan_file1_neutral__percentage = (lahukalagaan_file1_neutral*100) / float(1+Total_number_sentiment_file_1)
    lahukalagaan_file1_negative__percentage = (lahukalagaan_file1_negative*100) / float(1+Total_number_sentiment_file_1)
    b.write("Positive Percentage : %s" % str(lahukalagaan_file1_positive_percentage))
    b.write("\n")
    b.write("Neutral Percentage : %s" % str(lahukalagaan_file1_neutral__percentage))
    b.write("\n")
    b.write("Negative Percentage : %s" % str(lahukalagaan_file1_negative__percentage))
    b.write("\n")
b.close()
#########################################
#lahukalagaan_file2 = "D:/EXPERIMENT/Timing/#lahukalagaan/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
sentiment_lahukalagaan_file2 = "D:/EXPERIMENT/Timing/#lahukalagaan/sentiment_tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
with open(lahukalagaan_file2, "r") as a2:
    data_a2 = a2.read().splitlines()
a2.close()
lahukalagaan_file2_positive = 0
lahukalagaan_file2_neutral = 0
lahukalagaan_file2_negative = 0
with open(sentiment_lahukalagaan_file2, "a") as b2:
    for c2 in data_a2:
        analysis2 = TextBlob(c2)
        if analysis2.sentiment.polarity > 0:
            lahukalagaan_file2_positive += 1
            b2.write("%s : %s" % (c2, "4"))
            b2.write("\n")
        elif analysis2.sentiment.polarity == 0:
            lahukalagaan_file2_neutral += 1
            b2.write("%s : %s" % (c2, "2"))
            b2.write("\n")
        else:
            lahukalagaan_file2_negative += 1
            b2.write("%s : %s" % (c2, "0"))
            b2.write("\n")
    Total_number_sentiment_file_2 = (lahukalagaan_file2_positive + lahukalagaan_file2_neutral + lahukalagaan_file2_negative)
    lahukalagaan_file2_positive_percentage = (lahukalagaan_file2_positive*100) / float(1+Total_number_sentiment_file_2)
    lahukalagaan_file2_neutral__percentage = (lahukalagaan_file2_neutral*100) / float(1+Total_number_sentiment_file_2)
    lahukalagaan_file2_negative__percentage = (lahukalagaan_file2_negative*100) / float(1+Total_number_sentiment_file_2)
    b2.write("Positive Percentage : %s" % str(lahukalagaan_file2_positive_percentage))
    b2.write("\n")
    b2.write("Neutral Percentage : %s" % str(lahukalagaan_file2_neutral__percentage))
    b2.write("\n")
    b2.write("Negative Percentage : %s" % str(lahukalagaan_file2_negative__percentage))
    b2.write("\n")
b2.close()
#############################################
#lahukalagaan_file3 = "D:/EXPERIMENT/Timing/#lahukalagaan/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
sentiment_lahukalagaan_file3 = "D:/EXPERIMENT/Timing/#lahukalagaan/sentiment_tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
with open(lahukalagaan_file3, "r") as a3:
    data_a3 = a3.read().splitlines()
a3.close()
lahukalagaan_file3_positive = 0
lahukalagaan_file3_neutral = 0
lahukalagaan_file3_negative = 0
with open(sentiment_lahukalagaan_file3, "a") as b3:
    for c3 in data_a3:
        analysis3 = TextBlob(c3)
        if analysis3.sentiment.polarity > 0:
            lahukalagaan_file3_positive += 1
            b3.write("%s : %s" % (c3, "4"))
            b3.write("\n")
        elif analysis3.sentiment.polarity == 0:
            lahukalagaan_file3_neutral += 1
            b3.write("%s : %s" % (c3, "2"))
            b3.write("\n")
        else:
            lahukalagaan_file3_negative += 1
            b3.write("%s : %s" % (c3, "0"))
            b3.write("\n")
    Total_number_sentiment_file_3 = (lahukalagaan_file3_positive + lahukalagaan_file3_neutral + lahukalagaan_file3_negative)
    lahukalagaan_file3_positive_percentage = (lahukalagaan_file3_positive*100) / float(1+Total_number_sentiment_file_3)
    lahukalagaan_file3_neutral__percentage = (lahukalagaan_file3_neutral*100) / float(1+Total_number_sentiment_file_3)
    lahukalagaan_file3_negative__percentage = (lahukalagaan_file3_negative*100) / float(1+Total_number_sentiment_file_3)
    b3.write("Positive Percentage : %s" % str(lahukalagaan_file3_positive_percentage))
    b3.write("\n")
    b3.write("Neutral Percentage : %s" % str(lahukalagaan_file3_neutral__percentage))
    b3.write("\n")
    b3.write("Negative Percentage : %s" % str(lahukalagaan_file3_negative__percentage))
    b3.write("\n")
b3.close()
#############################################
#lahukalagaan_file4 = "D:/EXPERIMENT/Timing/#lahukalagaan/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
sentiment_lahukalagaan_file4 = "D:/EXPERIMENT/Timing/#lahukalagaan/sentiment_tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
with open(lahukalagaan_file4, "r") as a4:
    data_a4 = a4.read().splitlines()
a4.close()
lahukalagaan_file4_positive = 0
lahukalagaan_file4_neutral = 0
lahukalagaan_file4_negative = 0
with open(sentiment_lahukalagaan_file4, "a") as b4:
    for c4 in data_a4:
        analysis4 = TextBlob(c4)
        if analysis4.sentiment.polarity > 0:
            lahukalagaan_file4_positive += 1
            b4.write("%s : %s" % (c4, "4"))
            b4.write("\n")
        elif analysis4.sentiment.polarity == 0:
            lahukalagaan_file4_neutral += 1
            b4.write("%s : %s" % (c4, "2"))
            b4.write("\n")
        else:
            lahukalagaan_file4_negative += 1
            b4.write("%s : %s" % (c4, "0"))
            b4.write("\n")
    Total_number_sentiment_file_4 = (lahukalagaan_file4_positive + lahukalagaan_file4_neutral + lahukalagaan_file4_negative)
    lahukalagaan_file4_positive_percentage = (lahukalagaan_file4_positive*100) / float(1+Total_number_sentiment_file_4)
    lahukalagaan_file4_neutral__percentage = (lahukalagaan_file4_neutral*100) / float(1+Total_number_sentiment_file_4)
    lahukalagaan_file4_negative__percentage = (lahukalagaan_file4_negative*100) / float(1+Total_number_sentiment_file_4)
    b4.write("Positive Percentage : %s" % str(lahukalagaan_file4_positive_percentage))
    b4.write("\n")
    b4.write("Neutral Percentage : %s" % str(lahukalagaan_file4_neutral__percentage))
    b4.write("\n")
    b4.write("Negative Percentage : %s" % str(lahukalagaan_file4_negative__percentage))
    b4.write("\n")
b4.close()
########################################################################################################################################################################

##2
#################################################################################################################################################################################
bjymnec_path = "D:/EXPERIMENT/Timing/#bjymnec"
bjymnec_file1 = "D:/EXPERIMENT/Timing/#bjymnec/tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
bjymnec_file2 = "D:/EXPERIMENT/Timing/#bjymnec/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
bjymnec_file3 = "D:/EXPERIMENT/Timing/#bjymnec/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
bjymnec_file4 = "D:/EXPERIMENT/Timing/#bjymnec/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_bjymnec_file1 = "D:/EXPERIMENT/Timing/#bjymnec/sentiment_tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
with open(bjymnec_file1, "r") as d1:
    data_d1 = d1.read().splitlines()
d1.close()
bjymnec_file1_positive = 0
bjymnec_file1_neutral = 0
bjymnec_file1_negative = 0
with open(sentiment_bjymnec_file1, "a") as e1:
    for f1 in data_d1:
        analysis1 = TextBlob(f1)
        if analysis1.sentiment.polarity > 0:
            bjymnec_file1_positive += 1
            e1.write("%s : %s" % (f1, "4"))
            e1.write("\n")
        elif analysis1.sentiment.polarity == 0:
            bjymnec_file1_neutral += 1
            e1.write("%s : %s" % (f1, "2"))
            e1.write("\n")
        else:
            bjymnec_file1_negative += 1
            e1.write("%s : %s" % (f1, "0"))
            e1.write("\n")
    Total_number_bjymnec_sentiment_file_1 = (bjymnec_file1_positive + bjymnec_file1_neutral + bjymnec_file1_negative)
    bjymnec_file1_positive_percentage = (bjymnec_file1_positive*100) / float(1+Total_number_bjymnec_sentiment_file_1)
    bjymnec_file1_neutral__percentage = (bjymnec_file1_neutral*100) / float(1+Total_number_bjymnec_sentiment_file_1)
    bjymnec_file1_negative__percentage = (bjymnec_file1_negative*100) / float(1+Total_number_bjymnec_sentiment_file_1)
    e1.write("Positive Percentage : %s" % str(bjymnec_file1_positive_percentage))
    e1.write("\n")
    e1.write("Neutral Percentage : %s" % str(bjymnec_file1_neutral__percentage))
    e1.write("\n")
    e1.write("Negative Percentage : %s" % str(bjymnec_file1_negative__percentage))
    e1.write("\n")
e1.close()
#########################################
#bjymnec_file2 = "D:/EXPERIMENT/Timing/#bjymnec/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
sentiment_bjymnec_file2 = "D:/EXPERIMENT/Timing/#bjymnec/sentiment_tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
with open(bjymnec_file2, "r") as d2:
    data_d2 = d2.read().splitlines()
d2.close()
bjymnec_file2_positive = 0
bjymnec_file2_neutral = 0
bjymnec_file2_negative = 0
with open(sentiment_bjymnec_file2, "a") as e2:
    for f2 in data_d2:
        analysis2 = TextBlob(f2)
        if analysis2.sentiment.polarity > 0:
            bjymnec_file2_positive += 1
            e2.write("%s : %s" % (f2, "4"))
            e2.write("\n")
        elif analysis2.sentiment.polarity == 0:
            bjymnec_file2_neutral += 1
            e2.write("%s : %s" % (f2, "2"))
            e2.write("\n")
        else:
            bjymnec_file2_negative += 1
            e2.write("%s : %s" % (f2, "0"))
            e2.write("\n")
    Total_number_bjymnec_sentiment_file_2 = (bjymnec_file2_positive + bjymnec_file2_neutral + bjymnec_file2_negative)
    bjymnec_file2_positive_percentage = (bjymnec_file2_positive*100) / float(1+Total_number_bjymnec_sentiment_file_2)
    bjymnec_file2_neutral__percentage = (bjymnec_file2_neutral*100) / float(1+Total_number_bjymnec_sentiment_file_2)
    bjymnec_file2_negative__percentage = (bjymnec_file2_negative*100) / float(1+Total_number_bjymnec_sentiment_file_2)
    e2.write("Positive Percentage : %s" % str(bjymnec_file2_positive_percentage))
    e2.write("\n")
    e2.write("Neutral Percentage : %s" % str(bjymnec_file2_neutral__percentage))
    e2.write("\n")
    e2.write("Negative Percentage : %s" % str(bjymnec_file2_negative__percentage))
    e2.write("\n")
e2.close()
#############################################
#bjymnec_file3 = "D:/EXPERIMENT/Timing/#bjymnec/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
sentiment_bjymnec_file3 = "D:/EXPERIMENT/Timing/#bjymnec/sentiment_tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
with open(bjymnec_file3, "r") as d3:
    data_d3 = d3.read().splitlines()
d3.close()
bjymnec_file3_positive = 0
bjymnec_file3_neutral = 0
bjymnec_file3_negative = 0
with open(sentiment_bjymnec_file3, "a") as e3:
    for f3 in data_d3:
        analysis3 = TextBlob(f3)
        if analysis3.sentiment.polarity > 0:
            bjymnec_file3_positive += 1
            e3.write("%s : %s" % (f3, "4"))
            e3.write("\n")
        elif analysis3.sentiment.polarity == 0:
            bjymnec_file3_neutral += 1
            e3.write("%s : %s" % (f3, "2"))
            e3.write("\n")
        else:
            bjymnec_file3_negative += 1
            e3.write("%s : %s" % (f3, "0"))
            e3.write("\n")
    Total_number_bjymnec_sentiment_file_3 = (bjymnec_file3_positive + bjymnec_file3_neutral + bjymnec_file3_negative)
    bjymnec_file3_positive_percentage = (bjymnec_file3_positive*100) / float(1+Total_number_bjymnec_sentiment_file_3)
    bjymnec_file3_neutral__percentage = (bjymnec_file3_neutral*100) / float(1+Total_number_bjymnec_sentiment_file_3)
    bjymnec_file3_negative__percentage = (bjymnec_file3_negative*100) / float(1+Total_number_bjymnec_sentiment_file_3)
    e3.write("Positive Percentage : %s" % str(bjymnec_file3_positive_percentage))
    e3.write("\n")
    e3.write("Neutral Percentage : %s" % str(bjymnec_file3_neutral__percentage))
    e3.write("\n")
    e3.write("Negative Percentage : %s" % str(bjymnec_file3_negative__percentage))
    e3.write("\n")
e3.close()
#############################################
#bjymnec_file4 = "D:/EXPERIMENT/Timing/#bjymnec/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
sentiment_bjymnec_file4 = "D:/EXPERIMENT/Timing/#bjymnec/sentiment_tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
with open(bjymnec_file4, "r") as d4:
    data_d4 = d4.read().splitlines()
d4.close()
bjymnec_file4_positive = 0
bjymnec_file4_neutral = 0
bjymnec_file4_negative = 0
with open(sentiment_bjymnec_file4, "a") as e4:
    for f4 in data_d4:
        analysis4 = TextBlob(f4)
        if analysis4.sentiment.polarity > 0:
            bjymnec_file4_positive += 1
            e4.write("%s : %s" % (f4, "4"))
            e4.write("\n")
        elif analysis4.sentiment.polarity == 0:
            bjymnec_file4_neutral += 1
            e4.write("%s : %s" % (f4, "2"))
            e4.write("\n")
        else:
            bjymnec_file4_negative += 1
            e4.write("%s : %s" % (f4, "0"))
            e4.write("\n")
    Total_number_bjymnec_sentiment_file_4 = (bjymnec_file4_positive + bjymnec_file4_neutral + bjymnec_file4_negative)
    bjymnec_file4_positive_percentage = (bjymnec_file4_positive*100) / float(1+Total_number_bjymnec_sentiment_file_4)
    bjymnec_file4_neutral__percentage = (bjymnec_file4_neutral*100) / float(1+Total_number_bjymnec_sentiment_file_4)
    bjymnec_file4_negative__percentage = (bjymnec_file4_negative*100) / float(1+Total_number_bjymnec_sentiment_file_4)
    e4.write("Positive Percentage : %s" % str(bjymnec_file4_positive_percentage))
    e4.write("\n")
    e4.write("Neutral Percentage : %s" % str(bjymnec_file4_neutral__percentage))
    e4.write("\n")
    e4.write("Negative Percentage : %s" % str(bjymnec_file4_negative__percentage))
    e4.write("\n")
e4.close()
########################################################################################################################################################################

##3

#################################################################################################################################################################################
vijaymallya_path = "D:/EXPERIMENT/Timing/#vijaymallya"
vijaymallya_file1 = "D:/EXPERIMENT/Timing/#vijaymallya/tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
vijaymallya_file2 = "D:/EXPERIMENT/Timing/#vijaymallya/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
vijaymallya_file3 = "D:/EXPERIMENT/Timing/#vijaymallya/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
vijaymallya_file4 = "D:/EXPERIMENT/Timing/#vijaymallya/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_vijaymallya_file1 = "D:/EXPERIMENT/Timing/#vijaymallya/sentiment_tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
with open(vijaymallya_file1, "r") as g1:
    data_g1 = g1.read().splitlines()
g1.close()
vijaymallya_file1_positive = 0
vijaymallya_file1_neutral = 0
vijaymallya_file1_negative = 0
with open(sentiment_vijaymallya_file1, "a") as h1:
    for i1 in data_g1:
        analysis1 = TextBlob(i1)
        if analysis1.sentiment.polarity > 0:
            vijaymallya_file1_positive += 1
            h1.write("%s : %s" % (i1, "4"))
            h1.write("\n")
        elif analysis1.sentiment.polarity == 0:
            vijaymallya_file1_neutral += 1
            h1.write("%s : %s" % (i1, "2"))
            h1.write("\n")
        else:
            vijaymallya_file1_negative += 1
            h1.write("%s : %s" % (i1, "0"))
            h1.write("\n")
    Total_number_vijaymallya_sentiment_file_1 = (vijaymallya_file1_positive + vijaymallya_file1_neutral + vijaymallya_file1_negative)
    vijaymallya_file1_positive_percentage = (vijaymallya_file1_positive*100) / float(1+Total_number_vijaymallya_sentiment_file_1)
    vijaymallya_file1_neutral__percentage = (vijaymallya_file1_neutral*100) / float(1+Total_number_vijaymallya_sentiment_file_1)
    vijaymallya_file1_negative__percentage = (vijaymallya_file1_negative*100) / float(1+Total_number_vijaymallya_sentiment_file_1)
    h1.write("Positive Percentage : %s" % str(vijaymallya_file1_positive_percentage))
    h1.write("\n")
    h1.write("Neutral Percentage : %s" % str(vijaymallya_file1_neutral__percentage))
    h1.write("\n")
    h1.write("Negative Percentage : %s" % str(vijaymallya_file1_negative__percentage))
    h1.write("\n")
h1.close()
#########################################
#vijaymallya_file2 = "D:/EXPERIMENT/Timing/#vijaymallya/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
sentiment_vijaymallya_file2 = "D:/EXPERIMENT/Timing/#vijaymallya/sentiment_tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
with open(vijaymallya_file2, "r") as g2:
    data_g2 = g2.read().splitlines()
g2.close()
vijaymallya_file2_positive = 0
vijaymallya_file2_neutral = 0
vijaymallya_file2_negative = 0
with open(sentiment_vijaymallya_file2, "a") as h2:
    for i2 in data_g2:
        analysis2 = TextBlob(i2)
        if analysis2.sentiment.polarity > 0:
            vijaymallya_file2_positive += 1
            h2.write("%s : %s" % (i2, "4"))
            h2.write("\n")
        elif analysis2.sentiment.polarity == 0:
            vijaymallya_file2_neutral += 1
            h2.write("%s : %s" % (i2, "2"))
            h2.write("\n")
        else:
            vijaymallya_file2_negative += 1
            h2.write("%s : %s" % (i2, "0"))
            h2.write("\n")
    Total_number_vijaymallya_sentiment_file_2 = (vijaymallya_file2_positive + vijaymallya_file2_neutral + vijaymallya_file2_negative)
    vijaymallya_file2_positive_percentage = (vijaymallya_file2_positive*100) / float(1+Total_number_vijaymallya_sentiment_file_2)
    vijaymallya_file2_neutral__percentage = (vijaymallya_file2_neutral*100) / float(1+Total_number_vijaymallya_sentiment_file_2)
    vijaymallya_file2_negative__percentage = (vijaymallya_file2_negative*100) / float(1+Total_number_vijaymallya_sentiment_file_2)
    h2.write("Positive Percentage : %s" % str(vijaymallya_file2_positive_percentage))
    h2.write("\n")
    h2.write("Neutral Percentage : %s" % str(vijaymallya_file2_neutral__percentage))
    h2.write("\n")
    h2.write("Negative Percentage : %s" % str(vijaymallya_file2_negative__percentage))
    h2.write("\n")
h2.close()
#############################################
#vijaymallya_file3 = "D:/EXPERIMENT/Timing/#vijaymallya/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
sentiment_vijaymallya_file3 = "D:/EXPERIMENT/Timing/#vijaymallya/sentiment_tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
with open(vijaymallya_file3, "r") as g3:
    data_g3 = g3.read().splitlines()
g3.close()
vijaymallya_file3_positive = 0
vijaymallya_file3_neutral = 0
vijaymallya_file3_negative = 0
with open(sentiment_vijaymallya_file3, "a") as h3:
    for i3 in data_g3:
        analysis3 = TextBlob(i3)
        if analysis3.sentiment.polarity > 0:
            vijaymallya_file3_positive += 1
            h3.write("%s : %s" % (i3, "4"))
            h3.write("\n")
        elif analysis3.sentiment.polarity == 0:
            vijaymallya_file3_neutral += 1
            h3.write("%s : %s" % (i3, "2"))
            h3.write("\n")
        else:
            vijaymallya_file3_negative += 1
            h3.write("%s : %s" % (i3, "0"))
            h3.write("\n")
    Total_number_vijaymallya_sentiment_file_3 = (vijaymallya_file3_positive + vijaymallya_file3_neutral + vijaymallya_file3_negative)
    vijaymallya_file3_positive_percentage = (vijaymallya_file3_positive*100) / float(1+Total_number_vijaymallya_sentiment_file_3)
    vijaymallya_file3_neutral__percentage = (vijaymallya_file3_neutral*100) / float(1+Total_number_vijaymallya_sentiment_file_3)
    vijaymallya_file3_negative__percentage = (vijaymallya_file3_negative*100) / float(1+Total_number_vijaymallya_sentiment_file_3)
    h3.write("Positive Percentage : %s" % str(vijaymallya_file3_positive_percentage))
    h3.write("\n")
    h3.write("Neutral Percentage : %s" % str(vijaymallya_file3_neutral__percentage))
    h3.write("\n")
    h3.write("Negative Percentage : %s" % str(vijaymallya_file3_negative__percentage))
    h3.write("\n")
h3.close()
#############################################
#vijaymallya_file4 = "D:/EXPERIMENT/Timing/#vijaymallya/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
sentiment_vijaymallya_file4 = "D:/EXPERIMENT/Timing/#vijaymallya/sentiment_tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
with open(vijaymallya_file4, "r") as g4:
    data_g4 = g4.read().splitlines()
g4.close()
vijaymallya_file4_positive = 0
vijaymallya_file4_neutral = 0
vijaymallya_file4_negative = 0
with open(sentiment_vijaymallya_file4, "a") as h4:
    for i4 in data_g4:
        analysis4 = TextBlob(i4)
        if analysis4.sentiment.polarity > 0:
            vijaymallya_file4_positive += 1
            h4.write("%s : %s" % (i4, "4"))
            h4.write("\n")
        elif analysis4.sentiment.polarity == 0:
            vijaymallya_file4_neutral += 1
            h4.write("%s : %s" % (i4, "2"))
            h4.write("\n")
        else:
            vijaymallya_file4_negative += 1
            h4.write("%s : %s" % (i4, "0"))
            h4.write("\n")
    Total_number_vijaymallya_sentiment_file_4 = (vijaymallya_file4_positive + vijaymallya_file4_neutral + vijaymallya_file4_negative)
    vijaymallya_file4_positive_percentage = (vijaymallya_file4_positive*100) / float(1+Total_number_vijaymallya_sentiment_file_4)
    vijaymallya_file4_neutral__percentage = (vijaymallya_file4_neutral*100) / float(1+Total_number_vijaymallya_sentiment_file_4)
    vijaymallya_file4_negative__percentage = (vijaymallya_file4_negative*100) / float(1+Total_number_vijaymallya_sentiment_file_4)
    h4.write("Positive Percentage : %s" % str(vijaymallya_file4_positive_percentage))
    h4.write("\n")
    h4.write("Neutral Percentage : %s" % str(vijaymallya_file4_neutral__percentage))
    h4.write("\n")
    h4.write("Negative Percentage : %s" % str(vijaymallya_file4_negative__percentage))
    h4.write("\n")
h4.close()
########################################################################################################################################################################
##4

#################################################################################################################################################################################
worldheritageday_path = "D:/EXPERIMENT/Timing/#worldheritageday"
worldheritageday_file1 = "D:/EXPERIMENT/Timing/#worldheritageday/tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
worldheritageday_file2 = "D:/EXPERIMENT/Timing/#worldheritageday/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
worldheritageday_file3 = "D:/EXPERIMENT/Timing/#worldheritageday/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
worldheritageday_file4 = "D:/EXPERIMENT/Timing/#worldheritageday/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_worldheritageday_file1 = "D:/EXPERIMENT/Timing/#worldheritageday/sentiment_tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
with open(worldheritageday_file1, "r") as j1:
    data_j1 = j1.read().splitlines()
j1.close()
worldheritageday_file1_positive = 0
worldheritageday_file1_neutral = 0
worldheritageday_file1_negative = 0
with open(sentiment_worldheritageday_file1, "a") as k1:
    for l1 in data_j1:
        analysis1 = TextBlob(l1)
        if analysis1.sentiment.polarity > 0:
            worldheritageday_file1_positive += 1
            k1.write("%s : %s" % (l1, "4"))
            k1.write("\n")
        elif analysis1.sentiment.polarity == 0:
            worldheritageday_file1_neutral += 1
            k1.write("%s : %s" % (l1, "2"))
            k1.write("\n")
        else:
            worldheritageday_file1_negative += 1
            k1.write("%s : %s" % (l1, "0"))
            k1.write("\n")
    Total_number_worldheritageday_sentiment_file_1 = (worldheritageday_file1_positive + worldheritageday_file1_neutral + worldheritageday_file1_negative)
    worldheritageday_file1_positive_percentage = (worldheritageday_file1_positive*100) / float(1+Total_number_worldheritageday_sentiment_file_1)
    worldheritageday_file1_neutral__percentage = (worldheritageday_file1_neutral*100) / float(1+Total_number_worldheritageday_sentiment_file_1)
    worldheritageday_file1_negative__percentage = (worldheritageday_file1_negative*100) / float(1+Total_number_worldheritageday_sentiment_file_1)
    k1.write("Positive Percentage : %s" % str(worldheritageday_file1_positive_percentage))
    k1.write("\n")
    k1.write("Neutral Percentage : %s" % str(worldheritageday_file1_neutral__percentage))
    k1.write("\n")
    k1.write("Negative Percentage : %s" % str(worldheritageday_file1_negative__percentage))
    k1.write("\n")
k1.close()
#########################################
#worldheritageday_file2 = "D:/EXPERIMENT/Timing/#worldheritageday/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
###############################################
sentiment_worldheritageday_file2 = "D:/EXPERIMENT/Timing/#worldheritageday/sentiment_tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
with open(worldheritageday_file2, "r") as j2:
    data_j2 = j2.read().splitlines()
j2.close()
worldheritageday_file2_positive = 0
worldheritageday_file2_neutral = 0
worldheritageday_file2_negative = 0
with open(sentiment_worldheritageday_file2, "a") as k2:
    for l2 in data_j2:
        analysis2 = TextBlob(l2)
        if analysis2.sentiment.polarity > 0:
            worldheritageday_file2_positive += 1
            k2.write("%s : %s" % (l2, "4"))
            k2.write("\n")
        elif analysis2.sentiment.polarity == 0:
            worldheritageday_file2_neutral += 1
            k2.write("%s : %s" % (l2, "2"))
            k2.write("\n")
        else:
            worldheritageday_file2_negative += 1
            k2.write("%s : %s" % (l2, "0"))
            k2.write("\n")
    Total_number_worldheritageday_sentiment_file_2 = (worldheritageday_file2_positive + worldheritageday_file2_neutral + worldheritageday_file2_negative)
    worldheritageday_file2_positive_percentage = (worldheritageday_file2_positive*100) / float(1+Total_number_worldheritageday_sentiment_file_2)
    worldheritageday_file2_neutral__percentage = (worldheritageday_file2_neutral*100) / float(1+Total_number_worldheritageday_sentiment_file_2)
    worldheritageday_file2_negative__percentage = (worldheritageday_file2_negative*100) / float(1+Total_number_worldheritageday_sentiment_file_2)
    k2.write("Positive Percentage : %s" % str(worldheritageday_file2_positive_percentage))
    k2.write("\n")
    k2.write("Neutral Percentage : %s" % str(worldheritageday_file2_neutral__percentage))
    k2.write("\n")
    k2.write("Negative Percentage : %s" % str(worldheritageday_file2_negative__percentage))
    k2.write("\n")
k2.close()
#############################################
#worldheritageday_file3 = "D:/EXPERIMENT/Timing/#worldheritageday/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
###############################################
sentiment_worldheritageday_file3 = "D:/EXPERIMENT/Timing/#worldheritageday/sentiment_tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
with open(worldheritageday_file3, "r") as j3:
    data_j3 = j3.read().splitlines()
j3.close()
worldheritageday_file3_positive = 0
worldheritageday_file3_neutral = 0
worldheritageday_file3_negative = 0
with open(sentiment_worldheritageday_file3, "a") as k3:
    for l3 in data_j3:
        analysis3 = TextBlob(l3)
        if analysis3.sentiment.polarity > 0:
            worldheritageday_file3_positive += 1
            k3.write("%s : %s" % (l3, "4"))
            k3.write("\n")
        elif analysis3.sentiment.polarity == 0:
            worldheritageday_file3_neutral += 1
            k3.write("%s : %s" % (l3, "2"))
            k3.write("\n")
        else:
            worldheritageday_file3_negative += 1
            k3.write("%s : %s" % (l3, "0"))
            k3.write("\n")
    Total_number_worldheritageday_sentiment_file_3 = (worldheritageday_file3_positive + worldheritageday_file3_neutral + worldheritageday_file3_negative)
    worldheritageday_file3_positive_percentage = (worldheritageday_file3_positive*100) / float(1+Total_number_worldheritageday_sentiment_file_3)
    worldheritageday_file3_neutral__percentage = (worldheritageday_file3_neutral*100) / float(1+Total_number_worldheritageday_sentiment_file_3)
    worldheritageday_file3_negative__percentage = (worldheritageday_file3_negative*100) / float(1+Total_number_worldheritageday_sentiment_file_3)
    k3.write("Positive Percentage : %s" % str(worldheritageday_file3_positive_percentage))
    k3.write("\n")
    k3.write("Neutral Percentage : %s" % str(worldheritageday_file3_neutral__percentage))
    k3.write("\n")
    k3.write("Negative Percentage : %s" % str(worldheritageday_file3_negative__percentage))
    k3.write("\n")
k3.close()
#############################################
#worldheritageday_file4 = "D:/EXPERIMENT/Timing/#worldheritageday/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_worldheritageday_file4 = "D:/EXPERIMENT/Timing/#worldheritageday/sentiment_tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
with open(worldheritageday_file4, "r") as j4:
    data_j4 = j4.read().splitlines()
j4.close()
worldheritageday_file4_positive = 0
worldheritageday_file4_neutral = 0
worldheritageday_file4_negative = 0
with open(sentiment_worldheritageday_file4, "a") as k4:
    for l4 in data_j4:
        analysis4 = TextBlob(l4)
        if analysis4.sentiment.polarity > 0:
            worldheritageday_file4_positive += 1
            k4.write("%s : %s" % (l4, "4"))
            k4.write("\n")
        elif analysis4.sentiment.polarity == 0:
            worldheritageday_file4_neutral += 1
            k4.write("%s : %s" % (l4, "2"))
            k4.write("\n")
        else:
            worldheritageday_file4_negative += 1
            k4.write("%s : %s" % (l4, "0"))
            k4.write("\n")
    Total_number_worldheritageday_sentiment_file_4 = (worldheritageday_file4_positive + worldheritageday_file4_neutral + worldheritageday_file4_negative)
    worldheritageday_file4_positive_percentage = (worldheritageday_file4_positive*100) / float(1+Total_number_worldheritageday_sentiment_file_4)
    worldheritageday_file4_neutral__percentage = (worldheritageday_file4_neutral*100) / float(1+Total_number_worldheritageday_sentiment_file_4)
    worldheritageday_file4_negative__percentage = (worldheritageday_file4_negative*100) / float(1+Total_number_worldheritageday_sentiment_file_4)
    k4.write("Positive Percentage : %s" % str(worldheritageday_file4_positive_percentage))
    k4.write("\n")
    k4.write("Neutral Percentage : %s" % str(worldheritageday_file4_neutral__percentage))
    k4.write("\n")
    k4.write("Negative Percentage : %s" % str(worldheritageday_file4_negative__percentage))
    k4.write("\n")
k4.close()
########################################################################################################################################################################
##5
#################################################################################################################################################################################
ti17curtainraiser_path = "D:/EXPERIMENT/Timing/#ti17curtainraiser"
ti17curtainraiser_file1 = "D:/EXPERIMENT/Timing/#ti17curtainraiser/tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
ti17curtainraiser_file2 = "D:/EXPERIMENT/Timing/#ti17curtainraiser/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
ti17curtainraiser_file3 = "D:/EXPERIMENT/Timing/#ti17curtainraiser/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
ti17curtainraiser_file4 = "D:/EXPERIMENT/Timing/#ti17curtainraiser/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_ti17curtainraiser_file1 = "D:/EXPERIMENT/Timing/#ti17curtainraiser/sentiment_tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
with open(ti17curtainraiser_file1, "r") as m1:
    data_m1 = m1.read().splitlines()
m1.close()
ti17curtainraiser_file1_positive = 0
ti17curtainraiser_file1_neutral = 0
ti17curtainraiser_file1_negative = 0
with open(sentiment_ti17curtainraiser_file1, "a") as n1:
    for o1 in data_m1:
        analysis1 = TextBlob(o1)
        if analysis1.sentiment.polarity > 0:
            ti17curtainraiser_file1_positive += 1
            n1.write("%s : %s" % (o1, "4"))
            n1.write("\n")
        elif analysis1.sentiment.polarity == 0:
            ti17curtainraiser_file1_neutral += 1
            n1.write("%s : %s" % (o1, "2"))
            n1.write("\n")
        else:
            ti17curtainraiser_file1_negative += 1
            n1.write("%s : %s" % (o1, "0"))
            n1.write("\n")
    Total_number_ti17curtainraiser_sentiment_file_1 = (ti17curtainraiser_file1_positive + ti17curtainraiser_file1_neutral + ti17curtainraiser_file1_negative)
    ti17curtainraiser_file1_positive_percentage = (ti17curtainraiser_file1_positive*100) / float(1+Total_number_ti17curtainraiser_sentiment_file_1)
    ti17curtainraiser_file1_neutral__percentage = (ti17curtainraiser_file1_neutral*100) / float(1+Total_number_ti17curtainraiser_sentiment_file_1)
    ti17curtainraiser_file1_negative__percentage = (ti17curtainraiser_file1_negative*100) / float(1+Total_number_ti17curtainraiser_sentiment_file_1)
    n1.write("Positive Percentage : %s" % str(ti17curtainraiser_file1_positive_percentage))
    n1.write("\n")
    n1.write("Neutral Percentage : %s" % str(ti17curtainraiser_file1_neutral__percentage))
    n1.write("\n")
    n1.write("Negative Percentage : %s" % str(ti17curtainraiser_file1_negative__percentage))
    n1.write("\n")
n1.close()
#########################################
#ti17curtainraiser_file2 = "D:/EXPERIMENT/Timing/#ti17curtainraiser/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"

###############################################
sentiment_ti17curtainraiser_file2 = "D:/EXPERIMENT/Timing/#ti17curtainraiser/sentiment_tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
with open(ti17curtainraiser_file2, "r") as m2:
    data_m2 = m2.read().splitlines()
m2.close()
ti17curtainraiser_file2_positive = 0
ti17curtainraiser_file2_neutral = 0
ti17curtainraiser_file2_negative = 0
with open(sentiment_ti17curtainraiser_file2, "a") as n2:
    for o2 in data_m2:
        analysis2 = TextBlob(o2)
        if analysis2.sentiment.polarity > 0:
            ti17curtainraiser_file2_positive += 1
            n2.write("%s : %s" % (o2, "4"))
            n2.write("\n")
        elif analysis2.sentiment.polarity == 0:
            ti17curtainraiser_file2_neutral += 1
            n2.write("%s : %s" % (o2, "2"))
            n2.write("\n")
        else:
            ti17curtainraiser_file2_negative += 1
            n2.write("%s : %s" % (o2, "0"))
            n2.write("\n")
    Total_number_ti17curtainraiser_sentiment_file_2 = (ti17curtainraiser_file2_positive + ti17curtainraiser_file2_neutral + ti17curtainraiser_file2_negative)
    ti17curtainraiser_file2_positive_percentage = (ti17curtainraiser_file2_positive*100) / float(1+Total_number_ti17curtainraiser_sentiment_file_2)
    ti17curtainraiser_file2_neutral__percentage = (ti17curtainraiser_file2_neutral*100) / float(1+Total_number_ti17curtainraiser_sentiment_file_2)
    ti17curtainraiser_file2_negative__percentage = (ti17curtainraiser_file2_negative*100) / float(1+Total_number_ti17curtainraiser_sentiment_file_2)
    n2.write("Positive Percentage : %s" % str(ti17curtainraiser_file2_positive_percentage))
    n2.write("\n")
    n2.write("Neutral Percentage : %s" % str(ti17curtainraiser_file2_neutral__percentage))
    n2.write("\n")
    n2.write("Negative Percentage : %s" % str(ti17curtainraiser_file2_negative__percentage))
    n2.write("\n")
n2.close()
#############################################
#ti17curtainraiser_file3 = "D:/EXPERIMENT/Timing/#ti17curtainraiser/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
###############################################
sentiment_ti17curtainraiser_file3 = "D:/EXPERIMENT/Timing/#ti17curtainraiser/sentiment_tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
with open(ti17curtainraiser_file3, "r") as m3:
    data_m3 = m3.read().splitlines()
m3.close()
ti17curtainraiser_file3_positive = 0
ti17curtainraiser_file3_neutral = 0
ti17curtainraiser_file3_negative = 0
with open(sentiment_ti17curtainraiser_file3, "a") as n3:
    for o3 in data_m3:
        analysis3 = TextBlob(o3)
        if analysis3.sentiment.polarity > 0:
            ti17curtainraiser_file3_positive += 1
            n3.write("%s : %s" % (o3, "4"))
            n3.write("\n")
        elif analysis3.sentiment.polarity == 0:
            ti17curtainraiser_file3_neutral += 1
            n3.write("%s : %s" % (o3, "2"))
            n3.write("\n")
        else:
            ti17curtainraiser_file3_negative += 1
            n3.write("%s : %s" % (o3, "0"))
            n3.write("\n")
    Total_number_ti17curtainraiser_sentiment_file_3 = (ti17curtainraiser_file3_positive + ti17curtainraiser_file3_neutral + ti17curtainraiser_file3_negative)
    ti17curtainraiser_file3_positive_percentage = (ti17curtainraiser_file3_positive*100) / float(1+Total_number_ti17curtainraiser_sentiment_file_3)
    ti17curtainraiser_file3_neutral__percentage = (ti17curtainraiser_file3_neutral*100) / float(1+Total_number_ti17curtainraiser_sentiment_file_3)
    ti17curtainraiser_file3_negative__percentage = (ti17curtainraiser_file3_negative*100) / float(1+Total_number_ti17curtainraiser_sentiment_file_3)
    n3.write("Positive Percentage : %s" % str(ti17curtainraiser_file3_positive_percentage))
    n3.write("\n")
    n3.write("Neutral Percentage : %s" % str(ti17curtainraiser_file3_neutral__percentage))
    n3.write("\n")
    n3.write("Negative Percentage : %s" % str(ti17curtainraiser_file3_negative__percentage))
    n3.write("\n")
n3.close()
#############################################
#ti17curtainraiser_file4 = "D:/EXPERIMENT/Timing/#ti17curtainraiser/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_ti17curtainraiser_file4 = "D:/EXPERIMENT/Timing/#ti17curtainraiser/sentiment_tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
with open(ti17curtainraiser_file4, "r") as m4:
    data_m4 = m4.read().splitlines()
m4.close()
ti17curtainraiser_file4_positive = 0
ti17curtainraiser_file4_neutral = 0
ti17curtainraiser_file4_negative = 0
with open(sentiment_ti17curtainraiser_file4, "a") as n4:
    for o4 in data_m4:
        analysis4 = TextBlob(o4)
        if analysis4.sentiment.polarity > 0:
            ti17curtainraiser_file4_positive += 1
            n4.write("%s : %s" % (o4, "4"))
            n4.write("\n")
        elif analysis4.sentiment.polarity == 0:
            ti17curtainraiser_file4_neutral += 1
            n4.write("%s : %s" % (o4, "2"))
            n4.write("\n")
        else:
            ti17curtainraiser_file4_negative += 1
            n4.write("%s : %s" % (o4, "0"))
            n4.write("\n")
    Total_number_ti17curtainraiser_sentiment_file_4 = (ti17curtainraiser_file4_positive + ti17curtainraiser_file4_neutral + ti17curtainraiser_file4_negative)
    ti17curtainraiser_file4_positive_percentage = (ti17curtainraiser_file4_positive*100) / float(1+Total_number_ti17curtainraiser_sentiment_file_4)
    ti17curtainraiser_file4_neutral__percentage = (ti17curtainraiser_file4_neutral*100) / float(1+Total_number_ti17curtainraiser_sentiment_file_4)
    ti17curtainraiser_file4_negative__percentage = (ti17curtainraiser_file4_negative*100) / float(1+Total_number_ti17curtainraiser_sentiment_file_4)
    n4.write("Positive Percentage : %s" % str(ti17curtainraiser_file4_positive_percentage))
    n4.write("\n")
    n4.write("Neutral Percentage : %s" % str(ti17curtainraiser_file4_neutral__percentage))
    n4.write("\n")
    n4.write("Negative Percentage : %s" % str(ti17curtainraiser_file4_negative__percentage))
    n4.write("\n")
n4.close()
########################################################################################################################################################################
##6
#################################################################################################################################################################################
makeinindia_path = "D:/EXPERIMENT/Timing/#makeinindia"
makeinindia_file1 = "D:/EXPERIMENT/Timing/#makeinindia/tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
makeinindia_file2 = "D:/EXPERIMENT/Timing/#makeinindia/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
makeinindia_file3 = "D:/EXPERIMENT/Timing/#makeinindia/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
makeinindia_file4 = "D:/EXPERIMENT/Timing/#makeinindia/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_makeinindia_file1 = "D:/EXPERIMENT/Timing/#makeinindia/sentiment_tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
with open(makeinindia_file1, "r") as p1:
    data_p1 = p1.read().splitlines()
p1.close()
makeinindia_file1_positive = 0
makeinindia_file1_neutral = 0
makeinindia_file1_negative = 0
with open(sentiment_makeinindia_file1, "a") as q1:
    for r1 in data_p1:
        analysis1 = TextBlob(r1)
        if analysis1.sentiment.polarity > 0:
            makeinindia_file1_positive += 1
            q1.write("%s : %s" % (r1, "4"))
            q1.write("\n")
        elif analysis1.sentiment.polarity == 0:
            makeinindia_file1_neutral += 1
            q1.write("%s : %s" % (r1, "2"))
            q1.write("\n")
        else:
            makeinindia_file1_negative += 1
            q1.write("%s : %s" % (r1, "0"))
            q1.write("\n")
    Total_number_makeinindia_sentiment_file_1 = (makeinindia_file1_positive + makeinindia_file1_neutral + makeinindia_file1_negative)
    makeinindia_file1_positive_percentage = (makeinindia_file1_positive*100) / float(1+Total_number_makeinindia_sentiment_file_1)
    makeinindia_file1_neutral__percentage = (makeinindia_file1_neutral*100) / float(1+Total_number_makeinindia_sentiment_file_1)
    makeinindia_file1_negative__percentage = (makeinindia_file1_negative*100) / float(1+Total_number_makeinindia_sentiment_file_1)
    q1.write("Positive Percentage : %s" % str(makeinindia_file1_positive_percentage))
    q1.write("\n")
    q1.write("Neutral Percentage : %s" % str(makeinindia_file1_neutral__percentage))
    q1.write("\n")
    q1.write("Negative Percentage : %s" % str(makeinindia_file1_negative__percentage))
    q1.write("\n")
q1.close()
#########################################
#makeinindia_file2 = "D:/EXPERIMENT/Timing/#makeinindia/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
###############################################
sentiment_makeinindia_file2 = "D:/EXPERIMENT/Timing/#makeinindia/sentiment_tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
with open(makeinindia_file2, "r") as p2:
    data_p2 = p2.read().splitlines()
p2.close()
makeinindia_file2_positive = 0
makeinindia_file2_neutral = 0
makeinindia_file2_negative = 0
with open(sentiment_makeinindia_file2, "a") as q2:
    for r2 in data_p2:
        analysis2 = TextBlob(r2)
        if analysis2.sentiment.polarity > 0:
            makeinindia_file2_positive += 1
            q2.write("%s : %s" % (r2, "4"))
            q2.write("\n")
        elif analysis2.sentiment.polarity == 0:
            makeinindia_file2_neutral += 1
            q2.write("%s : %s" % (r2, "2"))
            q2.write("\n")
        else:
            makeinindia_file2_negative += 1
            q2.write("%s : %s" % (r2, "0"))
            q2.write("\n")
    Total_number_makeinindia_sentiment_file_2 = (makeinindia_file2_positive + makeinindia_file2_neutral + makeinindia_file2_negative)
    makeinindia_file2_positive_percentage = (makeinindia_file2_positive*100) / float(1+Total_number_makeinindia_sentiment_file_2)
    makeinindia_file2_neutral__percentage = (makeinindia_file2_neutral*100) / float(1+Total_number_makeinindia_sentiment_file_2)
    makeinindia_file2_negative__percentage = (makeinindia_file2_negative*100) / float(1+Total_number_makeinindia_sentiment_file_2)
    q2.write("Positive Percentage : %s" % str(makeinindia_file2_positive_percentage))
    q2.write("\n")
    q2.write("Neutral Percentage : %s" % str(makeinindia_file2_neutral__percentage))
    q2.write("\n")
    q2.write("Negative Percentage : %s" % str(makeinindia_file2_negative__percentage))
    q2.write("\n")
q2.close()
#############################################
#makeinindia_file3 = "D:/EXPERIMENT/Timing/#makeinindia/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
###############################################
sentiment_makeinindia_file3 = "D:/EXPERIMENT/Timing/#makeinindia/sentiment_tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
with open(makeinindia_file3, "r") as p3:
    data_p3 = p3.read().splitlines()
p3.close()
makeinindia_file3_positive = 0
makeinindia_file3_neutral = 0
makeinindia_file3_negative = 0
with open(sentiment_makeinindia_file3, "a") as q3:
    for r3 in data_p3:
        analysis3 = TextBlob(r3)
        if analysis3.sentiment.polarity > 0:
            makeinindia_file3_positive += 1
            q3.write("%s : %s" % (r3, "4"))
            q3.write("\n")
        elif analysis3.sentiment.polarity == 0:
            makeinindia_file3_neutral += 1
            q3.write("%s : %s" % (r3, "2"))
            q3.write("\n")
        else:
            makeinindia_file3_negative += 1
            q3.write("%s : %s" % (r3, "0"))
            q3.write("\n")
    Total_number_makeinindia_sentiment_file_3 = (makeinindia_file3_positive + makeinindia_file3_neutral + makeinindia_file3_negative)
    makeinindia_file3_positive_percentage = (makeinindia_file3_positive*100) / float(1+Total_number_makeinindia_sentiment_file_3)
    makeinindia_file3_neutral__percentage = (makeinindia_file3_neutral*100) / float(1+Total_number_makeinindia_sentiment_file_3)
    makeinindia_file3_negative__percentage = (makeinindia_file3_negative*100) / float(1+Total_number_makeinindia_sentiment_file_3)
    q3.write("Positive Percentage : %s" % str(makeinindia_file3_positive_percentage))
    q3.write("\n")
    q3.write("Neutral Percentage : %s" % str(makeinindia_file3_neutral__percentage))
    q3.write("\n")
    q3.write("Negative Percentage : %s" % str(makeinindia_file3_negative__percentage))
    q3.write("\n")
q3.close()
#############################################
#makeinindia_file4 = "D:/EXPERIMENT/Timing/#makeinindia/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_makeinindia_file4 = "D:/EXPERIMENT/Timing/#makeinindia/sentiment_tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
with open(makeinindia_file4, "r") as p4:
    data_p4 = p4.read().splitlines()
p4.close()
makeinindia_file4_positive = 0
makeinindia_file4_neutral = 0
makeinindia_file4_negative = 0
with open(sentiment_makeinindia_file4, "a") as q4:
    for r4 in data_p4:
        analysis4 = TextBlob(r4)
        if analysis4.sentiment.polarity > 0:
            makeinindia_file4_positive += 1
            q4.write("%s : %s" % (r4, "4"))
            q4.write("\n")
        elif analysis4.sentiment.polarity == 0:
            makeinindia_file4_neutral += 1
            q4.write("%s : %s" % (r4, "2"))
            q4.write("\n")
        else:
            makeinindia_file4_negative += 1
            q4.write("%s : %s" % (r4, "0"))
            q4.write("\n")
    Total_number_makeinindia_sentiment_file_4 = (makeinindia_file4_positive + makeinindia_file4_neutral + makeinindia_file4_negative)
    makeinindia_file4_positive_percentage = (makeinindia_file4_positive*100) / float(1+Total_number_makeinindia_sentiment_file_4)
    makeinindia_file4_neutral__percentage = (makeinindia_file4_neutral*100) / float(1+Total_number_makeinindia_sentiment_file_4)
    makeinindia_file4_negative__percentage = (makeinindia_file4_negative*100) / float(1+Total_number_makeinindia_sentiment_file_4)
    q4.write("Positive Percentage : %s" % str(makeinindia_file4_positive_percentage))
    q4.write("\n")
    q4.write("Neutral Percentage : %s" % str(makeinindia_file4_neutral__percentage))
    q4.write("\n")
    q4.write("Negative Percentage : %s" % str(makeinindia_file4_negative__percentage))
    q4.write("\n")
q4.close()
########################################################################################################################################################################
######7
#################################################################################################################################################################################
privateschoolfeehikeatrocity_path = "D:/EXPERIMENT/Timing/#privateschoolfeehikeatrocity"
privateschoolfeehikeatrocity_file1 = "D:/EXPERIMENT/Timing/#privateschoolfeehikeatrocity/tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
privateschoolfeehikeatrocity_file2 = "D:/EXPERIMENT/Timing/#privateschoolfeehikeatrocity/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
privateschoolfeehikeatrocity_file3 = "D:/EXPERIMENT/Timing/#privateschoolfeehikeatrocity/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
privateschoolfeehikeatrocity_file4 = "D:/EXPERIMENT/Timing/#privateschoolfeehikeatrocity/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_privateschoolfeehikeatrocity_file1 = "D:/EXPERIMENT/Timing/#privateschoolfeehikeatrocity/sentiment_tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
with open(privateschoolfeehikeatrocity_file1, "r") as s1:
    data_s1 = s1.read().splitlines()
s1.close()
privateschoolfeehikeatrocity_file1_positive = 0
privateschoolfeehikeatrocity_file1_neutral = 0
privateschoolfeehikeatrocity_file1_negative = 0
with open(sentiment_privateschoolfeehikeatrocity_file1, "a") as t1:
    for u1 in data_s1:
        analysis1 = TextBlob(u1)
        if analysis1.sentiment.polarity > 0:
            privateschoolfeehikeatrocity_file1_positive += 1
            t1.write("%s : %s" % (u1, "4"))
            t1.write("\n")
        elif analysis1.sentiment.polarity == 0:
            privateschoolfeehikeatrocity_file1_neutral += 1
            t1.write("%s : %s" % (u1, "2"))
            t1.write("\n")
        else:
            privateschoolfeehikeatrocity_file1_negative += 1
            t1.write("%s : %s" % (u1, "0"))
            t1.write("\n")
    Total_number_privateschoolfeehikeatrocity_sentiment_file_1 = (privateschoolfeehikeatrocity_file1_positive + privateschoolfeehikeatrocity_file1_neutral + privateschoolfeehikeatrocity_file1_negative)
    privateschoolfeehikeatrocity_file1_positive_percentage = (privateschoolfeehikeatrocity_file1_positive*100) / float(1+Total_number_privateschoolfeehikeatrocity_sentiment_file_1)
    privateschoolfeehikeatrocity_file1_neutral__percentage = (privateschoolfeehikeatrocity_file1_neutral*100) / float(1+Total_number_privateschoolfeehikeatrocity_sentiment_file_1)
    privateschoolfeehikeatrocity_file1_negative__percentage = (privateschoolfeehikeatrocity_file1_negative*100) / float(1+Total_number_privateschoolfeehikeatrocity_sentiment_file_1)
    t1.write("Positive Percentage : %s" % str(privateschoolfeehikeatrocity_file1_positive_percentage))
    t1.write("\n")
    t1.write("Neutral Percentage : %s" % str(privateschoolfeehikeatrocity_file1_neutral__percentage))
    t1.write("\n")
    t1.write("Negative Percentage : %s" % str(privateschoolfeehikeatrocity_file1_negative__percentage))
    t1.write("\n")
t1.close()
#########################################
#privateschoolfeehikeatrocity_file2 = "D:/EXPERIMENT/Timing/#privateschoolfeehikeatrocity/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
###############################################
sentiment_privateschoolfeehikeatrocity_file2 = "D:/EXPERIMENT/Timing/#privateschoolfeehikeatrocity/sentiment_tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
with open(privateschoolfeehikeatrocity_file2, "r") as s2:
    data_s2 = s2.read().splitlines()
s2.close()
privateschoolfeehikeatrocity_file2_positive = 0
privateschoolfeehikeatrocity_file2_neutral = 0
privateschoolfeehikeatrocity_file2_negative = 0
with open(sentiment_privateschoolfeehikeatrocity_file2, "a") as t2:
    for u2 in data_s2:
        analysis2 = TextBlob(u2)
        if analysis2.sentiment.polarity > 0:
            privateschoolfeehikeatrocity_file2_positive += 1
            t2.write("%s : %s" % (u2, "4"))
            t2.write("\n")
        elif analysis2.sentiment.polarity == 0:
            privateschoolfeehikeatrocity_file2_neutral += 1
            t2.write("%s : %s" % (u2, "2"))
            t2.write("\n")
        else:
            privateschoolfeehikeatrocity_file2_negative += 1
            t2.write("%s : %s" % (u2, "0"))
            t2.write("\n")
    Total_number_privateschoolfeehikeatrocity_sentiment_file_2 = (privateschoolfeehikeatrocity_file2_positive + privateschoolfeehikeatrocity_file2_neutral + privateschoolfeehikeatrocity_file2_negative)
    privateschoolfeehikeatrocity_file2_positive_percentage = (privateschoolfeehikeatrocity_file2_positive*100) / float(1+Total_number_privateschoolfeehikeatrocity_sentiment_file_2)
    privateschoolfeehikeatrocity_file2_neutral__percentage = (privateschoolfeehikeatrocity_file2_neutral*100) / float(1+Total_number_privateschoolfeehikeatrocity_sentiment_file_2)
    privateschoolfeehikeatrocity_file2_negative__percentage = (privateschoolfeehikeatrocity_file2_negative*100) / float(1+Total_number_privateschoolfeehikeatrocity_sentiment_file_2)
    t2.write("Positive Percentage : %s" % str(privateschoolfeehikeatrocity_file2_positive_percentage))
    t2.write("\n")
    t2.write("Neutral Percentage : %s" % str(privateschoolfeehikeatrocity_file2_neutral__percentage))
    t2.write("\n")
    t2.write("Negative Percentage : %s" % str(privateschoolfeehikeatrocity_file2_negative__percentage))
    t2.write("\n")
t2.close()
#############################################
#privateschoolfeehikeatrocity_file3 = "D:/EXPERIMENT/Timing/#privateschoolfeehikeatrocity/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
###############################################
sentiment_privateschoolfeehikeatrocity_file3 = "D:/EXPERIMENT/Timing/#privateschoolfeehikeatrocity/sentiment_tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
with open(privateschoolfeehikeatrocity_file3, "r") as s3:
    data_s3 = s3.read().splitlines()
s3.close()
privateschoolfeehikeatrocity_file3_positive = 0
privateschoolfeehikeatrocity_file3_neutral = 0
privateschoolfeehikeatrocity_file3_negative = 0
with open(sentiment_privateschoolfeehikeatrocity_file3, "a") as t3:
    for u3 in data_s3:
        analysis3 = TextBlob(u3)
        if analysis3.sentiment.polarity > 0:
            privateschoolfeehikeatrocity_file3_positive += 1
            t3.write("%s : %s" % (u3, "4"))
            t3.write("\n")
        elif analysis3.sentiment.polarity == 0:
            privateschoolfeehikeatrocity_file3_neutral += 1
            t3.write("%s : %s" % (u3, "2"))
            t3.write("\n")
        else:
            privateschoolfeehikeatrocity_file3_negative += 1
            t3.write("%s : %s" % (u3, "0"))
            t3.write("\n")
    Total_number_privateschoolfeehikeatrocity_sentiment_file_3 = (privateschoolfeehikeatrocity_file3_positive + privateschoolfeehikeatrocity_file3_neutral + privateschoolfeehikeatrocity_file3_negative)
    privateschoolfeehikeatrocity_file3_positive_percentage = (privateschoolfeehikeatrocity_file3_positive*100) / float(1+Total_number_privateschoolfeehikeatrocity_sentiment_file_3)
    privateschoolfeehikeatrocity_file3_neutral__percentage = (privateschoolfeehikeatrocity_file3_neutral*100) / float(1+Total_number_privateschoolfeehikeatrocity_sentiment_file_3)
    privateschoolfeehikeatrocity_file3_negative__percentage = (privateschoolfeehikeatrocity_file3_negative*100) / float(1+Total_number_privateschoolfeehikeatrocity_sentiment_file_3)
    t3.write("Positive Percentage : %s" % str(privateschoolfeehikeatrocity_file3_positive_percentage))
    t3.write("\n")
    t3.write("Neutral Percentage : %s" % str(privateschoolfeehikeatrocity_file3_neutral__percentage))
    t3.write("\n")
    t3.write("Negative Percentage : %s" % str(privateschoolfeehikeatrocity_file3_negative__percentage))
    t3.write("\n")
t3.close()
#############################################
#privateschoolfeehikeatrocity_file4 = "D:/EXPERIMENT/Timing/#privateschoolfeehikeatrocity/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_privateschoolfeehikeatrocity_file4 = "D:/EXPERIMENT/Timing/#privateschoolfeehikeatrocity/sentiment_tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
with open(privateschoolfeehikeatrocity_file4, "r") as s4:
    data_s4 = s4.read().splitlines()
s4.close()
privateschoolfeehikeatrocity_file4_positive = 0
privateschoolfeehikeatrocity_file4_neutral = 0
privateschoolfeehikeatrocity_file4_negative = 0
with open(sentiment_privateschoolfeehikeatrocity_file4, "a") as t4:
    for u4 in data_s4:
        analysis4 = TextBlob(u4)
        if analysis4.sentiment.polarity > 0:
            privateschoolfeehikeatrocity_file4_positive += 1
            t4.write("%s : %s" % (u4, "4"))
            t4.write("\n")
        elif analysis4.sentiment.polarity == 0:
            privateschoolfeehikeatrocity_file4_neutral += 1
            t4.write("%s : %s" % (u4, "2"))
            t4.write("\n")
        else:
            privateschoolfeehikeatrocity_file4_negative += 1
            t4.write("%s : %s" % (u4, "0"))
            t4.write("\n")
    Total_number_privateschoolfeehikeatrocity_sentiment_file_4 = (privateschoolfeehikeatrocity_file4_positive + privateschoolfeehikeatrocity_file4_neutral + privateschoolfeehikeatrocity_file4_negative)
    privateschoolfeehikeatrocity_file4_positive_percentage = (privateschoolfeehikeatrocity_file4_positive*100) / float(1+Total_number_privateschoolfeehikeatrocity_sentiment_file_4)
    privateschoolfeehikeatrocity_file4_neutral__percentage = (privateschoolfeehikeatrocity_file4_neutral*100) / float(1+Total_number_privateschoolfeehikeatrocity_sentiment_file_4)
    privateschoolfeehikeatrocity_file4_negative__percentage = (privateschoolfeehikeatrocity_file4_negative*100) / float(1+Total_number_privateschoolfeehikeatrocity_sentiment_file_4)
    t4.write("Positive Percentage : %s" % str(privateschoolfeehikeatrocity_file4_positive_percentage))
    t4.write("\n")
    t4.write("Neutral Percentage : %s" % str(privateschoolfeehikeatrocity_file4_neutral__percentage))
    t4.write("\n")
    t4.write("Negative Percentage : %s" % str(privateschoolfeehikeatrocity_file4_negative__percentage))
    t4.write("\n")
t4.close()
########################################################################################################################################################################
##8



#################################################################################################################################################################################
#transformingindia_path = "D:/EXPERIMENT/Timing/#transformingindia"
transformingindia_file1 = "D:/EXPERIMENT/Timing/#transformingindia/tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
transformingindia_file2 = "D:/EXPERIMENT/Timing/#transformingindia/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
transformingindia_file3 = "D:/EXPERIMENT/Timing/#transformingindia/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
transformingindia_file4 = "D:/EXPERIMENT/Timing/#transformingindia/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_transformingindia_file1 = "D:/EXPERIMENT/Timing/#transformingindia/sentiment_tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
with open(transformingindia_file1, "r") as v1:
    data_v1 = v1.read().splitlines()
v1.close()
transformingindia_file1_positive = 0
transformingindia_file1_neutral = 0
transformingindia_file1_negative = 0
with open(sentiment_transformingindia_file1, "a") as w1:
    for x1 in data_v1:
        analysis1 = TextBlob(x1)
        if analysis1.sentiment.polarity > 0:
            transformingindia_file1_positive += 1
            w1.write("%s : %s" % (x1, "4"))
            w1.write("\n")
        elif analysis1.sentiment.polarity == 0:
            transformingindia_file1_neutral += 1
            w1.write("%s : %s" % (x1, "2"))
            w1.write("\n")
        else:
            transformingindia_file1_negative += 1
            w1.write("%s : %s" % (x1, "0"))
            w1.write("\n")
    Total_number_transformingindia_sentiment_file_1 = (transformingindia_file1_positive + transformingindia_file1_neutral + transformingindia_file1_negative)
    transformingindia_file1_positive_percentage = (transformingindia_file1_positive*100) / float(1+Total_number_transformingindia_sentiment_file_1)
    transformingindia_file1_neutral__percentage = (transformingindia_file1_neutral*100) / float(1+Total_number_transformingindia_sentiment_file_1)
    transformingindia_file1_negative__percentage = (transformingindia_file1_negative*100) / float(1+Total_number_transformingindia_sentiment_file_1)
    w1.write("Positive Percentage : %s" % str(transformingindia_file1_positive_percentage))
    w1.write("\n")
    w1.write("Neutral Percentage : %s" % str(transformingindia_file1_neutral__percentage))
    w1.write("\n")
    w1.write("Negative Percentage : %s" % str(transformingindia_file1_negative__percentage))
    w1.write("\n")
w1.close()
#########################################
#transformingindia_file2 = "D:/EXPERIMENT/Timing/#transformingindia/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
###############################################
sentiment_transformingindia_file2 = "D:/EXPERIMENT/Timing/#transformingindia/sentiment_tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
with open(transformingindia_file2, "r") as v2:
    data_v2 = v2.read().splitlines()
v2.close()
transformingindia_file2_positive = 0
transformingindia_file2_neutral = 0
transformingindia_file2_negative = 0
with open(sentiment_transformingindia_file2, "a") as w2:
    for x2 in data_v2:
        analysis2 = TextBlob(x2)
        if analysis2.sentiment.polarity > 0:
            transformingindia_file2_positive += 1
            w2.write("%s : %s" % (x2, "4"))
            w2.write("\n")
        elif analysis2.sentiment.polarity == 0:
            transformingindia_file2_neutral += 1
            w2.write("%s : %s" % (x2, "2"))
            w2.write("\n")
        else:
            transformingindia_file2_negative += 1
            w2.write("%s : %s" % (x2, "0"))
            w2.write("\n")
    Total_number_transformingindia_sentiment_file_2 = (transformingindia_file2_positive + transformingindia_file2_neutral + transformingindia_file2_negative)
    transformingindia_file2_positive_percentage = (transformingindia_file2_positive*100) / float(1+Total_number_transformingindia_sentiment_file_2)
    transformingindia_file2_neutral__percentage = (transformingindia_file2_neutral*100) / float(1+Total_number_transformingindia_sentiment_file_2)
    transformingindia_file2_negative__percentage = (transformingindia_file2_negative*100) / float(1+Total_number_transformingindia_sentiment_file_2)
    w2.write("Positive Percentage : %s" % str(transformingindia_file2_positive_percentage))
    w2.write("\n")
    w2.write("Neutral Percentage : %s" % str(transformingindia_file2_neutral__percentage))
    w2.write("\n")
    w2.write("Negative Percentage : %s" % str(transformingindia_file2_negative__percentage))
    w2.write("\n")
w2.close()
#############################################
#transformingindia_file3 = "D:/EXPERIMENT/Timing/#transformingindia/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
###############################################
sentiment_transformingindia_file3 = "D:/EXPERIMENT/Timing/#transformingindia/sentiment_tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
with open(transformingindia_file3, "r") as v3:
    data_v3 = v3.read().splitlines()
v3.close()
transformingindia_file3_positive = 0
transformingindia_file3_neutral = 0
transformingindia_file3_negative = 0
with open(sentiment_transformingindia_file3, "a") as w3:
    for x3 in data_v3:
        analysis3 = TextBlob(x3)
        if analysis3.sentiment.polarity > 0:
            transformingindia_file3_positive += 1
            w3.write("%s : %s" % (x3, "4"))
            w3.write("\n")
        elif analysis3.sentiment.polarity == 0:
            transformingindia_file3_neutral += 1
            w3.write("%s : %s" % (x3, "2"))
            w3.write("\n")
        else:
            transformingindia_file3_negative += 1
            w3.write("%s : %s" % (x3, "0"))
            w3.write("\n")
    Total_number_transformingindia_sentiment_file_3 = (transformingindia_file3_positive + transformingindia_file3_neutral + transformingindia_file3_negative)
    transformingindia_file3_positive_percentage = (transformingindia_file3_positive*100) / float(1+Total_number_transformingindia_sentiment_file_3)
    transformingindia_file3_neutral__percentage = (transformingindia_file3_neutral*100) / float(1+Total_number_transformingindia_sentiment_file_3)
    transformingindia_file3_negative__percentage = (transformingindia_file3_negative*100) / float(1+Total_number_transformingindia_sentiment_file_3)
    w3.write("Positive Percentage : %s" % str(transformingindia_file3_positive_percentage))
    w3.write("\n")
    w3.write("Neutral Percentage : %s" % str(transformingindia_file3_neutral__percentage))
    w3.write("\n")
    w3.write("Negative Percentage : %s" % str(transformingindia_file3_negative__percentage))
    w3.write("\n")
w3.close()
#############################################
#transformingindia_file4 = "D:/EXPERIMENT/Timing/#transformingindia/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_transformingindia_file4 = "D:/EXPERIMENT/Timing/#transformingindia/sentiment_tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
with open(transformingindia_file4, "r") as v4:
    data_v4 = v4.read().splitlines()
v4.close()
transformingindia_file4_positive = 0
transformingindia_file4_neutral = 0
transformingindia_file4_negative = 0
with open(sentiment_transformingindia_file4, "a") as w4:
    for x4 in data_v4:
        analysis4 = TextBlob(x4)
        if analysis4.sentiment.polarity > 0:
            transformingindia_file4_positive += 1
            w4.write("%s : %s" % (x4, "4"))
            w4.write("\n")
        elif analysis4.sentiment.polarity == 0:
            transformingindia_file4_neutral += 1
            w4.write("%s : %s" % (x4, "2"))
            w4.write("\n")
        else:
            transformingindia_file4_negative += 1
            w4.write("%s : %s" % (x4, "0"))
            w4.write("\n")
    Total_number_transformingindia_sentiment_file_4 = (transformingindia_file4_positive + transformingindia_file4_neutral + transformingindia_file4_negative)
    transformingindia_file4_positive_percentage = (transformingindia_file4_positive*100) / float(1+Total_number_transformingindia_sentiment_file_4)
    transformingindia_file4_neutral__percentage = (transformingindia_file4_neutral*100) / float(1+Total_number_transformingindia_sentiment_file_4)
    transformingindia_file4_negative__percentage = (transformingindia_file4_negative*100) / float(1+Total_number_transformingindia_sentiment_file_4)
    w4.write("Positive Percentage : %s" % str(transformingindia_file4_positive_percentage))
    w4.write("\n")
    w4.write("Neutral Percentage : %s" % str(transformingindia_file4_neutral__percentage))
    w4.write("\n")
    w4.write("Negative Percentage : %s" % str(transformingindia_file4_negative__percentage))
    w4.write("\n")
w4.close()
########################################################################################################################################################################
##9
#################################################################################################################################################################################
nsel_path = "D:/EXPERIMENT/Timing/#nsel"
nsel_file1 = "D:/EXPERIMENT/Timing/#nsel/tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
nsel_file2 = "D:/EXPERIMENT/Timing/#nsel/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
nsel_file3 = "D:/EXPERIMENT/Timing/#nsel/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
nsel_file4 = "D:/EXPERIMENT/Timing/#nsel/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_nsel_file1 = "D:/EXPERIMENT/Timing/#nsel/sentiment_tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
with open(nsel_file1, "r") as ab1:
    data_ab1 = ab1.read().splitlines()
ab1.close()
nsel_file1_positive = 0
nsel_file1_neutral = 0
nsel_file1_negative = 0
with open(sentiment_nsel_file1, "a") as y1:
    for z1 in data_ab1:
        analysis1 = TextBlob(z1)
        if analysis1.sentiment.polarity > 0:
            nsel_file1_positive += 1
            y1.write("%s : %s" % (z1, "4"))
            y1.write("\n")
        elif analysis1.sentiment.polarity == 0:
            nsel_file1_neutral += 1
            y1.write("%s : %s" % (z1, "2"))
            y1.write("\n")
        else:
            nsel_file1_negative += 1
            y1.write("%s : %s" % (z1, "0"))
            y1.write("\n")
    Total_number_nsel_sentiment_file_1 = (nsel_file1_positive + nsel_file1_neutral + nsel_file1_negative)
    nsel_file1_positive_percentage = (nsel_file1_positive*100) / float(1+Total_number_nsel_sentiment_file_1)
    nsel_file1_neutral__percentage = (nsel_file1_neutral*100) / float(1+Total_number_nsel_sentiment_file_1)
    nsel_file1_negative__percentage = (nsel_file1_negative*100) / float(1+Total_number_nsel_sentiment_file_1)
    y1.write("Positive Percentage : %s" % str(nsel_file1_positive_percentage))
    y1.write("\n")
    y1.write("Neutral Percentage : %s" % str(nsel_file1_neutral__percentage))
    y1.write("\n")
    y1.write("Negative Percentage : %s" % str(nsel_file1_negative__percentage))
    y1.write("\n")
y1.close()
#########################################
#nsel_file2 = "D:/EXPERIMENT/Timing/#nsel/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
###############################################
sentiment_nsel_file2 = "D:/EXPERIMENT/Timing/#nsel/sentiment_tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
with open(nsel_file2, "r") as ab2:
    data_ab2 = ab2.read().splitlines()
ab2.close()
nsel_file2_positive = 0
nsel_file2_neutral = 0
nsel_file2_negative = 0
with open(sentiment_nsel_file2, "a") as y2:
    for z2 in data_ab2:
        analysis2 = TextBlob(z2)
        if analysis2.sentiment.polarity > 0:
            nsel_file2_positive += 1
            y2.write("%s : %s" % (z2, "4"))
            y2.write("\n")
        elif analysis2.sentiment.polarity == 0:
            nsel_file2_neutral += 1
            y2.write("%s : %s" % (z2, "2"))
            y2.write("\n")
        else:
            nsel_file2_negative += 1
            y2.write("%s : %s" % (z2, "0"))
            y2.write("\n")
    Total_number_nsel_sentiment_file_2 = (nsel_file2_positive + nsel_file2_neutral + nsel_file2_negative)
    nsel_file2_positive_percentage = (nsel_file2_positive*100) / float(1+Total_number_nsel_sentiment_file_2)
    nsel_file2_neutral__percentage = (nsel_file2_neutral*100) / float(1+Total_number_nsel_sentiment_file_2)
    nsel_file2_negative__percentage = (nsel_file2_negative*100) / float(1+Total_number_nsel_sentiment_file_2)
    y2.write("Positive Percentage : %s" % str(nsel_file2_positive_percentage))
    y2.write("\n")
    y2.write("Neutral Percentage : %s" % str(nsel_file2_neutral__percentage))
    y2.write("\n")
    y2.write("Negative Percentage : %s" % str(nsel_file2_negative__percentage))
    y2.write("\n")
y2.close()
#############################################
#nsel_file3 = "D:/EXPERIMENT/Timing/#nsel/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
###############################################
sentiment_nsel_file3 = "D:/EXPERIMENT/Timing/#nsel/sentiment_tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
with open(nsel_file3, "r") as ab3:
    data_ab3 = ab3.read().splitlines()
ab3.close()
nsel_file3_positive = 0
nsel_file3_neutral = 0
nsel_file3_negative = 0
with open(sentiment_nsel_file3, "a") as y3:
    for z3 in data_ab3:
        analysis3 = TextBlob(z3)
        if analysis3.sentiment.polarity > 0:
            nsel_file3_positive += 1
            y3.write("%s : %s" % (z3, "4"))
            y3.write("\n")
        elif analysis3.sentiment.polarity == 0:
            nsel_file3_neutral += 1
            y3.write("%s : %s" % (z3, "2"))
            y3.write("\n")
        else:
            nsel_file3_negative += 1
            y3.write("%s : %s" % (z3, "0"))
            y3.write("\n")
    Total_number_nsel_sentiment_file_3 = (nsel_file3_positive + nsel_file3_neutral + nsel_file3_negative)
    nsel_file3_positive_percentage = (nsel_file3_positive*100) / float(1+Total_number_nsel_sentiment_file_3)
    nsel_file3_neutral__percentage = (nsel_file3_neutral*100) / float(1+Total_number_nsel_sentiment_file_3)
    nsel_file3_negative__percentage = (nsel_file3_negative*100) / float(1+Total_number_nsel_sentiment_file_3)
    y3.write("Positive Percentage : %s" % str(nsel_file3_positive_percentage))
    y3.write("\n")
    y3.write("Neutral Percentage : %s" % str(nsel_file3_neutral__percentage))
    y3.write("\n")
    y3.write("Negative Percentage : %s" % str(nsel_file3_negative__percentage))
    y3.write("\n")
y3.close()
#############################################
#nsel_file4 = "D:/EXPERIMENT/Timing/#nsel/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_nsel_file4 = "D:/EXPERIMENT/Timing/#nsel/sentiment_tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
with open(nsel_file4, "r") as ab4:
    data_ab4 = ab4.read().splitlines()
ab4.close()
nsel_file4_positive = 0
nsel_file4_neutral = 0
nsel_file4_negative = 0
with open(sentiment_nsel_file4, "a") as y4:
    for z4 in data_ab4:
        analysis4 = TextBlob(z4)
        if analysis4.sentiment.polarity > 0:
            nsel_file4_positive += 1
            y4.write("%s : %s" % (z4, "4"))
            y4.write("\n")
        elif analysis4.sentiment.polarity == 0:
            nsel_file4_neutral += 1
            y4.write("%s : %s" % (z4, "2"))
            y4.write("\n")
        else:
            nsel_file4_negative += 1
            y4.write("%s : %s" % (z4, "0"))
            y4.write("\n")
    Total_number_nsel_sentiment_file_4 = (nsel_file4_positive + nsel_file4_neutral + nsel_file4_negative)
    nsel_file4_positive_percentage = (nsel_file4_positive*100) / float(1+Total_number_nsel_sentiment_file_4)
    nsel_file4_neutral__percentage = (nsel_file4_neutral*100) / float(1+Total_number_nsel_sentiment_file_4)
    nsel_file4_negative__percentage = (nsel_file4_negative*100) / float(1+Total_number_nsel_sentiment_file_4)
    y4.write("Positive Percentage : %s" % str(nsel_file4_positive_percentage))
    y4.write("\n")
    y4.write("Neutral Percentage : %s" % str(nsel_file4_neutral__percentage))
    y4.write("\n")
    y4.write("Negative Percentage : %s" % str(nsel_file4_negative__percentage))
    y4.write("\n")
y4.close()
########################################################################################################################################################################
##10
#################################################################################################################################################################################
satyagrah4men_path = "D:/EXPERIMENT/Timing/#satyagrah4men"
satyagrah4men_file1 = "D:/EXPERIMENT/Timing/#satyagrah4men/tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
satyagrah4men_file2 = "D:/EXPERIMENT/Timing/#satyagrah4men/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
satyagrah4men_file3 = "D:/EXPERIMENT/Timing/#satyagrah4men/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
satyagrah4men_file4 = "D:/EXPERIMENT/Timing/#satyagrah4men/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_satyagrah4men_file1 = "D:/EXPERIMENT/Timing/#satyagrah4men/sentiment_tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
with open(satyagrah4men_file1, "r") as as1:
    data_as1 = as1.read().splitlines()
as1.close()
satyagrah4men_file1_positive = 0
satyagrah4men_file1_neutral = 0
satyagrah4men_file1_negative = 0
with open(sentiment_satyagrah4men_file1, "a") as bs1:
    for cs1 in data_as1:
        analysis1 = TextBlob(cs1)
        if analysis1.sentiment.polarity > 0:
            satyagrah4men_file1_positive += 1
            bs1.write("%s : %s" % (cs1, "4"))
            bs1.write("\n")
        elif analysis1.sentiment.polarity == 0:
            satyagrah4men_file1_neutral += 1
            bs1.write("%s : %s" % (cs1, "2"))
            bs1.write("\n")
        else:
            satyagrah4men_file1_negative += 1
            bs1.write("%s : %s" % (cs1, "0"))
            bs1.write("\n")
    Total_number_satyagrah4men_sentiment_file_1 = (satyagrah4men_file1_positive + satyagrah4men_file1_neutral + satyagrah4men_file1_negative)
    satyagrah4men_file1_positive_percentage = (satyagrah4men_file1_positive*100) / float(1+Total_number_satyagrah4men_sentiment_file_1)
    satyagrah4men_file1_neutral__percentage = (satyagrah4men_file1_neutral*100) / float(1+Total_number_satyagrah4men_sentiment_file_1)
    satyagrah4men_file1_negative__percentage = (satyagrah4men_file1_negative*100) / float(1+Total_number_satyagrah4men_sentiment_file_1)
    bs1.write("Positive Percentage : %s" % str(satyagrah4men_file1_positive_percentage))
    bs1.write("\n")
    bs1.write("Neutral Percentage : %s" % str(satyagrah4men_file1_neutral__percentage))
    bs1.write("\n")
    bs1.write("Negative Percentage : %s" % str(satyagrah4men_file1_negative__percentage))
    bs1.write("\n")
bs1.close()
#########################################
#satyagrah4men_file2 = "D:/EXPERIMENT/Timing/#satyagrah4men/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
###############################################
sentiment_satyagrah4men_file2 = "D:/EXPERIMENT/Timing/#satyagrah4men/sentiment_tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
with open(satyagrah4men_file2, "r") as as2:
    data_as2 = as2.read().splitlines()
as2.close()
satyagrah4men_file2_positive = 0
satyagrah4men_file2_neutral = 0
satyagrah4men_file2_negative = 0
with open(sentiment_satyagrah4men_file2, "a") as bs2:
    for cs2 in data_as2:
        analysis2 = TextBlob(cs2)
        if analysis2.sentiment.polarity > 0:
            satyagrah4men_file2_positive += 1
            bs2.write("%s : %s" % (cs2, "4"))
            bs2.write("\n")
        elif analysis2.sentiment.polarity == 0:
            satyagrah4men_file2_neutral += 1
            bs2.write("%s : %s" % (cs2, "2"))
            bs2.write("\n")
        else:
            satyagrah4men_file2_negative += 1
            bs2.write("%s : %s" % (cs2, "0"))
            bs2.write("\n")
    Total_number_satyagrah4men_sentiment_file_2 = (satyagrah4men_file2_positive + satyagrah4men_file2_neutral + satyagrah4men_file2_negative)
    satyagrah4men_file2_positive_percentage = (satyagrah4men_file2_positive*100) / float(1+Total_number_satyagrah4men_sentiment_file_2)
    satyagrah4men_file2_neutral__percentage = (satyagrah4men_file2_neutral*100) / float(1+Total_number_satyagrah4men_sentiment_file_2)
    satyagrah4men_file2_negative__percentage = (satyagrah4men_file2_negative*100) / float(1+Total_number_satyagrah4men_sentiment_file_2)
    bs2.write("Positive Percentage : %s" % str(satyagrah4men_file2_positive_percentage))
    bs2.write("\n")
    bs2.write("Neutral Percentage : %s" % str(satyagrah4men_file2_neutral__percentage))
    bs2.write("\n")
    bs2.write("Negative Percentage : %s" % str(satyagrah4men_file2_negative__percentage))
    bs2.write("\n")
bs2.close()
#############################################
#satyagrah4men_file3 = "D:/EXPERIMENT/Timing/#satyagrah4men/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
###############################################
sentiment_satyagrah4men_file3 = "D:/EXPERIMENT/Timing/#satyagrah4men/sentiment_tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
with open(satyagrah4men_file3, "r") as as3:
    data_as3 = as3.read().splitlines()
as3.close()
satyagrah4men_file3_positive = 0
satyagrah4men_file3_neutral = 0
satyagrah4men_file3_negative = 0
with open(sentiment_satyagrah4men_file3, "a") as bs3:
    for cs3 in data_as3:
        analysis3 = TextBlob(cs3)
        if analysis3.sentiment.polarity > 0:
            satyagrah4men_file3_positive += 1
            bs3.write("%s : %s" % (cs3, "4"))
            bs3.write("\n")
        elif analysis3.sentiment.polarity == 0:
            satyagrah4men_file3_neutral += 1
            bs3.write("%s : %s" % (cs3, "2"))
            bs3.write("\n")
        else:
            satyagrah4men_file3_negative += 1
            bs3.write("%s : %s" % (cs3, "0"))
            bs3.write("\n")
    Total_number_satyagrah4men_sentiment_file_3 = (satyagrah4men_file3_positive + satyagrah4men_file3_neutral + satyagrah4men_file3_negative)
    satyagrah4men_file3_positive_percentage = (satyagrah4men_file3_positive*100) / float(1+Total_number_satyagrah4men_sentiment_file_3)
    satyagrah4men_file3_neutral__percentage = (satyagrah4men_file3_neutral*100) / float(1+Total_number_satyagrah4men_sentiment_file_3)
    satyagrah4men_file3_negative__percentage = (satyagrah4men_file3_negative*100) / float(1+Total_number_satyagrah4men_sentiment_file_3)
    bs3.write("Positive Percentage : %s" % str(satyagrah4men_file3_positive_percentage))
    bs3.write("\n")
    bs3.write("Neutral Percentage : %s" % str(satyagrah4men_file3_neutral__percentage))
    bs3.write("\n")
    bs3.write("Negative Percentage : %s" % str(satyagrah4men_file3_negative__percentage))
    bs3.write("\n")
bs3.close()
#############################################
#satyagrah4men_file4 = "D:/EXPERIMENT/Timing/#satyagrah4men/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_satyagrah4men_file4 = "D:/EXPERIMENT/Timing/#satyagrah4men/sentiment_tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
with open(satyagrah4men_file4, "r") as as4:
    data_as4 = as4.read().splitlines()
as4.close()
satyagrah4men_file4_positive = 0
satyagrah4men_file4_neutral = 0
satyagrah4men_file4_negative = 0
with open(sentiment_satyagrah4men_file4, "a") as bs4:
    for cs4 in data_as4:
        analysis4 = TextBlob(cs4)
        if analysis4.sentiment.polarity > 0:
            satyagrah4men_file4_positive += 1
            bs4.write("%s : %s" % (cs4, "4"))
            bs4.write("\n")
        elif analysis4.sentiment.polarity == 0:
            satyagrah4men_file4_neutral += 1
            bs4.write("%s : %s" % (cs4, "2"))
            bs4.write("\n")
        else:
            satyagrah4men_file4_negative += 1
            bs4.write("%s : %s" % (cs4, "0"))
            bs4.write("\n")
    Total_number_satyagrah4men_sentiment_file_4 = (satyagrah4men_file4_positive + satyagrah4men_file4_neutral + satyagrah4men_file4_negative)
    satyagrah4men_file4_positive_percentage = (satyagrah4men_file4_positive*100) / float(1+Total_number_satyagrah4men_sentiment_file_4)
    satyagrah4men_file4_neutral__percentage = (satyagrah4men_file4_neutral*100) / float(1+Total_number_satyagrah4men_sentiment_file_4)
    satyagrah4men_file4_negative__percentage = (satyagrah4men_file4_negative*100) / float(1+Total_number_satyagrah4men_sentiment_file_4)
    bs4.write("Positive Percentage : %s" % str(satyagrah4men_file4_positive_percentage))
    bs4.write("\n")
    bs4.write("Neutral Percentage : %s" % str(satyagrah4men_file4_neutral__percentage))
    bs4.write("\n")
    bs4.write("Negative Percentage : %s" % str(satyagrah4men_file4_negative__percentage))
    bs4.write("\n")
bs4.close()
########################################################################################################################################################################
##11

#################################################################################################################################################################################
dreamzgkfraud_path = "D:/EXPERIMENT/Timing/#dreamzgkfraud"
dreamzgkfraud_file1 = "D:/EXPERIMENT/Timing/#dreamzgkfraud/tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
dreamzgkfraud_file2 = "D:/EXPERIMENT/Timing/#dreamzgkfraud/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
dreamzgkfraud_file3 = "D:/EXPERIMENT/Timing/#dreamzgkfraud/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
dreamzgkfraud_file4 = "D:/EXPERIMENT/Timing/#dreamzgkfraud/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_dreamzgkfraud_file1 = "D:/EXPERIMENT/Timing/#dreamzgkfraud/sentiment_tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
with open(dreamzgkfraud_file1, "r") as ae1:
    data_ae1 = ae1.read().splitlines()
ae1.close()
dreamzgkfraud_file1_positive = 0
dreamzgkfraud_file1_neutral = 0
dreamzgkfraud_file1_negative = 0
with open(sentiment_dreamzgkfraud_file1, "a") as be1:
    for ce1 in data_ae1:
        analysis1 = TextBlob(ce1)
        if analysis1.sentiment.polarity > 0:
            dreamzgkfraud_file1_positive += 1
            be1.write("%s : %s" % (ce1, "4"))
            be1.write("\n")
        elif analysis1.sentiment.polarity == 0:
            dreamzgkfraud_file1_neutral += 1
            be1.write("%s : %s" % (ce1, "2"))
            be1.write("\n")
        else:
            dreamzgkfraud_file1_negative += 1
            be1.write("%s : %s" % (ce1, "0"))
            be1.write("\n")
    Total_number_dreamzgkfraud_sentiment_file_1 = (dreamzgkfraud_file1_positive + dreamzgkfraud_file1_neutral + dreamzgkfraud_file1_negative)
    dreamzgkfraud_file1_positive_percentage = (dreamzgkfraud_file1_positive*100) / float(1+Total_number_dreamzgkfraud_sentiment_file_1)
    dreamzgkfraud_file1_neutral__percentage = (dreamzgkfraud_file1_neutral*100) / float(1+Total_number_dreamzgkfraud_sentiment_file_1)
    dreamzgkfraud_file1_negative__percentage = (dreamzgkfraud_file1_negative*100) / float(1+Total_number_dreamzgkfraud_sentiment_file_1)
    be1.write("Positive Percentage : %s" % str(dreamzgkfraud_file1_positive_percentage))
    be1.write("\n")
    be1.write("Neutral Percentage : %s" % str(dreamzgkfraud_file1_neutral__percentage))
    be1.write("\n")
    be1.write("Negative Percentage : %s" % str(dreamzgkfraud_file1_negative__percentage))
    be1.write("\n")
be1.close()
#########################################
#dreamzgkfraud_file2 = "D:/EXPERIMENT/Timing/#dreamzgkfraud/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
###############################################
sentiment_dreamzgkfraud_file2 = "D:/EXPERIMENT/Timing/#dreamzgkfraud/sentiment_tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
with open(dreamzgkfraud_file2, "r") as ae2:
    data_ae2 = ae2.read().splitlines()
ae2.close()
dreamzgkfraud_file2_positive = 0
dreamzgkfraud_file2_neutral = 0
dreamzgkfraud_file2_negative = 0
with open(sentiment_dreamzgkfraud_file2, "a") as be2:
    for ce2 in data_ae2:
        analysis2 = TextBlob(ce2)
        if analysis2.sentiment.polarity > 0:
            dreamzgkfraud_file2_positive += 1
            be2.write("%s : %s" % (ce2, "4"))
            be2.write("\n")
        elif analysis2.sentiment.polarity == 0:
            dreamzgkfraud_file2_neutral += 1
            be2.write("%s : %s" % (ce2, "2"))
            be2.write("\n")
        else:
            dreamzgkfraud_file2_negative += 1
            be2.write("%s : %s" % (ce2, "0"))
            be2.write("\n")
    Total_number_dreamzgkfraud_sentiment_file_2 = (dreamzgkfraud_file2_positive + dreamzgkfraud_file2_neutral + dreamzgkfraud_file2_negative)
    dreamzgkfraud_file2_positive_percentage = (dreamzgkfraud_file2_positive*100) / float(1+Total_number_dreamzgkfraud_sentiment_file_2)
    dreamzgkfraud_file2_neutral__percentage = (dreamzgkfraud_file2_neutral*100) / float(1+Total_number_dreamzgkfraud_sentiment_file_2)
    dreamzgkfraud_file2_negative__percentage = (dreamzgkfraud_file2_negative*100) / float(1+Total_number_dreamzgkfraud_sentiment_file_2)
    be2.write("Positive Percentage : %s" % str(dreamzgkfraud_file2_positive_percentage))
    be2.write("\n")
    be2.write("Neutral Percentage : %s" % str(dreamzgkfraud_file2_neutral__percentage))
    be2.write("\n")
    be2.write("Negative Percentage : %s" % str(dreamzgkfraud_file2_negative__percentage))
    be2.write("\n")
be2.close()
#############################################
#dreamzgkfraud_file3 = "D:/EXPERIMENT/Timing/#dreamzgkfraud/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
###############################################
sentiment_dreamzgkfraud_file3 = "D:/EXPERIMENT/Timing/#dreamzgkfraud/sentiment_tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
with open(dreamzgkfraud_file3, "r") as ae3:
    data_ae3 = ae3.read().splitlines()
ae3.close()
dreamzgkfraud_file3_positive = 0
dreamzgkfraud_file3_neutral = 0
dreamzgkfraud_file3_negative = 0
with open(sentiment_dreamzgkfraud_file3, "a") as be3:
    for ce3 in data_ae3:
        analysis3 = TextBlob(ce3)
        if analysis3.sentiment.polarity > 0:
            dreamzgkfraud_file3_positive += 1
            be3.write("%s : %s" % (ce3, "4"))
            be3.write("\n")
        elif analysis3.sentiment.polarity == 0:
            dreamzgkfraud_file3_neutral += 1
            be3.write("%s : %s" % (ce3, "2"))
            be3.write("\n")
        else:
            dreamzgkfraud_file3_negative += 1
            be3.write("%s : %s" % (ce3, "0"))
            be3.write("\n")
    Total_number_dreamzgkfraud_sentiment_file_3 = (dreamzgkfraud_file3_positive + dreamzgkfraud_file3_neutral + dreamzgkfraud_file3_negative)
    dreamzgkfraud_file3_positive_percentage = (dreamzgkfraud_file3_positive*100) / float(1+Total_number_dreamzgkfraud_sentiment_file_3)
    dreamzgkfraud_file3_neutral__percentage = (dreamzgkfraud_file3_neutral*100) / float(1+Total_number_dreamzgkfraud_sentiment_file_3)
    dreamzgkfraud_file3_negative__percentage = (dreamzgkfraud_file3_negative*100) / float(1+Total_number_dreamzgkfraud_sentiment_file_3)
    be3.write("Positive Percentage : %s" % str(dreamzgkfraud_file3_positive_percentage))
    be3.write("\n")
    be3.write("Neutral Percentage : %s" % str(dreamzgkfraud_file3_neutral__percentage))
    be3.write("\n")
    be3.write("Negative Percentage : %s" % str(dreamzgkfraud_file3_negative__percentage))
    be3.write("\n")
be3.close()
#############################################
#dreamzgkfraud_file4 = "D:/EXPERIMENT/Timing/#dreamzgkfraud/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_dreamzgkfraud_file4 = "D:/EXPERIMENT/Timing/#dreamzgkfraud/sentiment_tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
with open(dreamzgkfraud_file4, "r") as ae4:
    data_ae4 = ae4.read().splitlines()
ae4.close()
dreamzgkfraud_file4_positive = 0
dreamzgkfraud_file4_neutral = 0
dreamzgkfraud_file4_negative = 0
with open(sentiment_dreamzgkfraud_file4, "a") as be4:
    for ce4 in data_ae4:
        analysis4 = TextBlob(ce4)
        if analysis4.sentiment.polarity > 0:
            dreamzgkfraud_file4_positive += 1
            be4.write("%s : %s" % (ce4, "4"))
            be4.write("\n")
        elif analysis4.sentiment.polarity == 0:
            dreamzgkfraud_file4_neutral += 1
            be4.write("%s : %s" % (ce4, "2"))
            be4.write("\n")
        else:
            dreamzgkfraud_file4_negative += 1
            be4.write("%s : %s" % (ce4, "0"))
            be4.write("\n")
    Total_number_dreamzgkfraud_sentiment_file_4 = (dreamzgkfraud_file4_positive + dreamzgkfraud_file4_neutral + dreamzgkfraud_file4_negative)
    dreamzgkfraud_file4_positive_percentage = (dreamzgkfraud_file4_positive*100) / float(1+Total_number_dreamzgkfraud_sentiment_file_4)
    dreamzgkfraud_file4_neutral__percentage = (dreamzgkfraud_file4_neutral*100) / float(1+Total_number_dreamzgkfraud_sentiment_file_4)
    dreamzgkfraud_file4_negative__percentage = (dreamzgkfraud_file4_negative*100) / float(1+Total_number_dreamzgkfraud_sentiment_file_4)
    be4.write("Positive Percentage : %s" % str(dreamzgkfraud_file4_positive_percentage))
    be4.write("\n")
    be4.write("Neutral Percentage : %s" % str(dreamzgkfraud_file4_neutral__percentage))
    be4.write("\n")
    be4.write("Negative Percentage : %s" % str(dreamzgkfraud_file4_negative__percentage))
    be4.write("\n")
be4.close()
########################################################################################################################################################################


























"""
folderPath = ""
folderPath = CommonPath+tag
files = []
files = os.listdir(folderPath)
for file in files:
    with open(file,"r") as f:
        data = f.read().splitlines()
        f.close()
        sentimentFileName = folderPath + "/" + tag + "_" + file
        for d in data:
            analysis = TextBlob(d)
            if analysis.sentiment.polarity > 0:
                with open(sentimentFileName, "a") as g:
                    g.write("%s,%s" % (d, "Positive"))
                    g.write("\n")
                    g.close()
            elif analysis.sentiment.polarity == 0:
                with open(sentimentFileName, "a") as g:
                    g.write("%s,%s" % (d, "Neutral"))
                    g.write("\n")
                    g.close()
            else:
                with open(sentimentFileName, "a") as g:
                    g.write("%s,%s" % (d, "Negative"))
                    g.write("\n")
                    g.close()
"""
