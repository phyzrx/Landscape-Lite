# Example Instrument Setup For Landscape_DataStream v1.0
from time import sleep

def Call(parameters):
    # parameters is a list of tuples.
    parameters = list(parameters)
    for pair in parameters:
        (parameter_name, parameter_value) = pair
        if parameter_name == "setup1":
            setup1 = parameter_value
        elif parameter_name == "setup2":
            setup2 = parameter_value
        else:
            pass
    
    returnstr = "Example is Called"
    print(returnstr)
    return (parameters, returnstr)

def Initialize(*arg):

    returnstr = "Example is Initialized"
    print(returnstr)
    return returnstr

def Retrieve(*arg):

    returnstr = "-10987"
    print(returnstr)
    return returnstr

def Scan(Scan_Value):

    # sleep(0.05)
    returnstr = "Example scanned to " + str(Scan_Value)
    stb = False
    stbtime = 765

    print(returnstr, stb, stbtime)
    return (returnstr, stb, stbtime)

def Write():
    
    returnstr = "Write to Example"
    print(returnstr)
    return returnstr

def Read():

    returnstr = "-10,-9,-8,-7,-6,-5,-4,-3,-2,-1"
    print(returnstr)
    return returnstr

def Close():

    returnstr = "Example is closed"
    print(returnstr)
    return returnstr

if __name__ == '__main__':
    pass
