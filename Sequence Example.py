# Example Sequence File For Landscape_DataStream v1.0
import numpy as np

# Functions
def array1D(start, end, step):
    if start <= end:
        step = +abs(step)
    else:
        step = -abs(step)
    array = np.arange(start,end,step)
    array = np.append(array, end)
    return array.tolist()

def array1Dnum(start,end,number):
    array = np.linspace(start,end,number)
    array = array.tolist()
    return array

def sarray1D(start,end,step):
    # First column is file suffix: 0 is original dataset, 1 is retrace dataset, 2 is dump dataset
    # Second column is index: 0,1,2,3,4,5,...
    # From the third column is the scan array
    line = 0
    array1 = []
    for d1 in array1D(start, end, step):
        array1.append([0, line, d1])
    for d1 in array1D(end, start, step):
        array1.append([1, line, d1])
    return array1

def sarray2D(start1,end1,step1,start2,end2,step2):
    # First column is file suffix: 0 is original dataset, 1 is retrace dataset, 2 is dump dataset
    # Second column is index: 0,1,2,3,4,5,...
    # From the third column is the scan array
    line = 0
    array2 = []
    for d2 in array1D(start2, end2, step2):
        for d1 in array1D(start1, end1, step1):
            array2.append([0, line, d1, d2])
            line = line + 1
        for d1 in array1D(end1, start1, step1):
            array2.append([1, line, d1, d2])
            line = line + 1
    return array2

### ------------------------------------------------------------------------------------------ ###

# Instrument

def internal_example(*arg):
    instrument_parameters = [
        ("Description", "Lock-in SR860-1"),
        ("Version", "1.0"),
        ("Type", "Internal"), # Internal\External\Python
        ("Address", ""),
        # Scan Setup
        ("Scan Command", ""),
        ("Scan Name", "Lock-in1 Set"),
        ("Ramp Step", "10mV"),
        ("Ramp Delay", "10ms"),
        ("Scan Limit", "-Inf\+Inf"),
        ("Scan Stablize", "True"),
        ("Scan Stablize Timeout", "600s"),
        ("Scan External VI Behavior", "Show"),
        # Read Setup
        ("Read Command", ""),
        ("Read Name", "R1\R2\R3"),
        ("Read External VI Behavior", "Hide"),
        ("Buffer", "True"),
    ]
    return instrument_parameters

def external_example(*arg):
    instrument_parameters = [
        ("Description", "Lock-in SR860-1"),
        ("Version", "1.0"),
        ("Type", "External"), # Internal\External\Python
        ("Address", ""),
        # Scan Setup
        ("Scan Command", ""),
        ("Scan Name", "Lock-in1 Set"),
        ("Scan External VI Behavior", "Show"),
        # Read Setup
        ("Read Command", ""),
        ("Read Name", "R1\R2\R3"),
        ("Read External VI Behavior", "Hide"),
    ]
    return instrument_parameters

def python_example(*arg):
    instrument_parameters = [
        ("Description", "Lock-in SR860-1"),
        ("Version", "1.0"),
        ("Type", "Python"), # Internal\External\Python
        ("Address", ""),
        # Scan Setup
        ("Scan Command", ""),
        ("Scan Name", "Lock-in1 Set"),
        # Read Setup
        ("Read Command", ""),
        ("Read Name", "R1\R2\R3"),
    ]
    return instrument_parameters


### ------------------------------------------------------------------------------------------ ###

# Measurement Sequence

def get_all_sequence(*arg):

    allsequence = [
        "line1",
        "line2",
    ]
    return 0
    

def line1(*arg):
    # First column is file suffix 0 is original dataset, 1 is retrace dataset, ...
    # Second column is index: 0,1,2,3,4,5,...
    # From the third column is the scan array

    description = "Test Instrument"

    dataset_info = [
        ("File Name", "Empty File"),
        ("Dataset Name", "Empty Dataset"),
        ("Note", "No Note")
    ]

    scan_instrument = [
        "lock-in1",
        "lock-in2"
    ]

    read_instrument = [
        "lock-in1",
        "lock-in2"
    ]


    # Instrument 1
    start_1 = 0
    end_1 = 1000
    step_1 = 1

    # Outer Loop Instrument
    start_2 = 0
    end_2 = 1000
    step_2 = 1

    return (dataset_info, scan_instrument, read_instrument , sarray2D(start_1,end_1,step_1,start_2,end_2,step_2))

### ------------------------------------------------------------------------------------------ ###

if __name__ == '__main__':
    pass
