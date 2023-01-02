# Import OUI tools
from Mac import oui
# Import text_utilities for text processing
from Utilities import text_utilities as util

oui_id=oui.oui_id
# Create method to parse log
def dhcpack(list_of_values):
   # This sequence handles the fact that there are two different forms of DHCPACK
   if list_of_values[1] == "on":
      ipv4 = list_of_values[2]
      mac = util.remove_brackets(list_of_values[4]).upper()
      oui = mac[0:8]
             
   elif list_of_values[1] == "to":
      ipv4 = list_of_values[2]
      mac = util.remove_brackets(list_of_values[3]).upper()
      oui = mac[0:8]    
   # Check for nodetype and if nodetype is known
   if oui in oui_id:
      nodetype = oui_id[oui]
   else:
      nodetype = "Unknown"
   
   if list_of_values[1] == "to":
      node = list_of_values[4]
   else:
      # Call function to remove brackets
      node = util.remove_brackets(list_of_values[5])
      
   if node ==  "via":
      node = "Unknown"
   # Create variable to return the required information
   par_list = str(f"Type:{nodetype} IPv4:{ipv4} Mac:{mac} Node:{node}\n")
   return par_list
   


   
   




   