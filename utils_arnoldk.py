''' ITERATION 3

Module: Alpha Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Process:
In this third iteration, additional variables have bee declared to show my ability to use different data types
'''

#####################################
# Declare a global variable-Keeping the byline at the end.
#We will use this information in a smarter byline
#####################################

#Boolean variables to indicate if the company has international clients.
has_international_client:bool = True

#Integer variable to determine the number of years in operation.
years_in_operation:int = 10

#List of strings representing the skills offered by the company
skills_offered:list = ["Data Analysis","Machine Learning","Business Intelligence"]

#List of floats representing individual client satisfaction
client_satisfaction_scores:list = [4.8,4.6,4.9,5.0,4.7]

#####################################
# Declare a global variable named byline.
#Make it a multiline f-string to show our information.
#####################################

byline:str = f"""
------------------------------------------------------------
Alpha Analytics: Delivering Transforming Insights
------------------------------------------------------------
Has International Clients: {has_international_client}
years in Operation: {years_in_operation}
Skills Offered: {skills_offered}
Client satisfaction Score:{client_satisfaction_scores}
"""

#####################################
# Define the get_byline() function.
#####################################

def get_byline()-> str:
    '''Return a byline for my analytics projects.'''
    return byline 

#####################################
# Define a main() function for this module.
#####################################

# The main function now calls get_byline() to retrieve the byline.

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())
    
    # Call main function if this script is executed directly
if __name__ == '__main__':
    main()
