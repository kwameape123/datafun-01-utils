''' ITERATION 2

Module: Alpha Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Process:
In this second iteration,add a function that returns the byline as a string.

1.I'll create a function named get_byline()
   
2. I'll return my byline to whatever calls the get_byline() function .

3. I'll update the main() function to use the new get_byline() function.

4. Same conditional boilerplate at the end.

I'll test this version in an online interpreter to ensure this version runs correctly before continuing.
It will demonstrate my ability to:
-declare variables of different types.
-Use Python to calculate basic descriptive statistics.
'''

#####################################
# Declare a global variable named byline.
#####################################

byline: str = 'Alpha Analytics: Delivering Transforming Insights'

#####################################
# Define the get_byline() Function.
#####################################

def get_byline()->str:
    '''Return a byline for my analytics projects.'''
    return byline 

#####################################
# Define a main() function for this module.
#####################################

# The main function now calls get_byline() to retrieve the byline.

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
