import re

#print spliting on the 's'
print (re.split(r'(s*)', 'here are some words'))


#print spliting on letters that are a - f, only lowercase
#[] <-- looks for character in this range
print (re.split(r'[a-f]', 'slkdjvoijewlkbjlknklsdfnayhoghsf'))

#add flags for upper and lower case
# re.I --> ignore all case flucation
# re.M --> if the input is multi-line, it would evaluate it contiously
print (re.split(r'[a-fA-F]', 'slkdjvDoijewlkbjlBknklsdfnaPyhoghsf'), re.I|re.M)


print (re.split(r'[a-f][a-f]', 'slkdjvDoijewlkbjlBknklsdfnaPyhoghsf'), re.I|re.M)

