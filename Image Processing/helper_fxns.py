#HELPER FUNCTIONS

"""
Contains certain Helper Functions
"""

#helper function to get the number of rows and columns needed in the picture            
def get_details(dictionary):
    values = list(dictionary.values())
    rows = set()
    cols = set()

    print(values)

    for i,j in values:
        rows.add(i)
        cols.add(j)

    return max(rows), max(cols)