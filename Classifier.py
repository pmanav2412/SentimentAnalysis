from lib2to3.pgen2 import token
from xml.etree import ElementTree as ET
import collections
import nltk

#tree = ET.parse ('Feb17_GroupB.txt.xml')
tree = ET.parse ('Feb17_GroupA.txt_original.xml')
root = tree.getroot ()
e = 0

m_Count = 0
l_Count = 0
r_Count = 0
mod_Count = 0
aly_Count = 0
mel_Count = 0
car_Count = 0
ted_Count = 0
Count = 0

Count = 0
#d = {1: 'meg', 2: 'lynn', 3: 'rita', 4: 'moderator', 5: 'alyssa', 6: 'melany', 7: 'caroline', 8: 'ted'}

# below list for the second data file
d = {1: 'david', 2: 'rick', 3: 'vicky', 4: 'julie', 5: 'leah', 6: 'macy', 7: 'moderator'}
j = 0
'''
for i in range (len (root[0][0])):
    id = root[0][0][i][0][0][0].text
    for a, b in d.items ():
        if id == b:
            j = a
            break

    if j == 1:

        for POS in root[0][0][i].iter ('POS'):

            if POS.text == 'PRP':
                m_Count = m_Count + 1
            elif POS.text == 'PRP$':
                m_Count = m_Count + 1
    elif j == 2

        for POS in root[0][0][i].iter ('POS'):

            if POS.text == 'PRP':
                l_Count = l_Count + 1
            elif POS.text == 'PRP$':
                l_Count = l_Count + 1
    elif j == 3:

        for POS in root[0][0][i].iter ('POS'):

            if POS.text == 'PRP':
                r_Count = r_Count + 1
            elif POS.text == 'PRP$':
                r_Count = r_Count + 1
    elif j == 4:

        for POS in root[0][0][i].iter ('POS'):

            if POS.text == 'PRP':
                mod_Count = mod_Count + 1
            elif POS.text == 'PRP$':
                mod_Count = mod_Count + 1
    elif j == 5:

        for POS in root[0][0][i].iter ('POS'):

            if POS.text == 'PRP':
                aly_Count = aly_Count + 1
            elif POS.text == 'PRP$':
                aly_Count = aly_Count + 1
    elif j == 6:

        for POS in root[0][0][i].iter ('POS'):

            if POS.text == 'PRP':
                mel_Count = mel_Count + 1
            elif POS.text == 'PRP$':
                mel_Count = mel_Count + 1
    elif j == 7:

        for POS in root[0][0][i].iter ('POS'):

            if POS.text == 'PRP':
                car_Count = car_Count + 1
            elif POS.text == 'PRP$':
                car_Count = car_Count + 1
    elif j == 8:

        for POS in root[0][0][i].iter ('POS'):

            if POS.text == 'PRP':
                ted_Count = ted_Count + 1
            elif POS.text == 'PRP$':
                ted_Count = ted_Count + 1
    else:

        for POS in root[0][0][i].iter ('POS'):

            if POS.text == 'PRP':
                Count = Count + 1
            elif POS.text == 'PRP$':
                Count = Count + 1

print ('\n')
print ('OUTPUT VALUE FOR FEB17_GroupA.txt \n')
print ('meg=      ', m_Count)
print ('lynn=     ', l_Count)
print ('moderator=', mod_Count)
print ('rita=     ', r_Count)
print ('alyssa=   ', aly_Count)
print ('melany=   ', mel_Count)
print ('caroline= ', car_Count)
print ('ted=      ', ted_Count)

t_Count = m_Count + l_Count + mod_Count + r_Count + aly_Count + mel_Count + car_Count + ted_Count
print ('Addition of all the pronoun spoken by all the participant = ', t_Count, '\n')

total_Count = 0
for POS in root[0][0].iter ('POS'):
    # print(POS.text)
    if POS.text == 'PRP':
        total_Count = total_Count + 1
    elif POS.text == 'PRP$':
        total_Count = total_Count + 1

print ('Total pronoun spoken by all the participant=', total_Count)
'''

