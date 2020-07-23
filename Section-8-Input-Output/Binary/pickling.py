import pickle

# imelda = (
#     "More Mayhem",
#     "Imelda May",
#     "2011",
#     (
#         (1, "Pulling the Rug"),
#         (2, "Psycho"),
#         (3, "Mayhem"),
#         (4, "Kentih Town Hall")
#     )
# )
#
# with open("imelda.pickle", "wb") as pickle_file:
#     pickle.dump(imelda, pickle_file)

# with open("imelda.pickle", "rb") as pickled_file:
#     imelda2 = pickle.load(pickled_file)
#
#
# print(imelda2)
# album, artist, year, tracks = imelda2
# print(album)
# print(artist)
# print(year)
#
# for (track_no, track_title) in tracks:
#     print(track_no, track_title)

# imelda = (
#     "More Mayhem",
#     "Imelda May",
#     "2011",
#     (
#         (1, "Pulling the Rug"),
#         (2, "Psycho"),
#         (3, "Mayhem"),
#         (4, "Kentih Town Hall")
#     )
# )
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
#
# with open("imelda.pickle", "wb") as pickle_file:
#     pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
#     pickle.dump(even, pickle_file, protocol=0)
#     pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
#     pickle.dump(2998302, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
#
# with open("imelda.pickle", "rb") as pickled_file:
#     imelda2 = pickle.load(pickled_file)
#     even_list = pickle.load(pickled_file)
#     odd_list = pickle.load(pickled_file)
#     value = pickle.load(pickled_file)
#
# print(imelda2)
# album, artist, year, tracks = imelda2
# print(album)
# print(artist)
# print(year)
#
# for (track_no, track_title) in tracks:
#     print(track_no, track_title)
#
# print("-" * 40)
#
# for i in even_list:
#     print(i)
#
# print("-" * 40)
#
# for i in odd_list:
#     print(i)
#
# print("-" * 40)
#
# print(value)

print("-" * 40)

pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")
