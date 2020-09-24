import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open("recipes", writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["soup"] = soup
    # recipes["pasta"] = pasta

    # temp_list = recipes.get("blt")
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes.get("pasta")
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

    # recipes["soup"].append("croutons")

    # recipes["soup"] = soup
    # soup.append("cream")
    # recipes.sync()

    for snack in recipes:
        print(snack, recipes[snack])
