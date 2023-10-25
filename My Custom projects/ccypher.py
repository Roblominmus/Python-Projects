import sys

mode = str(sys.argv[3])
step = int(sys.argv[2])
msg = str(sys.argv[1]).upper()
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cypher(msg, step, mode):
    response = ''
    for i in msg:
        if i in letters:
            temp = letters.find(i)
            if mode == "-e":
                temp += step
                temp = letters[(temp % len(letters))]
                response += temp
            elif mode == "-d":
                temp -= step
                temp = letters[(temp % len(letters))]
                response += temp
            else:
                print("Incorrect Syntax: ccypher test-message 3 -e")
        else:
            response += i
    return response

print(f"Input: {msg}")
print(f"Output: {cypher(msg, step, mode)}")