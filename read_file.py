def read_file():
    file = open("sample.txt", "r")
    
    content = file.read()
    print("File Content:")
    print(content)
    
    file.close()

if __name__ == "__main__":
  read_file()