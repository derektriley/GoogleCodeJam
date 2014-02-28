import re
def is_valid_string(string, word):
    for i in range(0, len(string)):
        if not is_valid_char(string[i], word[i]):
            return False;
    return True;
def is_valid_char(char, test):
    if char[0] == '(':
        for i in range(1, len(char)-1):
            if char[i] == test:
                return True;
        return False;
    else:
        if char[0] == test:
            return True;
        else:
            return False;
content = open('small.in', 'r').readlines()
for i in range(0, len(content)):
        content[i] = content[i].rstrip('\n')
content[0] = content[0].split()
tokens = content[0][0]
testcases = content[0][1]
words = content[0][2]
content.pop(0)
wordlist = []
for i in range(0, int(testcases)):
    wordlist.append(content[0])
    content.pop(0)
content = ''.join(content)
content = re.findall('\([a-z]*\)|[a-z]', content)
content = list(filter(None, content))
newcontent = []
for i in range(0, int(words)):
    combined = []
    for j in range(0, int(tokens)):
        item = content.pop(0)
        combined.append(item)
    newcontent.append(combined)
for i in range(0, int(words)):
    counter = 0
    for j in range(0, int(testcases)):
        if is_valid_string(newcontent[i], wordlist[j]):
            counter += 1
    print ('Case #' + str(i+1) + ': ' + str(counter))
