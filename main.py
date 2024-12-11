#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Names/invited_names.txt') as file:
    clear_names = []
    names = file.readlines()

    for name in names:
        new_name = name.strip()
        clear_names.append(new_name)




for name in clear_names:
    letter = open('./Input/Letters/starting_letter.txt')

    changed_letter = letter.readlines()

    with open(f'./Output/ReadyToSend/{name}_invitation.txt',mode='w') as letter:
        for change in changed_letter:
            new_letter = change.replace('[name]',name)
            letter.write(new_letter)



    # new_letter = open(f'./Output/ReadyToSend/{name}_invitation.txt',mode='w')



