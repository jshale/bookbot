def get_num_words(bookContent):
    num_words = len(bookContent.split())
    return num_words


def count_characters(bookContent):

    character_dictionary = {}

    for char in bookContent:
        loweredChar = char.lower()
        if loweredChar in character_dictionary:
            character_dictionary[loweredChar] += 1
        else:
            character_dictionary[loweredChar] = 1

    return character_dictionary


def sort_characters(character_dictionay):
    dict_list = []
    key_list = character_dictionay.keys()

    for key in key_list:
        if key.isalpha():
            tmp_dict = {"letter": key, "count": character_dictionay[key]}
            dict_list.append(tmp_dict)

    def sort_on(items):
        return items["count"]

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list
