# hash_my_directory
improvements to Hash My Files application

- Supports the following hashing algorithms: 

`ACCEPTABLE_ALGORITHMS = ['sha3_512', 'sha512', 'sha3_384', 'sha3_384', 'mdc2', 'md5', 'sha3_384', 'sha1','sha256','sha224', 'sha512_224', 'sha512_224','sha3_224']`

- Outputs in the expected format for CHK35
- Can output more than one type of hash via 

`HASHING_ALGORITHMS = ['sha256', 'sha1'] # choose/add (as a list) from below`

- No issues with path length
- multithreaded
