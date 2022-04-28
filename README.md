# HANGMAN![image](https://user-images.githubusercontent.com/102962523/164088068-c255d789-a69f-47da-bcde-dc94eebbe303.png)

If you want to see the code, open the .py files 
<br>The project containts a pair of client – server applications (made with Python sockets) that implements the game „Hangman”. The rules are simple: 	
	 -  the client, the moment he/she wants to start the game, sends the start command to the server;
	 - the server chooses a random word from the 'hangwords.txt’ file. It sends a version of this word to the client. This version retains only the letters that appear at the beginning and at its end, the rest of the letters being replaced by underlines. Along with this, the server also sends a list of letters from the word HANGMAN which shows how many times the client has made a mistake and how many guesses it still has; at first there is no letter from HANGMAN because there’s no mistake . . . yet   .
	 - after the client receives the sketch of the word he/she has to guess, he/she will send letters to the server till the game finishes.  If the letter received from the client exists in the word that needs to be guessed, then the underline from the position of that letter in the word is replaced by that letter changing the version of the word that is sent to the client. Otherwise, a letter from the word 'HANGMAN' is added to the list. The current version of the word to be guessed along with the letters from HANGMAN are added to the message sent to the client to show him/her the progress. 

	<br>Too complicated?
	Let's check the code and see how it works. 
	Maybe things are getting better . . .
	<br>Let's start with the client, more precisely, with the beginning of the Client program:<br>
 ![image](https://user-images.githubusercontent.com/102962523/164088217-f7e55964-0407-4394-9782-e47113713c1c.png)
  	<br>At the beginning of the program, the ’socket’ library is imported so that we can use the sockets, although this is completely obvious  . 
	Then we choose the ID address and port number of the server to be able to connect the applications. The address 127.0.0.1 was chosen because both applications were created on the same device. The port 6200 was randomly chosen for the sake of the project.
	'client_socket' is an object that inherits the attributes of the 'socket' class by calling the class constructor. It helps us send the messages to the server.
	 <br>After that we declare 3 variables. Their role is explained in the comments from the code:<br>
  ![image](https://user-images.githubusercontent.com/102962523/164088293-75546284-2a0b-4e08-bc56-3eee4f20bb81.png)
 	<br>Now we are geting to the most importatnt part from the Client application: we’ll see how to send messages to the server and how to get the word we need to guess from the server. The message exchange takes place in a while structure. The instructions in the structure repeat as long as the boolean variable 'finished' (which checks if the game is over) is False.<br>
  ![image](https://user-images.githubusercontent.com/102962523/164088365-8e863a77-8e44-466b-92b0-21bb34acc2d8.png)
 	<br>First we check if the start command has been sent (it must be sent so the game begins). The boolean variable 'st' checks this. 'st' is currently False.
	We have to write the "START" command. The size of the characters is ignored because it is automatically converted to uppercase and then compared to "START".<br>
  ![image](https://user-images.githubusercontent.com/102962523/164088411-e57fc279-b5ef-4802-9df0-0fe0e5fcd15b.png)
 	<br>As long as the right command is not entered, the input will continue to be requested so that the application can move on.<br>
  ![image](https://user-images.githubusercontent.com/102962523/164088580-2ea27e18-d74b-492e-9d9d-4cb3bea53aa0.png)
	<br>After writing "START" and send it to the server, the client receives the structure of the word that needs to be guessed, and 'st' becomes True (the command has been sent).<br>
  ![image](https://user-images.githubusercontent.com/102962523/164088626-89116b77-c83a-460c-adeb-b6a91cd6cbab.png)
  ![image](https://user-images.githubusercontent.com/102962523/164088636-7e231a0a-7e53-426f-8f37-221220a633c0.png)
 	<br>Let’s get back to this line: ![image](https://user-images.githubusercontent.com/102962523/164088668-290aa54b-56c0-4b10-9b02-b37f21d7e437.png)
 	<br>Using the client_socket object, we send the encoded message to the server that has the address and the port from the tuple.
	Now let’s go to the server and see what happens when the message is received.
 	But before that, we should take a look at the beginning of the 'Server' program:<br>
  ![image](https://user-images.githubusercontent.com/102962523/164088794-fdfd6619-cd2d-43eb-a836-3801192c6bcd.png)
 	We give the port its value (6200 is the same value that the port in the Client has).
	Then 'server_socket' inherits the attributes of the 'socket' class by calling the class constructor. On the next line, the server binds with the client that uses the port 6200. 
	We then print a message to show that the server is ready to do its job.
	'hangman' is a list that contains the letters of the word ”HANGMAN”. The letters from this list will be added to the message that will be sent to the client each time the client make a wrong guess.
 	<br>The exchange of messages and the verification of the letters take place in a 'while' structure, but this time there is no condition for this 'while' to end, because the server must always be ready in order to be accessed by a new Client.
 	In the first instruction inside of 'while' a message and the Client’s adress are received from the Client. The message is verified. The first time it is checked if it is "START" and indeed, in the Client we sent the command "START" to the Server.<br>
  ![image](https://user-images.githubusercontent.com/102962523/164089161-2af50970-0a82-4845-abfd-f0d3f77fefe0.png)
  <br>After receiving the start command, the server opens the 'hangwords.txt' file and reads the words in it (each word is on a different line), and then chooses a random number, less than the number of lines in the text file , and the word at that position becomes the word that needs to be guessed by the Client.<br>
  ![image](https://user-images.githubusercontent.com/102962523/164089306-f8e49778-67b7-4571-ba46-923619182d8b.png)
 	<br>Then two lists are declared (the first one - 'guessWord', contains the letters from the word thet needs to be guessed, and the second one - 'H', contains letters from the hangman, letters that are added to the list at each mistake of the Client) and a string - 'msg', whose content will consist of the two lists combined. The two lists are currently empty, they only have square brackets because between them will be included the word to be guessed and hangman.<br>
  ![image](https://user-images.githubusercontent.com/102962523/164089386-1785293b-c0d6-475b-a947-16f1545bd250.png)
 	<br>The version of the word to be guessed is formed (the letters that are equal to the first and last letter of the word are added in 'guessWord', and the others are first replaced with underline, and then added in 'guessWord').<br>
  ![image](https://user-images.githubusercontent.com/102962523/164089422-277609c9-deda-4600-b33f-89c562bb49e8.png)
 	<br>'msg' is created by concatenating 'guessWord' and 'H' and is sent to the server:<br>
  ![image](https://user-images.githubusercontent.com/102962523/164089459-e927160b-1550-45a2-90d1-310c24c43ec3.png)
 	<br>'j' is a counter that adds letters from 'H' to the message sent to the client. It becomes 0 after each START command because each client starts the game with 0 mistakes.
  	<br>The message is sent to the Client so let’s get back to the 'Client' program.<br>
  ![image](https://user-images.githubusercontent.com/102962523/164089643-0e84a1f1-ed29-4b91-a8b9-d86715dfcbcf.png)
 	<br>The message is received and displayed and 'st' becames True.<br>
  ![image](https://user-images.githubusercontent.com/102962523/164089700-8497bd58-492e-453b-8fcb-3300c74d38e5.png)
 	This is the message sent by the Server in this example. The second list is empty because there is no mistake made, so there is no letter from the list 'H'.
 	<br>The 'while' structure is repeated again, only this time "START" has been sent, so we jump to the "else" statement:<br>
  ![image](https://user-images.githubusercontent.com/102962523/164089760-05190eef-175c-4db2-8a3c-0697df609fcb.png)
 	<br>Inside 'else' a letter is first required to be inserted. The letter is then sent to the Server, and then a reply is received which is displayed.<br>
  ![image](https://user-images.githubusercontent.com/102962523/164089817-b1cb480d-4e86-45e7-a5db-b3380fae359c.png)
 	<br>The program checks if there are underlines in the reply, or if the word "HANGMAN" appears in the reply. If one of the two conditions is True, the game ends; otherwise, 'while' is repeated until one of the two conditions becomes True.<br>
  ![image](https://user-images.githubusercontent.com/102962523/164089858-b284b2c7-1a91-410e-b48a-cd041def2a0f.png)
 	<br>At the end of the program, after the game is over, the connection to the Server closes.<br>
  ![image](https://user-images.githubusercontent.com/102962523/164089889-de0b4a48-c0b8-41ac-ac1c-dbb6b712cf73.png)


 	Let's get back to this line: 
  ![image](https://user-images.githubusercontent.com/102962523/164089918-609fb75b-d639-4e5d-b3da-5f83526c33f4.png)
 	<br>Here a letter is sent to the Server. Let’s see what does the Server do with the letter:
	The 'while' structure is repeated again, only this time the message is no longer "START", so the program jumps to the 'else' statement.
  ![image](https://user-images.githubusercontent.com/102962523/164089995-4938894e-dc3f-42c3-b0ab-f69a778fdfa3.png)

  Inside 'else', 'msg' becomes empty because it will be formed this time from a new 'guessWord' or a new 'H', depending on how the Client guesses the letter.
  ![image](https://user-images.githubusercontent.com/102962523/164090039-19268b0a-eb86-4da9-9727-0c757b78aa47.png)
 <br>The program checks if the letter appears in the word. If id does, the underline of the letter position (s) in the word is replaced by the letter; if not, a character from 'hangman' is added to 'H', and 'j' increases, moving to the next character in 'hangman'.<br>
  ![image](https://user-images.githubusercontent.com/102962523/164090252-dd1537b7-99a0-430f-ab2f-c8100ac86059.png)
  <br>After that, 'guessWord' and 'H' are added to 'msg', and then the message
 is sent to the Client.<br>
  ![image](https://user-images.githubusercontent.com/102962523/164090291-76617275-f620-4779-b3ce-76a15e10288e.png)

   
  # This is how a complete message exchange looks like:
  ![image](https://user-images.githubusercontent.com/102962523/164090390-2b63e07b-a875-431d-b674-5439f33e474c.png)
  ![image](https://user-images.githubusercontent.com/102962523/164090405-557278e0-59da-42ea-aa2f-f5b1cab8c96e.png)
  <br>The server is always ready and receives messages from multiple clients, generating new words after each START command.<br>
  ![image](https://user-images.githubusercontent.com/102962523/164090441-d79ac069-572a-47d8-938a-510b7fa9d3a7.png)
