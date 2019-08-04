### Description:
BlockChain is a sequential chain of records, sort of like a linked list. Each block contains some information and they are connected together to form a chain.
* Components of a blockchain: A block in a simple blockchain consists of following components:
 * Timestamp : to save the date and time of creation of block
 * Data : data to be stored
 * Hash : to ensure integrity and to identify that block. Usually created by hashing any of the  other 4 values
 * Previous hash : hash of the previous block

### Data structure:
* Hash and linked list.
* Blockchain technology extensively depends on the hash functions.
* The SHA-256 hash function gets any string and returns a 256 bit (32 bytes) string

### Implementation process:
1. First a Block class is created to represent a block and calc_hash() function to calculate hash.
2. Implemented linked list to link the 5 blocks of data
6. Printed timestamp, data, Hash and previous hash values for each block in the blockchain

### Time Complexity:
The average time complexity of search by hash is and also implementation of linked lists is O(1).

### Space Complexity:
The space complexity of search by hash is O(n).
