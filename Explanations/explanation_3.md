### Description:
The goal is to write code for building a Huffman tree, encoding the data, and, lastly, decoding the data.
> A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

### Implementation process:
Followed the same pseudocode mentioned in the project.
 1. Function "frequency" takes a text string as input and returns a dictionary of the letters encountered with a count of how often they appear.
 2. Next function builds and sorts a list of tuples. This list will be the input for the main Huffman algorithm.
 3. Codes are assigned by recursively traversing the tree, keeping track of the left and right turns in the variable "pat".
 > code in our example: {'h': '000', 'i': '001', 'r': '010', 'T': '0110', 'b': '0111', 'o': '1000', 's': '1001', 't': '1010', 'w': '1011', ' ': '110', 'd': '1110', 'e': '1111'}

 4. The Huffman Tree is built by assigning the above  binary code to each letter.
 5. Encoding schema is built to make the text into its compressed form.
 6. Decoding schema is built to decode the text from its compressed form.

### Time Complexity: O(n)
The time complexity of the Huffman algorithm is O(n). There are O(n) iterations, one for each item.

### Space Complexity:
Space complexity is O(n). Where, n are the number of characters.
