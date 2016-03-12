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

#will split if two letter are twogether that are within the range
print (re.split(r'[a-f][a-f]', 'slkdjvDoijewlkbjlBknklsdfnaPyhoghsf'), re.I|re.M)

# other way to find digits [0-9]
# \D is to find everything but digits]
# \S is non-space
print (re.findall(r'\d{1,5}\s\w+\s\w+\.', 'slkjdoibjkl324 main st.sldkjflkbjlskdjflskj'))

# ###########Quantities
# * = 0 or more
# + = 1 or more
# ? = 0 or 1 of
# {5} = exact number of
# {1,60} = range on number of

# \w = alphanumeric
# \s = space
# \. = regular period (.)
# . = any character but newline (\n)





