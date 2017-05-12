#import regex
import re
import csv
import nltk
#start process_tweet
def processTweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end

#Read the tweets one by one and process it
#D:/EXPERIMENT


#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
#end

#start getStopWordList
def getStopWordList(stopWordListFileName):
    #read the stopwords file and build a list
    stopWords = []
    stopWords.append('AT_USER')
    stopWords.append('URL')

    fp = open(stopWordListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    return stopWords
#end

#start getfeatureVector
def getFeatureVector(tweet, stopWords):
    featureVector = []
    #split tweet into words
    words = tweet.split()
    for w in words:
        #replace two or more with two occurrences
        w = replaceTwoOrMore(w)
        #strip punctuation
        w = w.strip('\'"?,.')
        #check if the word stats with an alphabet
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        #ignore if it is a stop word
        if(w in stopWords or val is None):
            continue
        else:
            featureVector.append(w.lower())
    return featureVector
#end

#Read the tweets one by one and process it

#start extract_features
def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in tweet_words)
    return features
#end

"""
# here 0: Negative , 2: Neutral , 4: Positive

fp = csv.reader(open('D:/EXPERIMENT/testdata.csv', 'r'), delimiter=',', quotechar='|')
processedTweets = []
for each_row in fp:
    TweetSentimentinNumeral = int(each_row[0][1:-1])
    processedTweetFromInput = processTweet(each_row[5])
    processedTweets.append((processedTweetFromInput,TweetSentimentinNumeral))


"""
stopWords = getStopWordList('D:/EXPERIMENT/stopwords.txt')
# here 0: Negative , 2: Neutral , 4: Positive
inputTweets = csv.reader(open('D:/EXPERIMENT/testdata.csv', 'r'), delimiter=',', quotechar='|')
tweets = []
featureList = []
for each_row in inputTweets:
    sentiment_num = int(each_row[0][1:-1])
    #print("sentiment_num",sentiment_num)
    tweet = processTweet(each_row[5])
    processedTweet = processTweet(tweet)
    #print("processedTweet", processedTweet)
    featureVector = getFeatureVector(processedTweet, stopWords)
    featureList.extend(featureVector)
    tweets.append((featureVector, sentiment_num))
#end loop

# Remove featureList duplicates
featureList = list(set(featureList))

print("featureList",featureList)

#print("tweets", tweets)
#print("featureList",featureList)
# Extract feature vector for all tweets in one shote
training_set = nltk.classify.util.apply_features(extract_features, tweets)

#print("training_set", training_set)

# Train the classifier
NBClassifier = nltk.NaiveBayesClassifier.train(training_set)

# Test the classifier
testTweet = 'using Linux and loving it - so much nicer than windows... Looking forward to using the wysiwyg latex editor!'
processedTestTweet = processTweet(testTweet)
print ("First",NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet,stopWords))))
print (NBClassifier.show_most_informative_features(10))
testTweet = 'Trouble in Iran, I see. Hmm. Iran. Iran so far away. #flockofseagullsweregeopoliticallycorrect'
processedTestTweet = processTweet(testTweet)
print ("Second",NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet,stopWords))))

#################################################################################################################################################################################
lahukalagaan_path = "D:/EXPERIMENT/Timing2/#lahukalagaan"
lahukalagaan_file1 = "D:/EXPERIMENT/Timing/#lahukalagaan/tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
lahukalagaan_file2 = "D:/EXPERIMENT/Timing/#lahukalagaan/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
lahukalagaan_file3 = "D:/EXPERIMENT/Timing/#lahukalagaan/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
lahukalagaan_file4 = "D:/EXPERIMENT/Timing/#lahukalagaan/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_lahukalagaan_file1 = "D:/EXPERIMENT/Timing2/#lahukalagaan/sentiment_tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
with open(lahukalagaan_file1, "r") as a:
    data_a = a.read().splitlines()
