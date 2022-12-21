# r+ opens a file for both reading and writing. The file
# pointer will be at the beginning of the file.
# w+ Opens a file for both writing and reading. Overwrites
# the existing file if the file exists. If the file does
# not exist, creates a new file for reading and writing.

# writing files, using "with" will run .close() implicitly
with open("story.txt", "w+", encoding="utf-8") as f:
    f.write("Little red riding hood was \n")
    f.write("walking in the woods. \n")
    f.write("She picked flowers on her way to see her grandmother. \n")
    f.seek(0)           # reset cursor to start
    print(f.read())     # .read returns specified number of bytes

# try:
#     story = open("./story.txt", "r")
#     content = story.read()
#     print(content)      # print the content
# finally:                # if exception, will enforce .close()
#     story.close()


