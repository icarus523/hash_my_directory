import getpass
import logging
import os
import time
import hashlib
import hmac

from tkinter import *
from tkinter import filedialog
from datetime import datetime

## Change this only ##
HASHING_ALGORITHMS = ['sha256'] # choose/add (as a list) from below
ACCEPTABLE_ALGORITHMS = ['sha3_512', 'sha512', 'sha3_384', 'mdc2', 'md5', 'sha1','sha256','sha224', 'sha512_224', 'sha3_224']
HMAC = False 
SEED = "0000000000000000000000000000000000000000" # note: in Hash Calc to compare use Hex String = '00'
######################

MAXIMUM_BLOCKSIZE_TO_READ = 65535
program_name = 'hash_my_directory'
LOGGER_FNAME = 'hash_my_directory.log'

# Configure logging to file and format
logging.basicConfig(level=logging.DEBUG,
        format='%(message)s',
        filename=LOGGER_FNAME,
        filemode='w') # overwrite the log 'a' - appends to it

class HashMyDirectory: 

    # input: file to be hashed using hmac-sha1
    # output: hexdigest of input file    
    def dohash_hmacsha(self, fname, dm, chunksize=8192):
        # change this if you want other hashing types for HMAC, e.g. hashlib.md5
        key = bytes.fromhex(self.seed)
        m = hmac.new(key, digestmod = dm.name) 
        
        # Read in chunksize blocks at a time
        with open(fname, 'rb') as f:
            while True:
                block = f.read(chunksize)
                if not block: break
                m.update(block)      
        
        return m.hexdigest()
 
    def dohash(self, fname, m, chunksize=8192):
        # time.sleep(1) 
        # Read in chunksize blocks at a time
        with open(fname, 'rb') as f:
            while True:
                block = f.read(chunksize)
                if not block: break
                m.update(block)    
                      
        return m.hexdigest()

    def logResult(self, results_l, path, fname):
        hashes = ''
        result_str = ''

        for i in range(len(results_l)):
            hashes = hashes + results_l[i] + "\t" 

        # For neet output (default)
        #result_str = hashes + path + "\t" + fname # change order here

        # For CHK38
        result_str = fname + "\t" + hashes # change order here

        logging.getLogger().info(result_str)

    def logHeadings(self):
        def_str = "==== " + program_name + " started on: " + str(datetime.now()) + " by: " + getpass.getuser()  + " ===="
        logging.getLogger().info(def_str)
        heading_str = ''
        for i in range(len(HASHING_ALGORITHMS)):
            if HMAC and HASHING_ALGORITHMS[i].startswith('sha'): 
                heading_str = heading_str + "HMAC-"+HASHING_ALGORITHMS[i] + "\t"                
            else: 
                heading_str = heading_str + HASHING_ALGORITHMS[i] + "\t"

        heading_str = heading_str + "PATH" + "\t" + "FILENAME"  # change order here

        logging.getLogger().info(heading_str)

    def getHashLib(self, h_alg):
        m = None
        if h_alg == 'sha3_512': 
            m = hashlib.sha3_512()
        elif h_alg == 'sha512': 
            m = hashlib.sha512()
        elif h_alg == 'sha3_384': 
            m = hashlib.sha3_384()
        elif h_alg == 'mdc2': 
            m = hashlib.mdc2()
        elif h_alg == 'md5': 
            m = hashlib.md5()
        elif h_alg == 'sha3_384': 
            m = hashlib.sha3_384()                
        elif h_alg == 'sha1':
            m = hashlib.sha1()
        elif h_alg == 'sha256':
            m = hashlib.sha256()
        elif h_alg == 'sha224':
            m = hashlib.sha224()
        elif h_alg == 'sha512_224':
            m = hashlib.sha512_224()
        elif h_alg == 'sha3_224':
            m = hashlib.sha3_224()                
        else:
            logging.getLogger().error(h_alg, "unsupported hashing algorithm")
            sys.exit(1)
        return m

    def __init__(self):
        self.logHeadings()        
        self.root=Tk()
        self.root.withdraw() # hide Tk windows
        self.seed = SEED

        # select directory
        my_directory = filedialog.askdirectory(initialdir='.',title='Select Directory to Hash contents')

        # generate file list
        file_list = list() 
        for rootfs, dirs, files in os.walk(my_directory, topdown=True):
           for name in files:
              file_list.append(os.path.join(rootfs.replace("\\","/"), name)) # replace backslashes with forward slashes in path

        # generate a hash for each file
        for fname in file_list:
            results = list()
            
            if not os.path.isfile(fname): # sanity check
                print(fname, "not a file")
                pass
            else:
                m = None
                
                for h_alg in HASHING_ALGORITHMS:
                    assert(h_alg in hashlib.algorithms_available), hashlib.algorithms_available # is it supported?
                    assert(h_alg in ACCEPTABLE_ALGORITHMS), ACCEPTABLE_ALGORITHMS # is it acceptable? 
                    m = self.getHashLib(h_alg)
                    hash_result = dict() 
                    hash_result['type'] = h_alg
                    if HMAC and h_alg.startswith('sha'): 
                        hash_result['value'] = self.dohash_hmacsha(fname, m, MAXIMUM_BLOCKSIZE_TO_READ) # generate SHA256 hash                       
                    else: 
                        hash_result['value'] = self.dohash(fname, m, MAXIMUM_BLOCKSIZE_TO_READ) # generate SHA256 hash

                    results.append(hash_result['value'])

                self.logResult(results, os.path.dirname(fname), os.path.basename(fname))

        os.startfile(LOGGER_FNAME) # open the log file

def main():
    app = None
    app = HashMyDirectory() 

if __name__ == "__main__": main() 
