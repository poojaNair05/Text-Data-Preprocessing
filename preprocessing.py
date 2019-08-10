import re
import math
file1=open(r"sample.txt","r")
string = file1.read()
#print (string)
#Read title
sentences = string.split(".")
print(sentences)
l=len(sentences)
'''
removing special characters and removing trailing and leading spaces
and converting each sentence to lower case
NEED TO IMPLEMENT THE PROPER NOUN FEATURE BEFORE THIS
'''
for i in range(l):
    sentence=sentences[i]
    sentences[i]=re.sub(r"[^a-zA-Z0-9]+", ' ', sentence).strip().lower()
    
#print(sentences)

''' implement title  feature'''
dictionary={}#occurence of word in the document
WordInSentence={}#no of sentences in which the word occurs
maxlen=0       #no of words occuring in longest sentence
SentenceLength=[0]*l
i=0
for sentence in sentences:
    words=sentence.split(" ")
    c=0;
    temp={}
    for word in words:
        if(dictionary.get(word)!=None):
            dictionary[word]+=1;
        else:
            dictionary[word]=1
        if(temp.get(word)==None):
            temp[word]=1
            if(WordInSentence.get(word)!=None):
                WordInSentence[word]+=1
            else:
                WordInSentence[word]=1
        c+=1
    SentenceLength[i]=c
    maxlen=max(maxlen,c)
    i+=1

for i in range(l):
    SentenceLength[i]/=maxlen

print(SentenceLength)
#print(type(dictionary))
#FrequencyList is a list containing words sorted according to their frequency
#FrequencyList = [[k, dictionary[k]] for k in sorted(dictionary, key=dictionary.get, reverse=True)]
frequent=sorted(dictionary, key=dictionary.get, reverse=True)
top=10#set this to 10 for actual problem
frequent=frequent[:top]
print(frequent)
'''-------------THEMATIC WEIGHT-------------'''

ThematicWeight=[0]*l;
for i in range(l):
    words=sentences[i].split(" ")
    for word in words:
        if(word in frequent):
            ThematicWeight[i]+=1;
    ThematicWeight[i]/=top
print(ThematicWeight)
TermWeight=[0]*l


'''-------------TERM WEIGHT-------------'''
print("DICTIONARY",dictionary)            
print("WIS",WordInSentence)
print("LENGTH",l)

N=l
maxTW=0#maximum term weight
'''CALCULATING MAXIMUM TERM WEIGHT'''
for i in range(l):
    words=sentences[i].split(" ")
    temp={}
    s=0
    for word in words:
        if(temp.get(word)==None):
            temp[word]=1
            tf=dictionary[word]
            ni=WordInSentence[word]
            if((math.log(ni))!=0): #IF this is not satisified nothing is added
                s+=(tf)*(math.log(N)/math.log(ni))
    TermWeight[i]=s
    print("i",i,"s",s)
    maxTW=max(maxTW,s)
'''CALCULATING TERM WEIGHT FOR EACH'''
print("MAX",maxTW)
for i in range(l):
    TermWeight[i]/=maxTW
print(TermWeight)
