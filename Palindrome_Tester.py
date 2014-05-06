#This python script finds the longest palindrome contained in a string


import string

text = '''afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood'''

text2 = "feklsjfelfkjslfkejslkefkeekfeklsjekflsjkflefjslkef"

print text[len(text)-1]

#This function takes a string and returns the longest palindrome contained in said string

def palindrome_long(text):
    pal_str = []
    for length_counter in range(3,len(text)-5):
        for i in range(len(text)-1-length_counter):
            if palindrome_short(text[i:i+length_counter], length_counter) == True:
                pal_str.append(text[i:i+length_counter])
    print pal_str
    return pal_str[-1]

#This function returns 'True' if the input string is a palindrome.
#Args:
#text - a string
#length - the length of said string

def palindrome_short(text, length):
    if text[0::] == text[::-1]:
        return True
print palindrome_short("banab", 5)
print palindrome_long(text)
print palindrome_long(text2)
