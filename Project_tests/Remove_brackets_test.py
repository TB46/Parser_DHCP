# Import Unittest  and function to be tested
import unittest
from Utilities.text_utilities import remove_brackets

# Create a class to inerit from unittest.TestCase 
class Testbrackets(unittest.TestCase):
   # Name the function with prefix test
   def test_text_utilities(self):
      # Define variable to be passed in argument
      test_text = ("DHCPACK on 192.168.5.168 to c8:4b:d6:0a:77:2d (A-76MRRL3) via eth0")
      # Call the function dhcpack
      result = remove_brackets(test_text)
      # Assert method to verify result
      self.assertEqual(result, "DHCPACK on 192.168.5.168 to c8:4b:d6:0a:77:2d A-76MRRL3 via eth0" )

# Main for function call
if __name__ =="__main__":
   unittest.main()

                                                        
