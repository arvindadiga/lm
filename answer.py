"""
We need a way of finding all the occurrences of a particular
set of characters in a string. It should:

- Accept two strings as input.
  One called 'textToSearch' and one called 'subtext'

- The solution should match the subtext against
  the textToSearch, outputting the positions of the
  beginning of each match for the subtext within the textToSearch.

- Multiple matches are possible

- Matching is case insensitive

- If no matches have been found, no output is generated
"""


def text_search(text_to_search, subtext):
    matches = []

    i = 0
    j = 0
    word_beginning = 1
    while i < len(text_to_search):
        lhs = text_to_search[i].lower()
        rhs = subtext[j].lower()
        i = i + 1

        # no match
        if lhs == ' ':
            j = 0
            word_beginning = i + 1
            continue

        if lhs == rhs:
            j = j + 1

            # found a match
            if j >= len(subtext):
                matches.append(word_beginning)
                j = 0
                continue
        else:
            j = 0  # no match

    return matches
