import socket

host = '127.0.0.1'
port = 6200

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


finished = False  #'finished' checks if the game is over, if the word was found or if the word HANGMAN was completed.
st = False   #'st' is a variable that checks if the start command has been sent to the server
start = ''   #'start' is a string that gets the start message input


while finished == False:

    # It is checked if the "START" message has been sent
    if st == False:

        while start.upper() != "START":
            start = input("Input the start command(START): ")

        # The message "START" is sent to the server, then the word to be guessed is received and displayed.
        start = start.upper()
        client_socket.sendto(start.encode(), (host, port))
        message, serverAdress = client_socket.recvfrom(100)
        print(message.decode())
        st = True


    #If the START command has been sent, the client must enter letters that the application sends to the server, and then the response is displayed.
    else:
        letter = input("Type a letter: ")

        client_socket.sendto(letter.encode(), (host, port))

        message, serverAdress = client_socket.recvfrom(100)
        print(message.decode())

        
        #If there are no more underlines in the word to be guessed, or if the word HANGMAN is complete, then the game finishes       
        if not ('_' in message.decode()):
            print("\nCongrats! You've guessed the word! You win!\n")
            finished = True

        elif "[HANGMAN]" in message.decode():
            print("\nSorry, but you ran out of guesses!  Maybe next time...\n")
            finished = True


client_socket.close()
