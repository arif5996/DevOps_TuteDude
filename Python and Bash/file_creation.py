def create_file():
    file = open("sample.txt", "w")
    
    file.write("Hello, World!\n")
    file.write("This is a text file created using Python.\n")
    file.write("Learning file handling is fun!")
    
    file.close()
    print("Content written to sample.txt successfully.")

if __name__ == "__main__":
  create_file()