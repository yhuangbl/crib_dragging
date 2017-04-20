import re

# turn ASCII to int
def s_to_int(s):
    int_list = []
    for c in s:
        # ord(c) turn ASCII to int
        int_list.append(ord(c))
    return int_list


# turn int to ASCII
def int_to_s(int_l):
    char_list = []
    for i in int_l:
        # str(unichr(i)) turn int to ASCII
        char_list.append(str(unichr(i)))
    return ''.join(char_list)


# read file and return an int array represting the string
def read_file(file_name):
    target = open(file_name, 'r')
    content = target.read()
    target.close()
    return s_to_int(content)

# XOR function; reference from professor's code
def xor_two_lists(a, b):
    if len(a) > len(b):
        temp = a
        a = b
        b = temp
    s = []
    for i in range(0, len(a)):
        s.append(a[i] ^ b[i])
    for i in range(len(a), len(b)):
        s.append(b[i])
    return s

# crib drag solver
class cribDrag(object):
    def __init__(self):
        # c0 and c1 are ciphertexts
        self.c0 = read_file("ctext0")
        self.c1 = read_file("ctext1")
        self.c0_xor_c1 = xor_two_lists(self.c0, self.c1)

    # crib
    def guess_word(self, word):
        word_length = len(word)
        word_int = s_to_int(word)
        # for parsing
        charset = '^['+'a-zA-Z0-9.,?! :;\'"'+']+$'
        # put the intermediate results in log.txt file
        with open("log.txt", "a") as myfile:
            myfile.write("guess word: \""+word+"\"")
            for i in range(len(self.c0_xor_c1)-word_length+1):
                z = self.c0_xor_c1[i:i+word_length]
                crib = xor_two_lists(z, word_int)
                test_string = int_to_s(crib)
                if (re.search(charset, test_string)):
                    myfile.write("\n[%d]" % i)
                    myfile.write(test_string)
        myfile.close()


# main function
finish = False
c = cribDrag()

while not finish:
    word = raw_input("Guess a word: ")
    c.guess_word(word)
    check = raw_input("finish?(y/n): ")
    if check == "y":
        finish = True
        break
