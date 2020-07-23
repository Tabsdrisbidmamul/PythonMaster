# splitString = "This string has been\nsplit ovber\nseveral\nlines"
# print(splitString)
#
# print("""The pet shop owner said "No, no, \
#  'e's uh,...he's resting".""")
# anotherSplitString = """This string has been \
# split over \
# several \
# lines"""
# print(anotherSplitString)
#
#
# # print("C:\Users\timbuchalka\notes.txt")
#
# print("C:\\Users\\timbuchalka\\notes.txt")
# print(r"C:\Users\timbuchalka\notes.txt")
#
# age = 24
# print(type(age))
# print(type(splitString))

gen_list = ['9', '223', '372', '036', '854', '775', '807']
gen_list = [int(num) for num in gen_list]
print(gen_list)

albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the Lightning", "Metallica", 1984),
]

for (name, artist, year) in albums:
    print("Album: {}, Artist: {}, Year: {}".
          format(name, artist, year))
