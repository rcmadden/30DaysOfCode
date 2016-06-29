tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# must use print function to envoke format variables, returning variable returns string literals
back_slash = '''escaping \t \nto see what happens'''
back_slash
print(back_slash)

ascii_bell = '\a'
print(ascii_bell)
print("wtf" + ascii_bell + "i don't see no bell")
print("wtf does this \b BS do? ")
print("wtf does this \f FF do? ")
# works
print("already know what this \n LF does? ")
print("\n")
print("but why does this \r CR blend with the LF above? ")
print("already know whast this \t TAB thing \t\t does? ")
print("this \u1234 16-bit hex prints hex characters? ")
print("wtf does this \v TAB thing \v\v do I only see these little boxes? ")
print("already know whast this \t TAB thing \t\t does? ")
print("wtf is this octal value thing \ooo all about?")
print("wtf is this hex value thing \8hh all about?")

#syntax error
#print("character \N{name} of Unicode character named name")
#print("wtf does this \U12345678 16-bit hex do? ")