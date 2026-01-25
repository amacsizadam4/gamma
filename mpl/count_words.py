def count_words(txt_file):
    with open(txt_file) as file:
        content = file.read()

        words = content.split()

        return len(words)
    


#-----------------------------------------

def find_and_replace(txt_file, target_word, replacement_word):
    with open(txt_file, 'r') as file:
        content = file.read()

    modified_content = content.replace(target_word, replacement_word)

    with open(txt_file, 'w') as file:
        file.write(modified_content)
    return f"Replaced {content.count(target_word)} occurrences of '{target_word}' with '{replacement_word}'."

#-----------------------------------------
print(count_words("abd.txt"))

print(find_and_replace("abd.txt", "Warsaw", "Cracow"))

content = "ala ma kota ala ma kota"
print(content.count("ala"))