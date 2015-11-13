from graphics import giveMeTheGraphic
from matplotlib.pyplot import show
import os
import re

class TagsList:
    
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.directories = os.listdir(base_dir)
        self.directories.sort(key=self.natural_keys)

        self.bits_reader = []
        self.bits_tags = []
        self.steps = []
        
    def generate_files_list(self, directory):
        files = os.listdir("%s/%s" % (self.base_dir, directory))
        
        return ['%s/%s' % (directory, file) for file in files]
            
    
    def generate_tags(self, file):
        return [line.rstrip('\n') for line in open("%s/%s" % (self.base_dir, file))]
    
    def run_algorithm(self, algorithm):
        for directory in self.directories:
            print  "Running for %s tags..." % directory
            total_bits_reader = 0
            total_bits_tags = 0
            total_step_count = 0
            
            files = self.generate_files_list(directory)
            
            for file in files:
                tags = self.generate_tags(file)
                
                bits = algorithm(tags)
                total_bits_reader += bits['bits_reader']
                total_bits_tags += bits['bits_tags']
                total_step_count += bits['step_count']
            
            average_bits_reader = float(total_bits_reader) / len(files)
            average_bits_tags = float(total_bits_tags) / len(files)

            average_step_count = float(total_step_count) / len(files)
            
            print "Finished running for %s tags - transfered avg %f bits per tag and avg %f bits per tag in avg %f steps" % (directory, average_bits_reader, average_bits_tags/int(directory), average_step_count)

            
            self.steps.append(average_step_count)
            self.bits_reader.append(average_bits_reader)
            self.bits_tags.append(average_bits_tags)
    
    def atoi(self, text):
        return int(text) if text.isdigit() else text
        
    def natural_keys(self, text):
       return [ self.atoi(c) for c in re.split('(\d+)', text) ]

    def plot_graphs(self, name):
        giveMeTheGraphic([(x+1)*100 for x in range(len(self.directories))], self.bits_reader, "Etiquetas", "Media de Bits pelo Reader", 1, name)
        giveMeTheGraphic([(x+1)*100 for x in range(len(self.directories))], self.bits_tags, "Etiquetas", "Media de Bits por Tag", 2, name)
        giveMeTheGraphic([(x+1)*100 for x in range(len(self.directories))], self.steps, "Etiquetas", "Numero de Passos", 3, name)

        self.bits_reader = []
        self.bits_tags = []
        self.steps = []

from qt import *
from qwt import *

tl = TagsList('./data128')
print "RUNNING QT"
tl.run_algorithm(qt)
tl.plot_graphs('QT')

print "\n\nRUNNING QwT"
tl.run_algorithm(qwt)
tl.plot_graphs('QwT')

show()
