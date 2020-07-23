# cities = [
#     "Adelaide",
#     "Alice Springs",
#     "Darwin",
#     "Melbourne",
#     "Sydney",
# ]

# with open("cities.txt", "w") as city_file:
#     for city in cities:
#         print(city, file=city_file)

import re

# cities = []
# # with open("cities.txt", "r") as file:
# #     line = file.readline()
# #     while line:
# #         line = re.sub("$\n", "", line)
# #         cities.append(line)
# #         line = file.readline()
# #
# # print(cities)

# imelda = "More Mayhem", "Imelda May", "2011", (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
# )
#
# with open("imelda.txt", "w") as file:
#     print(imelda, file=file)

with open("imelda.txt", "r") as file:
    contents = file.readline()
    imelda = eval(contents)
    print(imelda)
    title, artist, year, tracks = imelda
    print(title)
    print(artist)
    print(year)
    print(tracks)