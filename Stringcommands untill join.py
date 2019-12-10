word = 'ZaraKirakosyan'
#Type the first letter of the string  capital
print(str.capitalize(word))
#Print the length of the string
print(len(word))
#Make the string appear towards the center based on the number provided and with visual element "*"
print(word.center(150, "*"))
#Return how many times the subtring appears within the given start/end
str="This is the first steps I take to learn python"
sub="i"
print(str.count(sub, 3, 33))
#decode/encode bac em toghel
#Return tru/false if  the string ends with specified suffix
str="Hrashq Vardanyan"
suffix="yan"
print(str.endswith(suffix, 10,20))
print(str.endswith(suffix,0,5))
#Expand the tabs given in the sentence. avelacnelov/t nax@ntrac baric araj inqn arandnacnum e. Default@ 8 a.
str="inch vor\tgciknerov\tnakhadasutyun "
print(str.expandtabs())
print(str.expandtabs(33))
#Define whether string 2 occurs in string 1>
str="Hayastani Hanrapetutyun"
print(str.find("rap",0,18))
#index: didn't get why it returned 14
str="Vardanush, hrushakeghen, Lincoln"
print(str.index("sha"))
#check whether all chars are alphanumeric(constits of letters and numbers)
str1="hangstyan goti"
print(str1.isalnum())
str2="anerevakayeli"
print(str2.isalnum())
#check whethers chars are alphabetic
str1="herakhosahamar"
str2="herakhosihamarne33333333"
print(str1.isalpha())
print(str2.isalpha())
#Return whether all are digits
str1="123321"
str2="123r664"
print(str1.isdigit())
print(str2.isdigit())
#return true if all in char are lowercase, uppercase, false if not
str3="AshsjsjkPP"
str4="sghjdbstrsbdbabdhb"
str5="RRRRR"
print(str3.islower())
print(str3.isupper())
print(str4.islower())
print(str5.isupper())
#print every single new word first letter uppercase
str="Nayir nran ereq guynov"
print(str.stitle())









