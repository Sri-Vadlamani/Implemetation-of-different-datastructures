import os

def find_files(path, suffix, files=[]):
    if os.path.isfile(path):
        return files.append(path)
    for item in os.listdir(path):
        item = os.path.join(path, item)
        if os.path.isfile(item):
            if suffix in item:
                files.append(item)
        else:
            files = find_files(item, suffix, files)
    return files


print("--------------------------Test Case 1:printing .h files-------------------------")
for f in find_files("C:/Users/ganip/Downloads/testdir",'.h', []):
    print(f)

print("---------------Test Case 2: printing .c files-------------------------")
for f in find_files("C:/Users/ganip/Downloads/testdir",'.c', []):
    print(f)

print("---------------Test Case 3: printing all the files------------------------")
for f in find_files("C:/Users/ganip/Downloads/testdir",'.', []):
    print(f)
    
print("---------------Test Case 4: printing files in sub directory-------------------------")
for f in find_files("C:/Users/ganip/Downloads/testdir/subdir1",'', []):
    print(f)
