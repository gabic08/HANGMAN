import socket
from random import randint

port = 6200


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', port))

print("The server is ready!")

hangman = ['H', 'A', 'N', 'G', 'M', 'A', 'N']

while True:

    # The message is received from the client
    message, clientAdress = server_socket.recvfrom(100)

    # Checking if the received message is the "START" command
    if message.decode() == "START":

        f = open('hangwords.txt')
        words = f.readlines()
        w = len(words)
        k = randint(0, w - 1)

        ln = len(words[k])
        word = words[k]

        guessWord = ['[', ']']   #The list of letters of the word to be guessed.
        H = ['[', ']']   #The list in which letters from the word HANGMAN are added after every mistake
        msg = ''  #The message that will be sent to the client; it is composed of guessWord and H

        for i in range(1, ln):
            if word[i - 1] == word[0]:
                guessWord.insert(i, word[0])
            elif word[i - 1] == word[ln - 2]:
                guessWord.insert(i, word[ln - 2])
            else:
                guessWord.insert(i, '_')


        #Creating the message that will be sent to the client
        for i in range(len(guessWord)):
            msg = msg + guessWord[i]

        for i in range(len(H)):
            msg = msg + H[i]


        print('The word is:', word)
        server_socket.sendto(msg.encode(), clientAdress)  #The message is sent to the client

        j = 0 #The counter that shows which letter in HANGMAN has been reached


    #If the received message is not the start command it means that the game has started and the message received is a letter.
    else:
        msg = ''    # The old message is deleted so that a new one can be created


        #The letter is received and it is checked if it appears in the word
        letter = message.decode()
        if letter.upper() in words[k]:
            for i in range(len(word)):
                if letter.upper() == word[i]:
                    guessWord[i+1] = word[i]
        
        else:
            H.insert(j+1, hangman[j])
            j = j + 1


        #guessWord and H join in 'msg' and are send to the client
        for i in range(len(guessWord)):
            msg = msg + guessWord[i]

        for i in range(len(H)):
            msg = msg + H[i]

        server_socket.sendto(msg.encode(), clientAdress)
