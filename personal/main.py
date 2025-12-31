import sys

if len(sys.argv) == 2:
    bookPath = sys.argv[1]
    try:
        with open(bookPath, "r") as bookfile:
            booktext = bookfile.read()
    except FileNotFoundError:
        print("Error: File not found. Please make sure the book is at the specified path.")
        sys.exit(1)
    except PermissionError:
        print("You dont't have permission to access this file.")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookPath}...")
    print("------------ Word Count ------------")

    words = booktext.split()
    wordCount = len(words)

    print(f"Found {wordCount} total words")

    # initalize empty set to track characters
    characters = set()

    # loop through all of the letters in each word and add them to the set
    for word in words:
        for char in word:
            # check is the character is a letter before adding it
            if char.isalpha():
                characters.add(char)

    # convert the characters to a list and sort it
    characters = list(characters)
    characters = sorted(characters)

    # initialize an empty dictionary and then create pairs for each of the unique characters
    characters_Dictionary = {}
    for char in characters:
        characters_Dictionary[char] = 0

    for word in words:
        for char in word:
            # make sure the char is a letter. this avoids a key error from passing is a char that was filtered out when making the set of characters
            if char.isalpha():
                characters_Dictionary[char] += 1

    print(f"------------ Character Count ------------")
    for char in characters_Dictionary:
        print(f"{char} : {characters_Dictionary[char]}")

else:
    print("Please supply a path to a book to analyze.")
