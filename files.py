# r+ opens a file for both reading and writing. The file
# pointer will be at the beginning of the file.
# w+ Opens a file for both writing and reading. Overwrites
# the existing file if the file exists. If the file does
# not exist, creates a new file for reading and writing.

# writing files
with open("story.txt", "w") as f:
    f.write("Little red riding hood was \n")
    f.write("walking in the woods. \n")
    f.write("She picked flowers on her way to see her grandmother. \n")

# opening files

# file object/handler
try:
    story = open("./story.txt", "r")
    content = story.read()
    print(content)      # print the content
finally:                # if exception, will enforce .close()
    story.close()

# using 'with', .close() will be run implicitly
# with open("./fruits.txt", "r") as fruits:
