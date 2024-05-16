# Example Sequence File For Landscape_DataStream v1.0

import numpy as np

# Functions
def array1D(start, end, step):
    if start <= end:
        step = +abs(step)
    else:
        step = -abs(step)
    array = np.arange(start, end, step)
    array = np.append(array, end)
    array = array.tolist()
    return array

def array1Dnum(start, end, number):
    array = np.linspace(start, end, number)
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
        line = line + 1
    for d1 in array1D(start, end, step)[::-1]:
        array1.append([1, line, d1])
        line = line + 1
    return array1

def sarray2D(start1, end1, step1, start2, end2, step2):
    # First column is file suffix: 0 is original dataset, 1 is retrace dataset, 2 is dump dataset
    # Second column is index: 0,1,2,3,4,5,...
    # From the third column is the scan array
    line = 0
    array2 = []
    for d2 in array1D(start2, end2, step2):
        for d1 in array1D(start1, end1, step1):
            array2.append([0, line, d1, d2])
            line = line + 1
        for d1 in array1D(start1, end1, step1)[::-1]:
            array2.append([1, line, d1, d2])
            line = line + 1
    return array2

### ------------------------------------------------------------------------------------------ ###

# Instrument

def internal_example(*arg):
    instrument_parameters = [
        ("Description", "This is a standard instrument"),
        ("Version", "1.0"),
        ("Type", "Default"), # Default\External\Python
        ("Address", ""),
        # Scan Setup
        ("Scan Command", ""),
        ("Retrieve Command", ""),
        ("Scan Name", "Lock-in1 Set"),
        ("Ramp Step", "10mV"),
        ("Ramp Delay", "0ms"),
        ("Scan Limit", "-Inf\+Inf"),
        ("Scan Stablize", "False"),
        ("Scan Stablize Timeout", "0s"),
        ("External VI Behavior", "Mini"),
        # Read Setup
        ("Read Command", ""),
        ("Read Name", "R1\R2\R3"),
        ("Buffer", "True"),
    ]
    return instrument_parameters

def external_example(*arg):
    instrument_parameters = [
        ("Description", "This is an external instrument"),
        ("Version", "1.0"),
        ("Type", "External"), # Internal\External\Python
        ("Address", "D:\Files\Programs\LV2024\Landsacpe DataStream v1.0\VI Based Instrument\Empty Instrument.vi"),
        # Scan Setup
        ("Scan Command", ""),
        ("Scan Name", "Lock-in1 Set"),
        ("External VI Behavior", "Mini"),
        # Read Setup
        ("Read Command", ""),
        ("Read Name", "R1\R2\R3"),
    ]
    return instrument_parameters

def python_example1(*arg):
    instrument_parameters = [
        ("Description", "This is a python instrument"),
        ("Version", "1.0"),
        ("Type", "Python"), # Internal\External\Python
        ("Address", "D:\Files\Programs\LV2024\Landsacpe DataStream v1.0\Python Based Instrument\Python_Instrument_Example.py"),
        # Scan Setup
        ("Scan Command", ""),
        ("Scan Name", "Lock-in1 Set"),
        # Read Setup
        ("Read Command", ""),
        ("Read Name", "R1\R2\R3"),
    ]
    return instrument_parameters

def python_example2(*arg):
    instrument_parameters = [
        ("Description", "This is a python instrument"),
        ("Version", "1.0"),
        ("Type", "Python"), # Internal\External\Python
        ("Address", "D:\Files\Programs\LV2024\Landsacpe DataStream v1.0\Python Based Instrument\Python_Instrument_Example.py"),
        # Scan Setup
        ("Scan Command", ""),
        ("Scan Name", "Lock-in1 Set"),
        # Read Setup
        ("Read Command", ""),
        ("Read Name", "R1\R2\R3"),
    ]
    return instrument_parameters

def infiniteloop(*arg):
    instrument_parameters = [
        ("Description", "This is a python instrument"),
        ("Version", "1.0"),
        ("Type", "Python"), # Internal\External\Python
        ("Address", "D:\Files\Programs\LV2024\Landsacpe DataStream v1.0\Python Based Instrument\Inifinite Loop.py"),
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
        "DefaultExternal",
        "PythonPython",
        "inflp",
    ]
    return allsequence
    

