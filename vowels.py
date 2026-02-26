def vowels_count(text):
    if text == "":
        return 0
    return (text[0].lower() in "aeiou") + vowels_count(text[1:])

print(vowels_count(input("Enter the text : ")))