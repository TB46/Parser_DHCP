# Create function to remove duplicate files
def unduplicate(outputfile):
   # Create file Nodes.csv to hold final output
   finalfile = "nodes.csv"
   # Open input file as read only and pass contents of output file
   infile = open(outputfile, 'r')
   # Open output file as write only
   outfile = open(finalfile, 'w')
   # Create empty set
   list_lines = []
   # Craete loop to parse through infile
   for line in infile:
      if line in list_lines:
         continue
      # If a line is not in list_lines then add it and write to outfile
      else:
         outfile.write(line)
         list_lines.append(line)
  
   