def DefaultExternal(*arg):
    # First column is file suffix 0 is original dataset, 1 is retrace dataset, ...
    # Second column is index: 0,1,2,3,4,5,...
    # From the third column is the scan array

    description = "One Default Instrument + One External Instrument"

    dataset_info = [
        ("Description", description),
        ("File Name", "//sdasda/dsad"),
        ("Dataset Name", "New Dataset"),
        ("Note", ""),
        ("Scan Delay", "0ms"),
        ("Read Interval", "0ms"),
        ("Read Repeat", "1"),
        ("Read After Scan", "False"),
    ]

    scan_instrument = [
        "internal_example",
        "external_example"
    ]

    read_instrument = [
        "internal_example",
        "external_example"
    ]

    # Instrument 1
    start_1 = 0
    end_1 = 10
    step_1 = 0.1

    # Outer Loop Instrument
    start_2 = 10
    end_2 = 20
    step_2 = 0.1

    dataset_info = dataset_info + [
        ("x_start", str(start_1)),
        ("x_end", str(end_1)),
        ("x_step", str(step_1)),
        ("y_start", str(start_2)),
        ("y_end", str(end_2)),
        ("y_step", str(step_2)),
        ("z", "gx"),
    ]

    data_processing = [
        ("gx", "col(Lock-in1 Set)+col(Lock-in1 Set*)"),
        ("gy", "col(Lock-in1 Set)-col(Lock-in1 Set*)"),
        ("gz", "col(gx)-col(gy)"),
    ]

    return (dataset_info, scan_instrument, read_instrument , sarray2D(start_1, end_1, step_1, start_2, end_2, step_2), data_processing)

def PythonPython(*arg):
    # First column is file suffix 0 is original dataset, 1 is retrace dataset, ...
    # Second column is index: 0,1,2,3,4,5,...
    # From the third column is the scan array

    description = "Two Python Instrument"

    dataset_info = [
        ("Description", description),
        ("File Name", ""),
        ("Dataset Name", "New Dataset"),
        ("Note", ""),
        ("Scan Delay", "0ms"),
        ("Read Interval", "0ms"),
        ("Read Repeat", "5"),
        ("Read After Scan", "False"),
    ]

    scan_instrument = [
        "python_example1",
        "python_example2",
    ]

    read_instrument = [
        "python_example1",
        "python_example2"
    ]


    # Instrument 1
    start_1 = 0
    end_1 = 1
    step_1 = 0.01

    # Outer Loop Instrument
    start_2 = 0
    end_2 = 1
    step_2 = 0.01

    dataset_info = dataset_info + [
        ("x_start", str(start_1)),
        ("x_end", str(end_1)),
        ("x_step", str(step_1)),
        ("y_start", str(start_2)),
        ("y_end", str(end_2)),
        ("y_step", str(step_2)),
        ("z", "gx"),
    ]

    data_processing = [
        ("gx", "col(R1)+col(R2)"),
        ("gy", "col(R1)-col(R2)"),
        ("gz", "col(gx)-col(gy)"),
    ]

    return (dataset_info, scan_instrument, read_instrument , sarray2D(start_1, end_1, step_1, start_2, end_2, step_2), data_processing)

def inflp(*arg):
    # First column is file suffix 0 is original dataset, 1 is retrace dataset, ...
    # Second column is index: 0,1,2,3,4,5,...
    # From the third column is the scan array

    description = "Test Instrument"

    dataset_info = [
        ("Description", description),
        ("File Name", ""),
        ("Dataset Name", "New Dataset"),
        ("Note", ""),
        ("Scan Delay", "0ms"),
        ("Read Interval", "0ms"),
        ("Read Repeat", "5"),
        ("Read After Scan", "False"),
    ]

    scan_instrument = [
        "infiniteloop",
    ]

    read_instrument = [
        "python_example1",
        "python_example2"
    ]


    # Instrument 1
    start_1 = 0
    end_1 = 1
    step_1 = 0.1

    # Outer Loop Instrument
    start_2 = 0
    end_2 = 1
    step_2 = 0.1

    dataset_info = dataset_info + [
        ("x_start", str(start_1)),
        ("x_end", str(end_1)),
        ("x_step", str(step_1)),
        ("y_start", str(start_2)),
        ("y_end", str(end_2)),
        ("y_step", str(step_2)),
        ("z", "gx"),
    ]

    data_processing = [
        ("gx", "col(R1)+col(R2)"),
        ("gy", "col(R1)-col(R2)"),
        ("gz", "col(gx)-col(gy)"),
    ]

    return (dataset_info, scan_instrument, read_instrument , sarray1D(start_1, end_1, step_1), data_processing)

### ------------------------------------------------------------------------------------------ ###

def main():
    pass

if __name__ == '__main__':
    main()