a.close()
lahukalagaan_file1_positive = 0
lahukalagaan_file1_neutral = 0
lahukalagaan_file1_negative = 0
# here 0: Negative , 2: Neutral , 4: Positive
with open(sentiment_lahukalagaan_file1, "a") as b:
    for c in data_a:
        analysis = NBClassifier.classify(extract_features(getFeatureVector(processTweet(c),stopWords)))
        print("analysis",analysis)
        if analysis == 4:
            lahukalagaan_file1_positive += 1
            b.write("%s : %s" % (c, "4"))
            b.write("\n")
        elif analysis == 2:
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
sentiment_lahukalagaan_file2 = "D:/EXPERIMENT/Timing2/#lahukalagaan/sentiment_tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
with open(lahukalagaan_file2, "r") as a2:
    data_a2 = a2.read().splitlines()
a2.close()
lahukalagaan_file2_positive = 0
lahukalagaan_file2_neutral = 0
lahukalagaan_file2_negative = 0
with open(sentiment_lahukalagaan_file2, "a") as b2:
    for c2 in data_a2:
        analysis2 = NBClassifier.classify(extract_features(getFeatureVector(processTweet(c2),stopWords)))
        if analysis2 == 4:
            lahukalagaan_file2_positive += 1
            b2.write("%s : %s" % (c2, "4"))
            b2.write("\n")
        elif analysis2 == 2:
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
sentiment_lahukalagaan_file3 = "D:/EXPERIMENT/Timing2/#lahukalagaan/sentiment_tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
with open(lahukalagaan_file3, "r") as a3:
    data_a3 = a3.read().splitlines()
a3.close()
lahukalagaan_file3_positive = 0
lahukalagaan_file3_neutral = 0
lahukalagaan_file3_negative = 0
with open(sentiment_lahukalagaan_file3, "a") as b3:
    for c3 in data_a3:
        analysis3 = NBClassifier.classify(extract_features(getFeatureVector(processTweet(c3),stopWords)))
        if analysis3 == 4:
            lahukalagaan_file3_positive += 1
            b3.write("%s : %s" % (c3, "4"))
            b3.write("\n")
        elif analysis3 == 2:
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
sentiment_lahukalagaan_file4 = "D:/EXPERIMENT/Timing2/#lahukalagaan/sentiment_tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
with open(lahukalagaan_file4, "r") as a4:
    data_a4 = a4.read().splitlines()
a4.close()
lahukalagaan_file4_positive = 0
lahukalagaan_file4_neutral = 0
lahukalagaan_file4_negative = 0
with open(sentiment_lahukalagaan_file4, "a") as b4:
    for c4 in data_a4:
        analysis4 = NBClassifier.classify(extract_features(getFeatureVector(processTweet(c4),stopWords)))
        if analysis4 == 4:
            lahukalagaan_file4_positive += 1
            b4.write("%s : %s" % (c4, "4"))
            b4.write("\n")
        elif analysis4 == 2:
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
bjymnec_path = "D:/EXPERIMENT/Timing2/#bjymnec"
bjymnec_file1 = "D:/EXPERIMENT/Timing/#bjymnec/tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
bjymnec_file2 = "D:/EXPERIMENT/Timing/#bjymnec/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
bjymnec_file3 = "D:/EXPERIMENT/Timing/#bjymnec/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
bjymnec_file4 = "D:/EXPERIMENT/Timing/#bjymnec/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
# here 0: Negative , 2: Neutral , 4: Positive
sentiment_bjymnec_file1 = "D:/EXPERIMENT/Timing2/#bjymnec/sentiment_tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
with open(bjymnec_file1, "r") as d1:
    data_d1 = d1.read().splitlines()
d1.close()
bjymnec_file1_positive = 0
bjymnec_file1_neutral = 0
bjymnec_file1_negative = 0
with open(sentiment_bjymnec_file1, "a") as e1:
    for f1 in data_d1:
        analysis1 = NBClassifier.classify(extract_features(getFeatureVector(processTweet(f1),stopWords)))
        if analysis1 == 4:
            bjymnec_file1_positive += 1
            e1.write("%s : %s" % (f1, "4"))
            e1.write("\n")
        elif analysis1 == 2:
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
sentiment_bjymnec_file2 = "D:/EXPERIMENT/Timing2/#bjymnec/sentiment_tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
with open(bjymnec_file2, "r") as d2:
    data_d2 = d2.read().splitlines()
