import pandas as pd

feature_names = ['CountryName',
                 'CountryCode',
                 'IndicatorName',
                 'IndicatorCode',
                 'Year',
                 'Value']

row_vals = ['Arab World',
            'ARB',
            'Adolescent fertility rate (births per 1,000 women ages 15-19)',
            'SP.ADO.TFRT',
            '1960',
            '133.56090740552298']

# A list of lists consisting of multiple values similar to row_vals
row_lists = [['Arab World',
              'ARB',
              'Adolescent fertility rate (births per 1,000 women ages 15-19)',
              'SP.ADO.TFRT',
              '1960',
              '133.56090740552298'],
             ['Arab World',
              'ARB',
              'Age dependency ratio (% of working-age population)',
              'SP.POP.DPND',
              '1960',
              '87.7976011532547'],
             ['Arab World',
              'ARB',
              'Age dependency ratio, old (% of working-age population)',
              'SP.POP.DPND.OL',
              '1960',
              '6.634579191565161'],
             ['Arab World',
              'ARB',
              'Age dependency ratio, young (% of working-age population)',
              'SP.POP.DPND.YG',
              '1960',
              '81.02332950839141'],
             ['Arab World',
              'ARB',
              'Arms exports (SIPRI trend indicator values)',
              'MS.MIL.XPRT.KD',
              '1960',
              '3000000.0'],
             ['Arab World',
              'ARB',
              'Arms imports (SIPRI trend indicator values)',
              'MS.MIL.MPRT.KD',
              '1960',
              '538000000.0'],
             ['Arab World',
              'ARB',
              'Birth rate, crude (per 1,000 people)',
              'SP.DYN.CBRT.IN',
              '1960',
              '47.697888095096395'],
             ['Arab World',
              'ARB',
              'CO2 emissions (kt)',
              'EN.ATM.CO2E.KT',
              '1960',
              '59563.9892169935'],
             ['Arab World',
              'ARB',
              'CO2 emissions (metric tons per capita)',
              'EN.ATM.CO2E.PC',
              '1960',
              '0.6439635478877049'],
             ['Arab World',
              'ARB',
              'CO2 emissions from gaseous fuel consumption (% of total)',
              'EN.ATM.CO2E.GF.ZS',
              '1960',
              '5.041291753975099'],
             ['Arab World',
              'ARB',
              'CO2 emissions from liquid fuel consumption (% of total)',
              'EN.ATM.CO2E.LF.ZS',
              '1960',
              '84.8514729446567'],
             ['Arab World',
              'ARB',
              'CO2 emissions from liquid fuel consumption (kt)',
              'EN.ATM.CO2E.LF.KT',
              '1960',
              '49541.707291032304'],
             ['Arab World',
              'ARB',
              'CO2 emissions from solid fuel consumption (% of total)',
              'EN.ATM.CO2E.SF.ZS',
              '1960',
              '4.72698138789597'],
             ['Arab World',
              'ARB',
              'Death rate, crude (per 1,000 people)',
              'SP.DYN.CDRT.IN',
              '1960',
              '19.7544519237187'],
             ['Arab World',
              'ARB',
              'Fertility rate, total (births per woman)',
              'SP.DYN.TFRT.IN',
              '1960',
              '6.92402738655897'],
             ['Arab World',
              'ARB',
              'Fixed telephone subscriptions',
              'IT.MLT.MAIN',
              '1960',
              '406833.0'],
             ['Arab World',
              'ARB',
              'Fixed telephone subscriptions (per 100 people)',
              'IT.MLT.MAIN.P2',
              '1960',
              '0.6167005703199'],
             ['Arab World',
              'ARB',
              'Hospital beds (per 1,000 people)',
              'SH.MED.BEDS.ZS',
              '1960',
              '1.9296220724398703'],
             ['Arab World',
              'ARB',
              'International migrant stock (% of population)',
              'SM.POP.TOTL.ZS',
              '1960',
              '2.9906371279862403'],
             ['Arab World',
              'ARB',
              'International migrant stock, total',
              'SM.POP.TOTL',
              '1960',
              '3324685.0']]


# This consumes the iterator, commenting out
#   for feature, value in zipped_lists:
#       print(feature, value)


# Define lists2dict(), function
def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""

    # Zip lists: zipped_lists
    zipped_lists = zip(list1, list2)

    # Create a dictionary: rs_dict
    dictionary = dict(zipped_lists)

    return dictionary


# Define read_large_file()
def read_large_file(file_object, skip_colnames=False):
    """A generator function to read a large file lazily."""

    if skip_colnames:
        file_object.readline()

    # Loop indefinitely until the end of the file
    while True:

        # Read a line from the file: data
        data = file_object.readline()

        # Break if this is the end of the file
        if not data:
            break

        yield data


def process_file_differently(path):
    """
    Process the file line by line using the file's returned iterator
    """
    try:
        with open(path) as file_handler:
            # while True:
            for i in range(3):
                print(next(file_handler))
    except (IOError, OSError):
        print("Error opening / processing file")
    except StopIteration:
        pass


# Call lists2dict: rs_fxn
rs_fxn = lists2dict(feature_names, row_vals)

# Print rs_fxn
print("From function", rs_fxn)

# USING LIST COMPREHENSIONS

# Print the first two lists in row_lists
print(row_lists[0])
print(row_lists[1])

# Turn list of lists into list of dicts: list_of_dicts
# LIST COMPREHENSIONS: [output expression for variable in iterable]
list_of_dicts = [lists2dict(feature_names, row_list) for row_list in row_lists]

# Print the first two dictionaries in list_of_dicts
print(list_of_dicts[0])
print(list_of_dicts[1])

# Turn list of dicts into a DataFrame: df
df = pd.DataFrame(list_of_dicts)

# Print the head of the DataFrame
print(df.head())

# Processing data in chunks (1)

# The most widely used python_basics of context managers is the with statement
# Open a connection to the file
with open('datasets/world_ind_pop_data.csv', 'r') as file:
    # Skip the column names
    file.readline()

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Process only the first 1000 rows
    for j in range(1000):

        # Split the current line into a list: line
        line = file.readline().split(',')

        # Get the value for the first column: first_col
        first_col = line[0]

        # If the column value is in the dict, increment its value
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1

        # Else, add to the dict and set value to 1
        else:
            counts_dict[first_col] = 1

# Print the resulting dictionary
print(counts_dict)

# Open a connection to the file
with open('datasets/world_ind_pop_data.csv', 'r') as file:
    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)

    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))

# The following is supposed to work similarly as files return lazy iterators to begin with
process_file_differently('datasets/world_ind_pop_data.csv')

# Initialize an empty dictionary: counts_dict
counts_dict_2 = {}

# Open a connection to the file
with open('datasets/world_ind_pop_data.csv', 'r') as file:
    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict_2.keys():
            counts_dict_2[first_col] += 1
        else:
            counts_dict_2[first_col] = 1

# Print
print(counts_dict_2)

# Initialize an empty dictionary: counts_dict
counts_dict_2 = {}

# Open a connection to the file
with open('datasets/world_ind_pop_data.csv', 'r') as file:
    # Iterate over the generator from read_large_file()
    for line in read_large_file(file, skip_colnames=True):

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict_2.keys():
            counts_dict_2[first_col] += 1
        else:
            counts_dict_2[first_col] = 1

# Print
print(counts_dict_2)
