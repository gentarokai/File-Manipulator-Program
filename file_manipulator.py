import shutil
import sys

# reverse
def reverse_inputpath_outputpath(fileinput, fileoutput):
    with open(fileinput) as f:  
        contents = f.readlines()
        with open(fileoutput, "w") as f:
            # read contents reversevely
            for elm in contents[::-1]:
                f.writelines(elm[::-1])

# copy the contens
def copy_inputpath_outputpath(fileinput, fileoutput):
    # copy the entire file
    shutil.copy(fileinput, fileoutput)

# 
def duplicate_contents_inputpath_n(fileinput, fileoutput, number):
    with open(fileinput) as f:
        contents = f.readlines()
        # clear contents and add new
        with open(fileoutput, "w") as f:
            if number == 0 : return
            # read contents reversevely
            for elm in contents[0::]:
                f.writelines(elm)

        for i in range(0, number-1): # duplicate "number" times
            with open(fileoutput, "a") as f:
                # read contents reversevely
                for elm in contents[0::]:
                    f.writelines(elm)

# 
def replace_string_inputpath_needle_newstring(fileinput, fileoutput):
    # find needle
    with open(fileinput) as f:
        contents = f.readlines()

        with open(fileoutput, "w") as f:
            for i in range(len(contents)):
                if "needle" in contents[i]:
                    contents[i] = contents[i].replace("needle", "newstring")
                f.writelines(contents[i])

def main():
    # check if all args exist
    try:
        manipulation_type = sys.argv[1]
        fileinput = sys.argv[2]
        fileoutput = sys.argv[3]
    except:
        print("error: manipulation_type is not correct. Please input correct argument")
    
    # match is available after 3.10
    match manipulation_type:
        case "reverse":            
            return reverse_inputpath_outputpath(fileinput, fileoutput)
        case "copy":
            return copy_inputpath_outputpath(fileinput, fileoutput)
        case "duplicate":
            try:
                number = sys.argv[4]
            except:
                print("error: Missing number of duplication")
            return duplicate_contents_inputpath_n(fileinput, fileoutput, int(number))
        case "replace":
            return replace_string_inputpath_needle_newstring(fileinput, fileoutput)

main()