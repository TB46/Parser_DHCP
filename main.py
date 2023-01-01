from Utilities import dhcp_parse as par
from Utilities import unduplicate as undup
from Mac import oui as oui
import csv

if (__name__ == '__main__'):
   print(f"This module is called {__name__} and executes as a standalone script")
   # Create variable logfilename for dhcpd log 
   logfilename = "Unprocessed\dhcpd.log"
   # Open logfile as read only
   logfile = open(logfilename, "r") 
   # Create variable outputfile to store processed data
   outputfile = "Processed\output.csv"
   
   # Open outputfile in append mode, newline removes blank line.
   with open (outputfile, "a", newline='') as f:
   
   # Iterate through each line in logfile
      for line in logfile:  
         # Parse each line to identify its type. Discard data before position 34 as not required
         useful_data = line[34:]
         # Split the useful_data into segments separated by a space
         list_of_values = useful_data.split(" ")
         # Handle each sentence type
         if list_of_values[0] == "DHCPDISCOVER":
         # Nothing to see here
            pass
         elif list_of_values[0] == "DHCPREQUEST":
         # Nothing to see here
            pass
         elif list_of_values[0] == "DHCPACK":
            # Pass required values through parse function
            par_list = par.dhcpack(list_of_values)

            # Create the csv writer
            writer = csv.writer(f)
            # Write a row to the csv file from parsed list                   
            writer.writerow(par_list.split())

   # Pass contents of output file through the unduplicate function         
   undup.unduplicate(outputfile)   

else:
   print(f"This module is called {__name__} and is being called by another script")
