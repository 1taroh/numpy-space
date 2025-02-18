import numpy as np

class Space:
    def __init__(self, list_array_1d):
        """
        Input:
            **kwargs: 1d array list

        Example:
            >>> 
        """
        tuple_array_1d = [tuple(vector) for vector in list_array_1d]
        self.space = set(tuple_array_1d)

    def nparray_list(self):
        return [np.array(vector) for vector in self.space]

    def __str__(self):
        # V = {[1,2,3], [2,3,4]}
        formatted_output = "{" + ", ".join(str(vector) for vector in self.nparray_list()) + "}"
        return f"{formatted_output}"
    
    def __add__(self, other):
        s = self.space | other.space
        return Space(nparray_list(s))

    def __mul__(self, other):
        s = self.space & other.space
        return Space(nparray_list(s))

def nparray_list(s:set):
    return [np.array(vector) for vector in s]

