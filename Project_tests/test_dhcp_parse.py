# Import Unittest  and function to be tested
import unittest
from Utilities.dhcp_parse import dhcpack

# Create a class to inerit from unittest.TestCase 
class Testdhcpack(unittest.TestCase):
   # Name the function with prefix test
   def test_dhcpack(self):
      # Define variable to be passed in argument
      test_text = ("DHCPACK on 192.168.5.168 to c8:4b:d6:0a:77:2d (A-76MRRL3) via eth0")
      # Call the function dhcpack
      result = dhcpack(test_text)
      # Assert method to verify result
      self.assertEqual(result, "Type:Dell, IPv4:192.168.5.168, Mac:c8:4b:d6:0a:77:2d Node:A-76MRRL3")

# Main for function call
if __name__ =="__main__":
   unittest.main()

 