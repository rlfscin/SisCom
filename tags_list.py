from graphics import giveMeTheGraphic
from matplotlib.pyplot import show
import os
import re

bits_reader = []
bits_tags = []
steps = []

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
            
            steps.append(float(bits['steps']))
            bits_reader.append(average_bits_reader)
            bits_tags.append(average_bits_tags)
            # print "%s tags - %f | %f" % (directory, average_bits_reader, average_bits_tags)

    
    def atoi(self, text):
        return int(text) if text.isdigit() else text
        
    def natural_keys(self, text):
       return [ self.atoi(c) for c in re.split('(\d+)', text) ]

    def plot_graphs(self):
        giveMeTheGraphic([(x+1)*100 for x in range(10)], bits_reader, "Etiquetas", "Media de Bits pelo Reader", 1, "Reader")
        giveMeTheGraphic([(x+1)*100 for x in range(10)], bits_tags, "Etiquetas", "Media de Bits por Tag", 1, "Tags")
        giveMeTheGraphic([(x+1)*100 for x in range(10)], steps, "Etiquetas", "Numero de Passos", 2, "Steps")

from qt import *
from qwt import *
tl = TagsList('./data')
tl.run_algorithm(qwt)
tl.plot_graphs()
show()