# print(root.findall("./document/sentences/sentence[word='meg']"))


#find the turn length

mod_tw=0

id = root[0][0][3][0][0].get ('id')
print ('this is id= ',id, root[0][0][3][0][0],len(root[0][0][3][0]))
for i in range(len(root[0][0])):
    mod=root[0][0][i][0][0][0].text
    if mod == "moderator":
        mod_tw=mod_tw+len(root[0][0][i][0])
        e=e+1

list=[0.231,0.226,0.117 ]
(float)a=0
for i in list:
    a=a+list[i]

print(a)
print(e,mod_tw)




#get the list of all the noun and participant
p = 0
List_Name = list()
List_Noun = list ()
List = ['Hi', 'Ok', 'ok', 'day', 'hahaha', 'haha', 'yeah', 'day', 'Day', 'hehe', 'lol','gf','ugh','aww','bye','yeap','lot','yea','none','bc','u','yeahhhh',':D','yup','st.','hahahahaha','aw','work.lynnsf8']
for i in range (len (root[0][0])):
    for j in range (len (root[0][0][i][0])):
        if (root[0][0][i][0][j][0].text in List):
            break
        elif root[0][0][i][0][j][4].text == 'NN' and root[0][0][i][0][0][0].text != root[0][0][i][0][j][0].text and \
                        root[0][0][i][0][j][0].text != ':-RRB-' and root[0][0][i][0][j][0].text != 'PM':
            #print (p + 1, root[0][0][i][0][0][0].text, root[0][0][i][0][j][0].text)
            List_Noun.append (root[0][0][i][0][j][0].text)
            List_Name.append(root[0][0][i][0][0][0].text)
            p = p + 1

            # elif root[0][0][i][0][j][4].text =='PRP$':
            #      print(root[0][0][i][0][0][0].text , root[0][0][i][0][j][0].text)

print (List_Noun)

multi_noun=[item for item, count in collections.Counter(List_Noun).items() if count > 1]
print (multi_noun)
print(len(multi_noun), len(List_Noun))
List_Name_in=list() #all speakers who introduce the topic list
List_Noun_multi=list()
# this is to count or get all participant who introduce the topic
for i in range (len (multi_noun)):
    print(multi_noun[i])
    for j in range (len (List_Noun)):
        if(multi_noun[i]== List_Noun[j]):
            print( j,List_Name[j],List_Noun[j])
            List_Name_in.append (List_Name[j])
            List_Noun_multi.append(List_Noun[j])








print (List_Noun_multi)
#print(len(List_Name_in),len(List_Noun_multi))
freq_noun=nltk.FreqDist(List_Noun_multi)
freq= nltk.FreqDist(List_Name_in)
print ([freq])   # counts the topic introduction and topic Allotopicality
print ([freq_noun]) # helps to counts the topic chain index


print (len(root[0][0]))


print (len (root[0][0][0][0]))  # get the number of words in the senetence
print (root[0][0][3][0][7][4])  # pos
print (root[0][0][4][0][6][0].text)  # word
print (root[0][0][0][0][0])  # token
print (root[0][0][4])  # sentence
print (root[0][0])  # sentences
print (range (len (root[0][0])))  # range















'''
print(root.tag,root.attrib)
for child in root:
    print(child.tag,child.attrib)

print(root[0][0][1].text)

for superChild in root[0][0]:
    print(superChild.tag,superChild.attrib)
    
    
    
for superChild in root[0][0][0]:
    print(superChild.tag,superChild.attrib)

print(root[0][0][0][1].tag,root[0][0].text,root[0][0][2][0][0].attrib)
    
    
    

print(root[0][0].tag,root[0][0].text)

print(root.text)
Count = 0
for POS in root[0][0][2].iter('POS'):
        #print(POS.text)
        if POS.text == 'PRP':
            Count = Count + 1
        elif POS.text == 'PRP$':
            Count = Count + 1

print(Count)

id=root[0][0][2][0][0].get('id')
mod=root[0][0][2][0][0][0].text
print(id,mod)

'''
