def znajdz_samogloski(s):
    vowels = []
    for c in s:
        if c.lower() in "aeiou":
            vowels.append(c)
    return vowels