d2.close()
bjymnec_file2_positive = 0
bjymnec_file2_neutral = 0
bjymnec_file2_negative = 0
with open(sentiment_bjymnec_file2, "a") as e2:
    for f2 in data_d2:
        analysis2 = NBClassifier.classify(extract_features(getFeatureVector(processTweet(f2),stopWords)))
        if analysis2 == 4:
            bjymnec_file2_positive += 1
            e2.write("%s : %s" % (f2, "4"))
            e2.write("\n")
        elif analysis2 == 2:
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
sentiment_bjymnec_file3 = "D:/EXPERIMENT/Timing2/#bjymnec/sentiment_tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
with open(bjymnec_file3, "r") as d3:
    data_d3 = d3.read().splitlines()
d3.close()
bjymnec_file3_positive = 0
bjymnec_file3_neutral = 0
bjymnec_file3_negative = 0
with open(sentiment_bjymnec_file3, "a") as e3:
    for f3 in data_d3:
        analysis3 = NBClassifier.classify(extract_features(getFeatureVector(processTweet(f3),stopWords)))
        if analysis3 == 4:
            bjymnec_file3_positive += 1
            e3.write("%s : %s" % (f3, "4"))
            e3.write("\n")
        elif analysis3 == 2:
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
sentiment_bjymnec_file4 = "D:/EXPERIMENT/Timing2/#bjymnec/sentiment_tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
with open(bjymnec_file4, "r") as d4:
    data_d4 = d4.read().splitlines()
d4.close()
bjymnec_file4_positive = 0
bjymnec_file4_neutral = 0
bjymnec_file4_negative = 0
with open(sentiment_bjymnec_file4, "a") as e4:
    for f4 in data_d4:
        analysis4 = NBClassifier.classify(extract_features(getFeatureVector(processTweet(f4),stopWords)))
        if analysis4 == 4:
            bjymnec_file4_positive += 1
            e4.write("%s : %s" % (f4, "4"))
            e4.write("\n")
        elif analysis4 == 2:
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
sentiment_vijaymallya_file1 = "D:/EXPERIMENT/Timing2/#vijaymallya/sentiment_tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
with open(vijaymallya_file1, "r") as g1:
    data_g1 = g1.read().splitlines()
g1.close()
vijaymallya_file1_positive = 0
vijaymallya_file1_neutral = 0
vijaymallya_file1_negative = 0
with open(sentiment_vijaymallya_file1, "a") as h1:
    for i1 in data_g1:
        analysis1 = NBClassifier.classify(extract_features(getFeatureVector(processTweet(i1),stopWords)))
        if analysis1 == 4:
            vijaymallya_file1_positive += 1
            h1.write("%s : %s" % (i1, "4"))
            h1.write("\n")
        elif analysis1 == 2:
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
sentiment_vijaymallya_file2 = "D:/EXPERIMENT/Timing2/#vijaymallya/sentiment_tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
with open(vijaymallya_file2, "r") as g2:
    data_g2 = g2.read().splitlines()
g2.close()
vijaymallya_file2_positive = 0
vijaymallya_file2_neutral = 0
vijaymallya_file2_negative = 0
with open(sentiment_vijaymallya_file2, "a") as h2:
    for i2 in data_g2:
        analysis2 = NBClassifier.classify(extract_features(getFeatureVector(processTweet(i2),stopWords)))
        if analysis2 == 4:
            vijaymallya_file2_positive += 1
            h2.write("%s : %s" % (i2, "4"))
            h2.write("\n")
        elif analysis2 == 2:
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
sentiment_vijaymallya_file3 = "D:/EXPERIMENT/Timing2/#vijaymallya/sentiment_tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
with open(vijaymallya_file3, "r") as g3:
    data_g3 = g3.read().splitlines()
g3.close()
vijaymallya_file3_positive = 0
vijaymallya_file3_neutral = 0
vijaymallya_file3_negative = 0
with open(sentiment_vijaymallya_file3, "a") as h3:
    for i3 in data_g3:
        analysis3 = NBClassifier.classify(extract_features(getFeatureVector(processTweet(i3),stopWords)))
        if analysis3 == 4:
            vijaymallya_file3_positive += 1
            h3.write("%s : %s" % (i3, "4"))
            h3.write("\n")
        elif analysis3 == 2:
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
sentiment_vijaymallya_file4 = "D:/EXPERIMENT/Timing2/#vijaymallya/sentiment_tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
with open(vijaymallya_file4, "r") as g4:
    data_g4 = g4.read().splitlines()
