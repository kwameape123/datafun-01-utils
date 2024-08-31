''' ITERATION 4

Module: Alpha Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do. We also experiment with some basic statistics.

Process:
To calculate some basic statistics we use:
-The built in max() and min() function and
-The statistics module to calculate the mean and standard deviation of some variables.
'''
#####################################
# Import Modules at the Top
#####################################

#In Python, we can import modules to add extra tools and functions.
#Below, we are importing:
#-'statistics module':This gives us tools to calculate important statistical measures.

import statistics

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
# Calculate Basic statistics.
#   Do this BEFORE we declare a byline.
#   So the values have been calculated
#   and ready for use in the byline.
#####################################

min_score:float = min(client_satisfaction_scores)
max_score:float = max(client_satisfaction_scores)
mean_score:float = statistics.mean(client_satisfaction_scores)
stdev_score:float = statistics.stdev(client_satisfaction_scores)

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
