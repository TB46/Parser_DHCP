# Create a function to remove brackets
def remove_brackets(string_with_brackets):
   # Remove brackets with strip() function
   string_without_brackets = str(string_with_brackets.strip("()"))
   # Return string without brackets
   return string_without_brackets