g4.close()
vijaymallya_file4_positive = 0
vijaymallya_file4_neutral = 0
vijaymallya_file4_negative = 0
with open(sentiment_vijaymallya_file4, "a") as h4:
    for i4 in data_g4:
        analysis4 = NBClassifier.classify(extract_features(getFeatureVector(processTweet(i4),stopWords)))
        if analysis4 == 4:
            vijaymallya_file4_positive += 1
            h4.write("%s : %s" % (i4, "4"))
            h4.write("\n")
        elif analysis4 == 2:
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
##6
#################################################################################################################################################################################
makeinindia_path = "D:/EXPERIMENT/Timing/#makeinindia"
makeinindia_file1 = "D:/EXPERIMENT/Timing/#makeinindia/tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
makeinindia_file2 = "D:/EXPERIMENT/Timing/#makeinindia/tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
makeinindia_file3 = "D:/EXPERIMENT/Timing/#makeinindia/tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
makeinindia_file4 = "D:/EXPERIMENT/Timing/#makeinindia/tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
###############################################
sentiment_makeinindia_file1 = "D:/EXPERIMENT/Timing2/#makeinindia/sentiment_tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
with open(makeinindia_file1, "r") as p1:
    data_p1 = p1.read().splitlines()
p1.close()
makeinindia_file1_positive = 0
makeinindia_file1_neutral = 0
makeinindia_file1_negative = 0
with open(sentiment_makeinindia_file1, "a") as q1:
    for r1 in data_p1:
        analysis1 = NBClassifier.classify(extract_features(getFeatureVector(processTweet(r1),stopWords)))
        if analysis1 == 4:
            makeinindia_file1_positive += 1
            q1.write("%s : %s" % (r1, "4"))
            q1.write("\n")
        elif analysis1 == 2:
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
sentiment_makeinindia_file2 = "D:/EXPERIMENT/Timing2/#makeinindia/sentiment_tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
with open(makeinindia_file2, "r") as p2:
    data_p2 = p2.read().splitlines()
p2.close()
makeinindia_file2_positive = 0
makeinindia_file2_neutral = 0
makeinindia_file2_negative = 0
with open(sentiment_makeinindia_file2, "a") as q2:
    for r2 in data_p2:
        analysis2 = NBClassifier.classify(extract_features(getFeatureVector(processTweet(r2),stopWords)))
        if analysis2 == 4:
            makeinindia_file2_positive += 1
            q2.write("%s : %s" % (r2, "4"))
            q2.write("\n")
        elif analysis2 == 2:
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
sentiment_makeinindia_file3 = "D:/EXPERIMENT/Timing2/#makeinindia/sentiment_tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
with open(makeinindia_file3, "r") as p3:
    data_p3 = p3.read().splitlines()
p3.close()
makeinindia_file3_positive = 0
makeinindia_file3_neutral = 0
makeinindia_file3_negative = 0
with open(sentiment_makeinindia_file3, "a") as q3:
    for r3 in data_p3:
        analysis3 = NBClassifier.classify(extract_features(getFeatureVector(processTweet(r3),stopWords)))
        if analysis3 == 4:
            makeinindia_file3_positive += 1
            q3.write("%s : %s" % (r3, "4"))
            q3.write("\n")
        elif analysis3 == 2:
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
sentiment_makeinindia_file4 = "D:/EXPERIMENT/Timing2/#makeinindia/sentiment_tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
with open(makeinindia_file4, "r") as p4:
    data_p4 = p4.read().splitlines()
