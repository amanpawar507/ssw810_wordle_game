import HW03_Aman_Pawar_dictionary
import HW03_Aman_Pawar_ui

#Defining color functions
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

def main():
    print("\n**************WORDLE GAME*******************\n")
    print('Each guess must be a valid 5 letter word.\nYou have 6 attempts.\nHit the enter button to submit.')

    #Initializing variables
    words = [None] * 6
    copy_words =[None] * 6
    myWord = HW03_Aman_Pawar_dictionary.random_word().upper()
    print(myWord)
    #Loop for 6 times for 6 attempts
    for x in range(6):
        #variables for storing abbreviations
        final_list = [None] * 5
        final_string = ""

        #Creating copy of input words 
        copy_words = words.copy()
        
        #Taking input
        print("\nGuess the word")
        words[x] = HW03_Aman_Pawar_ui.get_input(words, copy_words, x)
        copy_myWord = myWord
        #Check if the word was correct
        if (words[x].upper()==myWord):
            prGreen("Correct guess, You win!")
            quit()
        else:
            print(words[x].upper())
            #Looping to check each letter
            for y in range(5):
                #Check which letter is in correct position and is a correct word
                if words[x][y].upper() == copy_myWord[y]:
                    i = y
                    copy_myWord =  copy_myWord[:i] +" "+ copy_myWord[i+1:]
                    final_list[y] = " "
                    
            for y in range(5):   
                if(final_list[y] != None):
                    continue
                else:
                    #Check which letter is correct but in wrong position
                    if words[x][y].upper() in copy_myWord:
                        my_letter = words[x][y].upper()
                        i= int(copy_myWord.find(my_letter))
                        copy_myWord =  copy_myWord[:i] +" "+ copy_myWord[i+1:]
                        final_list[y] = "`"
                    
                    #Check if the letter is incorrect  
                    else: 
                        final_list[y] = '"'
                        continue
            
            for i in final_list:
                final_string += str(i) + ""
            print(final_string)

            #Exit when all attempts are exhausted
            if x==5: prRed("You lose!")
            continue

if __name__== "__main__":
    main()