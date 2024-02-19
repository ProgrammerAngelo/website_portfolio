# ========== PSEUDO CODE ==========
# - Def function
def count_lines():
    file = open("story.txt","r")
    count= 0
    
    # - Using for loop
    for i in file:
        count+= 1
    file.close()
    print("The number of lines in the 'story.txt' file is", count)

# - Caller of the def function
count_lines()

