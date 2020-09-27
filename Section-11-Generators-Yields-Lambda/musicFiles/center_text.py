def centre_text(*args, margin=80):
    text = ''
    for arg in args:
        text += str(arg) + " "
    left_margin = (margin - len(text)) // 2
    print(" " * left_margin, text)


def centre_text_comp(*args, margin=80):
    text = "-".join([str(arg) for arg in args])
    left_margin = (margin - len(text)) // 2
    print(" " * left_margin, text)


centre_text_comp("spam and eggs", margin=120)
