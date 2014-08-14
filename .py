#!/usr/bin/python
#Stephen Talley
#Date: July 11, 2014
#Program for generating random ranked lists
import random
import csv

#This declaration creates a two-dimensional list i.e. a list of lists (the number of lists varies up to 100)
Listoflists=[[] for _ in range(random.randint(35,100))] 

#ListCreator function establishes an ordered list of a random length    
def ListCreator(list1): 
    for number in range(0,random.randint(25,100)):
        list1.append(number)

'''ListShuffle takes the ordered list from ListCreator
and shuffles the order to simulate a ranked list'''   
def ListShuffle(list1):
    random.shuffle(list1)

def main():
    outfile=open('TestLists.csv','wt')
    writer=csv.writer(outfile,lineterminator='\n')
    for element in Listoflists:
        ListCreator(element)
        ListShuffle(element)
        writer.writerow(element)#This command writes each list to the .csv file TestLists
    print Listoflists #Prints the entire two-dimensional list to verify that everything worked correctly
    outfile.close()
    
main()
