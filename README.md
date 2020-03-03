# hash_my_directory
Got annoyed at the limitations of both HashCalc and HashMyFiles. So I made my own. 

- Paste a complete path, instead of navigating to a directory
- By default, traverses entire directory and hashes all files. 
- Supports the following hashing algorithms: 

```
ACCEPTABLE_ALGORITHMS = ['sha3_512', 'sha512', 'sha3_384', 'sha3_384', 'mdc2', 'md5', 'sha3_384', 'sha1','sha256','sha224', 'sha512_224', 'sha512_224','sha3_224']
```

- hashing algorithm support can be easily modified by end-user - add a your favourite obscure algorithm: 

``` 
import hashlib
print(hashlib.algorithms_available)
```

- Support 'HMAC' with Seeds on SHA-type algorithms, default is zero seed or Hex string = ‘00’ for HMAC

```
HMAC = False 
SEED = "0000000000000000000000000000000000000000" # note: in Hash Calc to compare use Hex String = '00'
```

- Outputs in the expected format for CHK35, i.e. tab delimited
- Can output more than one type of hash via 

`HASHING_ALGORITHMS = ['sha256', 'sha1','md5'] # choose/add (as a list) from below`

- No issues with path length in Windows

# To Use
1. Open hash_my_directory.py in IDLE (default python text editor) 
2. Make changes based on your hashing parameters, i.e. Seed, HMAC, types of algorithms to use.
3. In your file navigation browser, copy the complete path that you wish to hash. 
4. Paste the path to the directory in the dialog window that pops up, and hit Enter
3. Review results. 
