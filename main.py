
def compressor(decomp: str) -> str:
    # check is decomp only has letters
    if decomp.isalpha() == False:
        print("Only alphabetic characters are allowed when compressing a source string.")
        return ""
    comp = "" # create a string comp we will add to
    n = decomp[0] # set n as the first letter of decomp
    count = 1 # count represents number of each letter
    for i in range(1, len(decomp)):
        if n == decomp[i]:
            count += 1 # if the letter is equal to the letter after it, increase count by 1
        else:
            comp = comp + str(count) + n # else add to string comp with the number of each letter
            count = 1 # reset count to 1 for new letter
            n = decomp[i] # set n to the next new letter
    comp = comp + str(count) + n # add to string outside loop to include last update

    return comp



def decompressor(comp: str) -> str:
    # check if comp has alphanumeric characters
    if comp.isalnum() == False:
        print("Only alphanumeric characters are allowed when decompressing a source string.")
        return ""
    n = len(comp) # n finds number of characters in comp
    counter = 1 # set counter to an int to represent number of each letter
    decomp = "" # string decomp to add to
    # iterate by 2 since every other character is a number
    for i in range(0, n, 2):

        counter = int(comp[i]) # convert the number string to an int
        decomp = decomp + (comp[i + 1] * counter) # add to string decomp the amount of letters

    return decomp



def display_menu():
    print("\nWhat would you like to do?"
          "\n1. Compress"
          "\n2. Decompress"
          "\n3. Exit\n")

def receive_choice() -> str:
    display_menu()
    user_choice = input("Your choice: ")
    while user_choice not in ['1', '2', '3']:
        print("That is not a valid option."
              "\n---\n")
        user_choice = input("Your choice: ") # ask user for choice again

    return user_choice


def main():
    choice = receive_choice()
    while choice != '3':
        source_str = input("Enter the source string: ").lower()
        if choice == '1':
            print(compressor(source_str)) # print the result from compressor if 1 is inputted
        else:
            print(decompressor(source_str)) # print the result from decompressor if 2 is inputted
        choice = receive_choice()
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
