#ref - https://stackoverflow.com/questions/8982163/how-do-i-tell-python-to-convert-integers-into-words

def numToWords(num, join=True):
    units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', \
             'seventeen', 'eighteen', 'nineteen']
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', \
            'eighty', 'ninety']
    thousands = ['', 'thousand']
    words = []
    numStr = '%d' % num
    numStrLen = len(numStr)
    groups = (numStrLen + 2) / 3
    numStr = numStr.zfill(groups * 3)
    for i in range(0, groups * 3, 3):
        h, t, u = int(numStr[i]), int(numStr[i + 1]), int(numStr[i + 2])
        g = groups - (i / 3 + 1)
        if h >= 1:
            words.append(units[h])
            words.append('hundred and')
        if t > 1:
            words.append(tens[t])
            if u >= 1:
                words.append(units[u])
        elif t == 1:
            if u >= 1:
                words.append(teens[u])
            else:
                words.append(tens[t])
        else:
            if u >= 1:
                words.append(units[u])
        if (g >= 1) and ((h + t + u) > 0):
            words.append(thousands[g] + ',')
    if join:
        return ' '.join(words)
    return words


results = ""
for i in range(1, 1001):
    results += numToWords(i)

results = results.replace(" ", "")
results = results.replace(",", "")
print(results)
print(len(results) - 27) #hardcoded for removing 'and' :D
