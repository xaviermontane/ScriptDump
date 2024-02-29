with open('sample.txt', 'r') as f:
    textContent = f.read()
    whitespaceIndex = 0

    for x in range(len(textContent)):
        if textContent[x].isspace():
            print(textContent[whitespaceIndex:x].upper())
            whitespaceIndex = x + 1
            
    # Print the remaining text after the last whitespace (if any)
    if whitespaceIndex < len(textContent):
        print(textContent[whitespaceIndex:].upper())