p4.close()
makeinindia_file4_positive = 0
makeinindia_file4_neutral = 0
makeinindia_file4_negative = 0
with open(sentiment_makeinindia_file4, "a") as q4:
    for r4 in data_p4:
        analysis4 = NBClassifier.classify(extract_features(getFeatureVector(processTweet(r4),stopWords)))
        if analysis4 == 4:
            makeinindia_file4_positive += 1
            q4.write("%s : %s" % (r4, "4"))
            q4.write("\n")
        elif analysis4 == 2:
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
sentiment_privateschoolfeehikeatrocity_file1 = "D:/EXPERIMENT/Timing2/#privateschoolfeehikeatrocity/sentiment_tweetsDB_day1_18APR_7_45AM_8_45AM.txt"
with open(privateschoolfeehikeatrocity_file1, "r") as s1:
    data_s1 = s1.read().splitlines()
s1.close()
privateschoolfeehikeatrocity_file1_positive = 0
privateschoolfeehikeatrocity_file1_neutral = 0
privateschoolfeehikeatrocity_file1_negative = 0
with open(sentiment_privateschoolfeehikeatrocity_file1, "a") as t1:
    for u1 in data_s1:
        analysis1 = NBClassifier.classify(extract_features(getFeatureVector(processTweet(u1),stopWords)))
        if analysis1 == 4:
            privateschoolfeehikeatrocity_file1_positive += 1
            t1.write("%s : %s" % (u1, "4"))
            t1.write("\n")
        elif analysis1 == 2:
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
sentiment_privateschoolfeehikeatrocity_file2 = "D:/EXPERIMENT/Timing2/#privateschoolfeehikeatrocity/sentiment_tweetsDB_day1_18APR_7_30PM_9_30PM.txt"
with open(privateschoolfeehikeatrocity_file2, "r") as s2:
    data_s2 = s2.read().splitlines()
s2.close()
privateschoolfeehikeatrocity_file2_positive = 0
privateschoolfeehikeatrocity_file2_neutral = 0
privateschoolfeehikeatrocity_file2_negative = 0
with open(sentiment_privateschoolfeehikeatrocity_file2, "a") as t2:
    for u2 in data_s2:
        analysis2 = NBClassifier.classify(extract_features(getFeatureVector(processTweet(u2),stopWords)))
        if analysis2 == 4:
            privateschoolfeehikeatrocity_file2_positive += 1
            t2.write("%s : %s" % (u2, "4"))
            t2.write("\n")
        elif analysis2 == 2:
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
sentiment_privateschoolfeehikeatrocity_file3 = "D:/EXPERIMENT/Timing2/#privateschoolfeehikeatrocity/sentiment_tweetsDB_day1_18APR_10_00PM_12_00PM.txt"
with open(privateschoolfeehikeatrocity_file3, "r") as s3:
    data_s3 = s3.read().splitlines()
s3.close()
privateschoolfeehikeatrocity_file3_positive = 0
privateschoolfeehikeatrocity_file3_neutral = 0
privateschoolfeehikeatrocity_file3_negative = 0
with open(sentiment_privateschoolfeehikeatrocity_file3, "a") as t3:
    for u3 in data_s3:
        analysis3 = NBClassifier.classify(extract_features(getFeatureVector(processTweet(u3),stopWords)))
        if analysis3 == 4:
            privateschoolfeehikeatrocity_file3_positive += 1
            t3.write("%s : %s" % (u3, "4"))
            t3.write("\n")
        elif analysis3 == 2:
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
sentiment_privateschoolfeehikeatrocity_file4 = "D:/EXPERIMENT/Timing2/#privateschoolfeehikeatrocity/sentiment_tweetsDB_day1_19APR_12_00AM_02_00AM.txt"
with open(privateschoolfeehikeatrocity_file4, "r") as s4:
    data_s4 = s4.read().splitlines()
s4.close()
privateschoolfeehikeatrocity_file4_positive = 0
privateschoolfeehikeatrocity_file4_neutral = 0
privateschoolfeehikeatrocity_file4_negative = 0
with open(sentiment_privateschoolfeehikeatrocity_file4, "a") as t4:
    for u4 in data_s4:
        analysis4 = NBClassifier.classify(extract_features(getFeatureVector(processTweet(u4),stopWords)))
        if analysis4 == 4:
            privateschoolfeehikeatrocity_file4_positive += 1
            t4.write("%s : %s" % (u4, "4"))
            t4.write("\n")
        elif analysis4 == 2:
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


