def count_words(text: str):
  return len(text.split())

def count_char_occurence(text: str, sort: bool = False):
  text = text.lower()
  occurences = dict()
  for char in text:
    if char.isalnum():
      if not char in occurences.keys():
        occurences[char] = 1
      else:
        occurences[char] += 1
  
  if not sort:
    return occurences
  
  return { k: v for k, v in sorted(occurences.items(), key=lambda item: item[1], reverse=True)}


with open("books/frankenstein.txt", "r") as f:
  print("--- Begin report of books/frankenstein.txt ---")

  text = f.read()
  print(f"{count_words(text)} words found in the document")
  print()
  occurences = count_char_occurence(text, True)
  for k, v in occurences.items():
    print(f"The '{k}' character was found {v} times")