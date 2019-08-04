### Description:
The goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

### Data structure:
Traversing is done by walking through tree of directories and searching for output files by defining a recursive function.

### Implementation process:
This code generate the file path with the required extension in a directory tree by walking the tree top-down.
For each directory in the tree rooted at directory top, it yields either a directory path or a file path
The dirpath is a string for the path to the directory. To get a full path (which begins with top) to a file or directory in dirpath, "os.path.join(dirpath, child)" is used.

### Time Complexity:
Time complexity of the traversal is O(n+m). However, O(m) might vary between O(1) to O(n^2), depending on how dense the tree is.

### Space Complexity:
Space complexity is O(n). Where, n is the depth of the tree

### References:
https://docs.python.org/3.7/library/os.path.html#os.path.isdir
