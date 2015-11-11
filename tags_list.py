import os
import re

class TagsList:
    
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.directories = os.listdir(base_dir)
        self.directories.sort(key=self.natural_keys)
        
    def generate_files_list(self, directory):
        files = os.listdir("%s/%s" % (self.base_dir, directory))
        
        return ['%s/%s' % (directory, file) for file in files]
            
    
    def generate_tags(self, file):
        return [line.rstrip('\n') for line in open("%s/%s" % (self.base_dir, file))]
    
    def run_algorithm(self, algorithm):
        for directory in self.directories:
            print directory
            total_bits_reader = 0
            total_bits_tags = 0
            
            files = self.generate_files_list(directory)
            
            for file in files:
                tags = self.generate_tags(file)
                
                bits = algorithm(tags)
                total_bits_reader += bits['bits_reader']
                total_bits_tags += bits['bits_tags']
            
            average_bits_reader = float(total_bits_reader) / len(files)
            average_bits_tags = float(total_bits_tags) / len(files)
            print "%s tags - %f | %f" % (directory, average_bits_reader, average_bits_tags)
    
    def atoi(self, text):
        return int(text) if text.isdigit() else text
        
    def natural_keys(self, text):
       return [ self.atoi(c) for c in re.split('(\d+)', text) ]

from qt import *
from qwt import *
tl = TagsList('./data')
tl.run_algorithm(qwt)