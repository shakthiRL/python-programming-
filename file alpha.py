def main():
    # Prompting the user for the name of the text file
    filename = input("Enter the name of the text file: ")

    try:
        # Open the file for reading
        with open(filename, 'r') as file:
            # Read the contents of the file
            contents = file.read()

            # Split the contents into words
            words = contents.split()

            # Create a set to store unique words
            unique_words = set()

            # Add each word to the set
            for word in words:
                unique_words.add(word)

            # Sort the unique words alphabetically
            unique_words = sorted(unique_words)

            # Print unique words
            print("Unique words in alphabetical order:")
            for word in unique_words:
                print(word)
    
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")

if __name__ == "__main__":
    main()
