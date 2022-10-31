#!/usr/bin/env python
# coding: utf-8

# <div style="float:left">
#     <h1 style="width:450px">Practical 4: Object-Oriented Programming</h1>
#     <h2 style="width:450px">Getting to grips with Functions &amp; Packages</h2>
# </div>
# <div style="float:right"><img width="100" src="https://github.com/jreades/i2p/raw/master/img/casa_logo.jpg" /></div>

# <div class="alert alert-block alert-warning">
#     <b>&#9888; Important</b>: This is a very long practical and it's <em>not</em> expected that you will get through it in the alloted time. The priorities here should be tasks 1--4. Task 5 is something you will probably want to revist before the start of group work (because packges of functions are useful when multiple people are working on the same code). Task 6 will help you to understand <i>how</i> to build your own classes in greater detail, but it is enough to understand that classes exist in hierarchies (as covered in the live session).</div>

# ## Task 1 (Revisited). Why 'Obvious' is Not Always 'Right'
# 
# Practical 3 is hard, so I want to provide _another_ chance for the concepts to bed in before we use them in an *object-oriented way through Pandas*. Yes, Week 5 will show how we combine concepts covered over the preceding two weeks in *practice* to do data science. 
# 
# So remember the finding from last week: if we don't really care about column order, then a dictionary of lists would be a nice way to handle data. And why should we care about column order? With our CSV file we saw what a pain it was to fix things when even a tiny thing like the layout of the columns changed. But if, instead, we could just reference the 'Description' column in the data set then it doesn't matter where that column actually is *and* we would know that all the descriptions would be *text*, while all the populations or prices would be *numbers*. Why is that? 

# ### Task 1.1 The Way That Doesn't Work
# 
# <div class="alert alert-block alert-success"><b>Difficulty level</b>: Low (this time around).</div>
# 
# Here are four rows of 'data' for city sizes organised by _row_ as a list-of-lists. Try printing out *just* the cities contained in the data:

# In[ ]:


myData = [
    ['id', 'Name', 'Rank', 'Longitude', 'Latitude', 'Population'], 
    ['1', 'Greater London', '1', '-18162.92767', '6711153.709', '9787426'], 
    ['2', 'Greater Manchester', '2', '-251761.802', '7073067.458', '2553379'], 
    ['3', 'West Midlands', '3', '-210635.2396', '6878950.083', '2440986']
]


# In[ ]:


col    = myData[0].index('Name')
print(col)
for i in range(1, len(myData)):
    print(myData[i][col])





# #### 1.1.1 Print a List of Cities
# 
# Print out a list of every city in the data set:

# In[ ]:


col    = myData[0].index('Name')
cities = []

for i in range(1, len(myData)):
    cities.append(myData[i][col])
    
print("The cities in the data set are: " + ", ".join(cities))


# #### 1.1.2 Is Edinburgh in the List?
# 
# Now write code to find out if `Edinburgh` is included in the list of data:

# In[ ]:


found = False
for i in range(1, len(myData)):
    if(myData[i][col]) == 'Edinburgh':
        print("Found Edinburgh in the data set!")
    else:
        print("Didn't find Edinburgh in the data set.")


# In[ ]:


found = False
for i in range(1, len(myData)):
    if myData[i][col] == 'Edinburgh':
        print("Found Edinburgh in the data set!")
        found = True
        break

if found == False:
    print("Didn't find Edinburgh in the data set.")


# ### Task 1.2 The Way That Does Work
# 
# <div class="alert alert-block alert-success"><b>Difficulty level</b>: Low (this time around).</div>
# 
# Compare that code to how it works for a dictionary-of-lists organised by _column_. Now try printing out the cities in the data:

# In[ ]:


myData2 = {
    'id'         : [0, 1, 2, 3, 4, 5],
    'Name'       : ['Greater London', 'Greater Manchester', 'Birmingham','Edinburgh','Inverness','Lerwick'],
    'Rank'       : [1, 2, 3, 4, 5, 6],
    'Longitude'  : [-0.128, -2.245, -1.903, -3.189, -4.223, -1.145],
    'Latitude'   : [51.507, 53.479, 52.480, 55.953, 57.478, 60.155],
    'Population' : [9787426, 2705000, 1141816, 901455, 70000, 6958],
}


# #### 1.2.1 Print a List of Cities
# 
# Print out a list of every city in the data set:

# In[ ]:


# What cities are in the data set?
print(type(myData2))
print(", ".join(myData2['Name']))


# #### 1.1.2 Is Edinburgh in the List?
# 
# Now write code to find out if `Edinburgh` is included in the list of data:

# In[ ]:


if 'Edinburgh' in myData2['Name']:
    print("Found Edinburgh in the data set!")
else:
    print("Didn't find Edinburgh in the data set.")


# See how even basic questions like "Is Edinburgh in our list of data?" are suddenly easy to answer? We no longer need to loop over the entire data set in order to find one data point. In addition, we know that everything in the 'Name' column will be a string, and that everything in the 'Longitude' column is a float, while the 'Population' column contains integers. So that's made life easier already. But let's test this out and see how it works.

# ### Task 1.3 Appending a Column
# 
# To give you a sense of how scaleable this approach to data is let's add a new column where the population is standardised to a z-score. Remember that the format for the z-score is: 
# 
# $$
# z = \frac{x - \bar{x}}{\mu}
# $$

# #### 1.3.1 Calculate Mean & Std Dev
# 
# <div class="alert alert-block alert-success"><b>Difficulty level</b>: Low-ish.</div>
# 
# Let's start by calculating the sample mean and standard deviation (use Google: `Python numpy mean...`):

# In[ ]:


import numpy as np
# Use numpy functions to calculate mean and standard deviation
mean = np.mean(myData2['Population'])
std  = np.std(myData2['Population'])
print(f"City distribution has a mean {mean:,.0f} and standard deviation of {std:,.2f}.")


# `numpy` gives us a way to calculate the mean and standard deviation _quickly_ and without having to reinvent the wheel. The other potentially new thing here is `{std:,.2f}`. This is about [string formatting](https://www.w3schools.com/python/ref_string_format.asp) and the main thing to recognise is that this means 'format this float with commas separating the thousands/millions and 2 digits to the right'. The link I've provided uses the slightly older approach of `<str>.format()` but the formatting approach is the same.

# #### 1.3.2 For Loops Without For Loops
# 
# <div class="alert alert-block alert-warning"><b>Difficulty level</b>: Medium.</div>
# 
# Now we're going to see something called a **List Comprehension**.
# 
# In Python you will see code like this a lot: `[x for x in list]`. This syntax is known as a 'list comprehension' and is basically a `for` loop on one line with the output being assigned to a list. So we can apply an operation (converting to a string, subtracting a value, etc.) to every item in a list without writing out a full for loop.
# 
# Here's a quick example just to show you what's going on:

# In[ ]:


demo = range(0,10) # <- a *range* of numbers between 0 and 9 (stop at 10)
print([x**2 for x in demo]) # square every element of demo


# Now let's apply this to our problem. We calculated the the mean and standard deviation above, so now we want to apply the z-score formula to every element of the Population list... 

# In[ ]:


rs = [(x - mean)/std for x in myData2['Population']] # rs == result set
print([f"{x:.3f}" for x in rs])


# #### 1.3.3 Appending
# 
# <div class="alert alert-block alert-success"><b>Difficulty level</b>: trivial</div>
# 
# And now let's add it to the data set:

# In[ ]:


myData2['Std. Population'] = rs
print(myData2['Std. Population'])
print(myData2)


# And just to show how everything is in a single data structure:

# In[ ]:


for c in myData2['Name']:
    idx = myData2['Name'].index(c)
    print(f"{c} has a population of {myData2['Population'][idx]:,} and standardised score of {myData2['Std. Population'][idx]:.3f}")


# ## Task 2. 'Functionalising'

# Let's start trying to pull what we've learned over the past two weeks together by creating a a set of functions that will help us to:
# 
# 1. Download a file from a URL (checking if it has already _been_ downloaded to save bandwidth).
# 2. Parse it as a CSV file and...
# 3. Convert it to a Dictionary-of-Lists
# 4. Perform some simple calculations using the resulting data.
# 
# To be honest, there's not going to be much about writing our _own_ objects here, but we will be making use of them and, conceptually, an understanding of objects and classes is going to be super-useful for understanding what we're doing in the remainder of the term!

# ### Task 2.1: Downloading from a URL
# 
# Let's focus on the first part *first* because that's the precondition for everything else. If we can get the 'download a file from a URL' working then the rest will gradually fall into place through *iterative* improvments!

# #### 2.1.1 Finding an Existing Answer
# 
# First, let's be sensibly lazy--we've already written code to read a file from the Internet and turn it into a list of lists. So I've copy+pasted that into the code block below since we're going to start from this point; however, just to help you check your own understanding, I've removed a few bits and replacement with `??`. Sorry. 😈

# In[ ]:


from urllib.request import urlopen
import csv

url = "https://raw.githubusercontent.com/jreades/fsds/master/data/src/Wikipedia-Cities-simple.csv"

urlData = [] # Somewhere to store the data

response = urlopen(url) # Get the data using the urlopen function
csvfile  = csv.reader(response.read().decode('utf-8').splitlines()) # Pass it over to the reader

for row in csvfile:
    urlData.append(row)

print("urlData has " + str(len(urlData)) + " rows and " + str(len(urlData[0])) + " columns.")
print(urlData[-1]) # Check it worked!


# You should get `urlData has 11 rows and 4 columns.` and a row that looks like this: `['Bangor', '18808', '53.228', '-4.128']`.

# #### 2.1.2 Getting Organised
# 
# <div class="alert alert-block alert-success"><b>Difficulty level</b>: Low</div>
# 
# Let's take the code above and modify it so that it is:
# 
# 1. A function that takes two arguments: a URL; and a destination filename.
# 2. Implemented as a function that checks if a file exists already before downloading it again.
# 
# You will find that the `os` module helps here because of the `path` function. And you will [need to Google](https://lmgtfy.app/?q=check+if+file+exists+python) how to test if a file exists. I would normally select a StackOverflow link in the results list over anything else because there will normally be an _explanation_ included of why a particular answer is a 'good one'. I also look at which answers got the most votes (not always the same as the one that was the 'accepted answer'). In this particular case, I also found [this answer](https://careerkarma.com/blog/python-check-if-file-exists/) useful.
# 
# I would start by setting my inputs:

# In[ ]:


import os
url = "https://raw.githubusercontent.com/jreades/fsds/master/data/src/Wikipedia-Cities-simple.csv"
out = os.path.join('data','Wikipedia-Cities.csv') # Print `out` if you aren't sure what this has done!
print(out)
os.path.isfile('Wikipedia-Cities.csv')


# #### 2.1.3 Sketching the Function
# 
# <div class="alert alert-block alert-success"><b>Difficulty level</b>: Low</div>
# 
# Then I would sketch out how my function will work using comments. And the simplest thing to start with is checking whether the file has already been downloaded:

# In[ ]:


from urllib.request import urlopen

def get_url(src, dest):
    
    # Check if dest exists -- if it does
    # then we can skip downloading the file,
    # otherwise we have to download it!
    if os.path.isfile(dest):
        print(f"{dest} found!")
    else:
        print(f"{dest} *not* found!")
        
get_url(url, out)


# #### 2.1.4 Fleshing Out the Function 
# 
# <div class="alert alert-block alert-warning"><b>Difficulty level</b>: Medium, if you really explore what's going on in the function rather than just running it and moving on.</div>
# 
# I would then flesh out the code so that it downloads the file if it isn't found and then, either way, returns the *local* file path for our CSV reader to extract:

# In[ ]:


def get_url(src, dest):
    
    # Check if dest does *not* exist -- that
    # would mean we had to download it!
    if os.path.isfile(dest):
        print(f"{dest} found locally!")
    else:
        print(f"{dest} not found, downloading!")
        
        # Get the data using the urlopen function
        response = urlopen(src) 
        filedata = response.read().decode('utf-8')
        
        # Extract the part of the dest(ination) that is *not*
        # the actual filename--have a look at how 
        # os.path.split works using `help(os.path.split)`
        path = list(os.path.split(dest)[:-1])
        
        # Create any missing directories in dest(ination) path
        # -- os.path.join is the reverse of split (as you saw above)
        # but it doesn't work with lists... so I had to google how 
        # to use the 'splat' operator! os.makedirs creates missing 
        # directories in a path automatically.
        if len(path) >= 1 and path[0] != '':
            os.makedirs(os.path.join(*path), exist_ok=True)
        
        with open(dest, 'w') as f:
            f.write(filedata)
            
        print(f"Data written to {dest}!")
    
    return dest
        
# Using the `return contents` line we make it easy to 
# see what our function is up to.
src = get_url(url, out)


# <div class="alert alert-block alert-warning">
#     <b>&#9888; Stop!</b> It really would be a good idea to put in the effort to make sense of how this function works. There is a lot going on here and understanding how this function works will help you to understand how to code. You should notice that we don't try to check if the data file contains any useful data! So if you download or create an empty file while testing, you won't necessarily get an error until you try to turn it into data afterwards!</div>

# ### Task 2.2: Parse the CSV File
# 
# <div class="alert alert-block alert-success"><b>Difficulty level</b>: Low</div>
# 
# Now we turn to the next task: parsing the file if it's a CSV. This implies that it *might* not be so that's something we should also consider!

# In[ ]:


import csv

def read_csv(src):
    
    csvdata = []
    with open(src, 'r') as f:
        csvr = csv.reader(f)
        
        for r in csvr:
            csvdata.append(r)
    
    # Return list of lists
    return csvdata

read_csv(src)
#read_csv('foo.bar') # <- Notice what happens if you try to run this code
#read_csv('Practical-04-Objects-Answers.ipynb') # Or this code!


# You should get:
# 
# ```
# [['City', 'Population', 'Latitude', 'Longitude'],
#  ['Perth', '45770', '56.39583', '-3.43333'],
#  ['Armagh', '14777', '54.3499', '-6.6546'],
#  ['Dundee', '147268', '56.462', '-2.9707'],
#  ['Colchester', '194706', '51.88861', '0.90361'],
#  ['Salisbury', '40302', '51.07', '-1.79'],
#  ['Portsmouth', '205056', '50.80583', '-1.08722'],
#  ['Wakefield', '325837', '53.683', '-1.499'],
#  ['Bradford', '522452', '53.792', '-1.754'],
#  ['Lancaster', '138375', '54.047', '-2.801'],
#  ['Bangor', '18808', '53.228', '-4.128']]
# ```

# ### Task 2.3: Convert the CSV into a DoL
# 
# <div class="alert alert-block alert-warning"><b>Difficulty level</b>: Medium.</div>

# Now we can focus on converting the CSV data to a dictionary-of-lists! We're going to start with the *same* function name but expand what the function *does*. This kind of *iteration* is common in software development.

# In[ ]:


def read_csv(src):
    
    csvdata = {} # An empty dictionary-of-lists
    
    with open(src, 'r') as f:
        csvr = csv.reader(f)
        
        # Read in our column names and
        # initialise the dictionary-of-lists
        csvcols = next(csvr) 
        for c in csvcols:
            csvdata[c] = []
        
        # Notice this code is still the same, 
        # we just used next(csvr) to get the 
        # header row first!
        for r in csvr: 
            # Although you can often assume that the order 
            # of the keys is the same, Python doesn't 
            # guarantee it; this way we will always make
            # the correct assignment.
            for idx, c in enumerate(csvcols):
                csvdata[c].append(r[idx])
    
    # Return dictionary of lists
    return csvdata

read_csv(src)


# You should get something that starts:
# ```
# {'City': ['Perth',
#   'Armagh',
#   'Dundee',
#   'Colchester',
#   'Salisbury',
#   'Portsmouth',
#   'Wakefield',
#   'Bradford',
#   'Lancaster',
#   'Bangor'],
#  'Population': ['45770',
# ```

# ### Task 2.4: Adding Docstring
# 
# <div class="alert alert-block alert-success"><b>Difficulty level</b>: Low</div>
# 
# We've assumed that the first row of our data set is always a _header_ (i.e. list of column names). If it's not then this code is going to have problems. A _robust_ function would allow us to specify column names, skip rows, etc. when we create the data structure, but let's not get caught up in that level of detail. Notice that I've also, for the first time:
# 
# 1. Used the docstring support offered by Python. You'll be able to use `help(...)` and get back the docstring help!
# 2. Provided hints to Python about the expected input and output data types. This can help to ensure consistency and is also critical in testing / continuous integration when working with others on a codebase.

# In[ ]:


def read_csv(src:str) -> dict:
    """
    Converts a CSV file to a dictionary-of-lists (dol),
    using the first row to create column names.
    
    :param src: ??
    :returns: ??
    """
    csvdata = {} # An empty dictionary-of-lists
    
    with open(src, 'r') as f:
        csvr = csv.reader(f)
        
        # Read in our column names and
        # initialise the dictionary-of-lists
        csvcols = next(csvr) 
        for c in csvcols:
            csvdata[c] = []
        
        # Notice this code is still the same, 
        # we just used next(csvr) to get the 
        # header row first!
        for r in csvr: 
            # Although you can often assume that the order 
            # of the keys is the same, Python doesn't 
            # guarantee it; this way we will always make
            # the correct assignment.
            for idx, c in enumerate(csvcols):
                csvdata[c].append(r[idx])
    
    # Return dictionary of lists
    return csvdata

ds = read_csv(src)


# In[ ]:


help(ds)


# In[ ]:


print(ds)


# In[ ]:


print("Columns are: " + ", ".join(ds.keys()))
print(f"First two cities are: {ds['City'][:2]}")
print(f"First two populations are: {ds['Population'][:2]}")
print(f"First two latitudes are: {ds['Latitude'][:2]}")
print(f"First two longitudes are: {ds['Longitude'][:2]}")

print(type(ds['Population'][0][0]))


# The answer should look like:
# ```
# Columns are: City, Population, Latitude, Longitude
# First two cities are: ['Perth', 'Armagh']
# First two populations are: ['45770', '14777']
# First two latitudes are: ['56.39583', '54.3499']
# ```

# ### Task 2.5: Fixing Data Types
# 
# <div class="alert alert-block alert-warning"><b>Difficulty level</b>: Medium.</div>
# 
# If you look closely at the above, you'll see that *everything* is a string, including the latitudes, longitudes, and populations, which are clearly numeric data types. Here's a 'simple' way to specify a `dtype` list to hold the _data type_ for each column. I'm also going to introduce you the `zip` function here as it has many uses with geographic data (especially converting lat/long to points).

# #### 2.5.1 Demonstrating Zip
# 
# <div class="alert alert-block alert-success"><b>Difficulty level</b>: Low</div>

# In[ ]:


cols  = ['City', 'Population', 'Latitude', 'Longitude'] # <- Column name
dtype = [str, int, float, float]                        # <- Column data type

# 'Zips up' these two lists into an iterator! So this will 
# take element 0 from *each* list and pass them to `col` as
# a list-like 'tuple' (meaning there is a col[0] and a col[1]).
for col in zip(cols, dtype):
    colname = col[0]
    coltype = col[1]
    
    # Notice the more advanced formatting here:
    # - `>12` means right-align with up to 12 characters of whitespace; notice the last line!
    # - `coltype.__name__` gives us the name of the data type, rather than a '<class...>' output.
    print(f"Column {colname:>12} should be type: {coltype.__name__}")


# #### 2.5.2 A Function to Convert Data Types
# 
# <div class="alert alert-block alert-success"><b>Difficulty level</b>: Low, as I've provided a function.</div>

# In[ ]:


# Convert the raw data to data of the appropriate
# type: 'column data' (cdata) -> 'column type' (ctype)
def to_type(cdata, ctype):
    # If a string
    if isinstance(cdata, str):
        try:
            if ctype==bool:
                return cdata==True
            else:
                return ctype(cdata)
        except TypeError:
            return cdata
    
    # Not a string (assume list)
    else: 
        fdata = []
        for c in cdata:
            try:
                if ctype==bool:
                    fdata.append( c=='True' )
                else:
                    fdata.append( ctype(c) )
            except:
                fdata.append( c )
        return fdata


# In[ ]:


# Now apply this! We'll copy the data to 
# new data structure only so that we know
# we're not overwriting `ds` until we're sure
# that the code works.
ds2 = {}
for col in zip(cols, dtype):
    colname = col[0]
    coltype = col[1]
    ds2[ colname ] = to_type( ds[colname], coltype ) #still don't understand


# Compare the output here to the output from `ds` up above:

# In[ ]:


print("Columns are: " + ", ".join(ds2.keys()))
print(f"First two cities are: {ds2['City'][:2]}")
print(f"First two populations are: {ds2['Population'][:2]}")
print(f"First two latitudes are: {ds2['Latitude'][:2]}")


# You should get the followg:
# ```
# Columns are: City, Population, Latitude, Longitude
# First two cities are: ['Perth', 'Armagh']
# First two populations are: [45770, 14777]
# First two latitudes are: [56.39583, 54.3499]
# ```

# ### Task 2.6: Checking Basic Functionality
# 
# <div class="alert alert-block alert-warning"><b>Difficulty level</b>: Medium</div>
# 
# Now that we've got our data structure all set up correctly (appropriate names, data types, etc.) let's see if it works by testing out some of our previous operations:

# In[ ]:


import numpy as np # We'll need this to apply functions to lists easily

print(f"Average population is {np.mean(ds2['Population']):,.2f}")
print(f"Westernmost city is {ds2['City'][np.where(ds2['Longitude']==np.min(ds2['Longitude']))[0][0]]}")
print(f"Northernmost city is {ds2['City'][np.where(ds2['Latitude']==np.max(ds2['Latitude']))[0][0]]}")
print(f"Southernmost city is {ds2['City'][np.where(ds2['Latitude']==np.min(ds2['Latitude']))[0][0]]}")


# You should get the following:
# 
# ```
# Average population is 165,335.10
# Westernmost city is Armagh
# Northernmost city is Dundee
# Southernmost city is Portsmouth
# ```
# 
# There are a few things to understand here:
# 
# 1. Where we want to find something else in the data *based on that value* then things get a little more complex: we use `np.min` to find the smallest value in the data, but we don't know *where* in the list that value actually *was* so we use `np.where` to find out which indexes match the minimum value. In this data set it's easy because there's one, and only one value that matches. But you'd need to do some clever thinking about how to handle ties.
# 2. `np.where` returns a complex data structure (list-of-lists, essentially) so we need to pull the value we need out of that data in order to actually find the list index we need and look up the `City` name associated with, for example, the minium value in the data. That bit (`[0][0]`) is a bit clunky, but right now we're not too worried about it.
# 
# **Notice** that we do *all* of this without using a `for` loop or variables to keep track of what we've found... You *could* also use a `for` loop to answer each of these questions (see the example below), but hopefully you see what the way we've used above is more *elegant* (it's also faster):

# In[ ]:


min_long = 180
min_idx  = -1

for l in ds2['Longitude']:
    if l < min_long: min_long = l
print(f"Minimum longitude is {min_long}")

for idx, l2 in enumerate(ds2['Longitude']):
    if l2==min_long:
        min_idx = idx
        break

print(f"Westernmost city is {ds2['City'][min_idx]}")


# ## Task 3. Was it Worth It?
# 
# <div class="alert alert-block alert-success"><b>Difficulty level</b>: Low</div>
# 
# At this point it's worth asking: was all this *worth* it? Let's see! 
# 
# The best way to test is to use a *different* data set and see if we've solved the 'hard-coding' problem.

# In[ ]:


url = "https://raw.githubusercontent.com/jreades/fsds/master/data/src/Wikipedia-Cities.csv"
out = os.path.join('data','Wikipedia-Cities-full.csv')

cols  = ['City', 'Population', 'Latitude', 'Longitude']
dtype = [str, int, float, float]

untyped_dol = read_csv(get_url(url, out))

typed_dol = {}
for col in zip(cols, dtype):
    colname = col[0]
    coltype = col[1]
    typed_dol[ colname ] = to_type(untyped_dol[colname], coltype)


# In[ ]:


print(f"Average population is {np.mean(typed_dol['Population']):,.2f}")
print(f"Westernmost city is {typed_dol['City'][np.where(typed_dol['Longitude']==np.min(typed_dol['Longitude']))[0][0]]}")
print(f"Northernmost city is {typed_dol['City'][np.where(typed_dol['Latitude']==np.max(typed_dol['Latitude']))[0][0]]}")
print(f"Southernmost city is {typed_dol['City'][np.where(typed_dol['Latitude']==np.min(typed_dol['Latitude']))[0][0]]}")

print(typed_dol)


# You should get:
# 
# ```
# Average population is 202,283.36
# Westernmost city is Derry
# Northernmost city is Inverness, Inerness, Inbhir Nis
# Southernmost city is Truro
# ```
# 
# So we used all the same code as for the subset of the data but changed *nothing*. And this is even though the column order changed (print out the first row of each file if you don't believe me) *and* the number of columns changed *and* our city column now contains commas! So what this has given us is a much more flexible way not only to *access* the data, but also to *work* with it!

# ## Task 4. More Functions!
# 
# <div class="alert alert-block alert-warning"><b>Difficulty level</b>: Medium</div>
# 
# Here is the skeleton of a function to replace the `np.where(column==np.[min|max|...](column))[0][0]` code. There are a few ways to do this: 
# 
# 1. You could use if/else/elif and do different things based on testing against the specified string
# 2. You could try to find a function in `numpy` that matches the specified string
# 3. You could try to `eval` the code, but I really wouldn't recommend this for security reasons
# 
# I have gone with a combination of 1 and 2, but you will need to really read the code to understand how it works. I've left the docstring for you to complete. This isn't the best function since it makes some assumptions about the types of data that it might be passed to the function: this is where *Object-Oriented Programming* could come to the rescue! If we had different column *types* (e.g. String, Float, Int) then we could have different *versions* of `find_val` that performed the same *function* (find a value) but did this completely differently depending on the data. This is what *methods* do!

# In[ ]:


import numpy as np

def find_val(col:list, val:str):
    """
    ??
    """
    if val in dir(np) and callable(getattr(np, val)):
        func = getattr(np, val) # <--- What does this do???
        if val in ['min','max']:
            return np.where(col==func(col))[0][0]
        else:
            return func(col)
    else:
        return np.nan
    
print(find_val(typed_dol['Latitude'], 'min'))
print(find_val(typed_dol['Latitude'], 'median')) #still don't understand how it can calculate median
print(find_val(typed_dol['Latitude'], 'max'))


# In[ ]:


print(f"Average population is {find_val(typed_dol['Population'],'mean'):,.2f}")
print(f"Westernmost city is {typed_dol['City'][find_val(typed_dol['Longitude'],'min')]}")
print(f"Northernmost city is {typed_dol['City'][find_val(typed_dol['Latitude'],'max')]}")
print(f"Southernmost city is {typed_dol['City'][find_val(typed_dol['Latitude'],'min')]}")


# So we have streaminlined the code still further and implemented a fairly generic 'helper' function that uses `numpy` to perform calculations on a column of data (assuming it's numeric). We could, of course, extend this further, to handle strings and other data types, but we're going to see a *better* way to do all of this *next* week.

# ## Task 5. Creating a Package from Functions
# 
# <div class="alert alert-block alert-danger"><b>Difficulty level</b>: Hard.</div>
# 
# Below is code to create a package called `dtools` (i.e. data tools) by converting the notebook into a Python script file called `__init__.py` that sits in the `dtools` directory. This is the first step to creating a package from code that is *already* working in a Notebook.

# ### Task 5.1 Create a Directory
# 
# When creating your own package, everything goes into a directory whose name is the name of the package. In other words, if you wanted to create a package called `my_stuff` then you'd need to *first* create a directory called `my_staff` in the *current working directory* (i.e. wherever you are keeping your Notbooks).
# 
# We can create the directory using `mkdir` (the `!` means 'run this [Linux] command'):

# In[ ]:


get_ipython().system("mkdir -p 'dtools'")


# ### Task 5.2 Create \_\_init\_\_.py
# 
# More complex packages will have lots of stuff going on inside their 'root' directory, but we're keeping it simple and only need to create and fill in *one* file inside the `dtools` directory: `__init__.py`. This is a convention.
# 
# We can create this file two ways: 
# 
# 1. By creating an empty file with that name in `dtools` (e.g. `!touch dtools/__init__.py` would work!)
# 2. By converting *this* entire notebook to a Python script and then removing all the stuff that *is not* a function that we need to keep.
# 
# The 'hybrid' way, which I'm going to suggest you use so you get some more experience, would be to convert this notebook to a Python script file, open it, and then copy the functions out into `__init__.py`. 

# In[ ]:


get_ipython().system('touch dtools/__init__.py')
# Comment out so we don't automatically re-run this code every time
get_ipython().system('jupyter nbconvert --ClearOutputPreprocessor.enabled=True      --to python --output=dtools/notebook.py      Practical-04-Objects-Answers.ipynb')


# ### Task 5.3 Extract Code to Init
# 
# You now need to open `notebook.py` and find+copy the following functions into `__init__.py`:
# 
# 1. `get_url`
# 2. `read_csv` 
# 3. `to_type` 
# 4. `find_val`
# 
# And don't forget to find all the `import` statements (including `from x import y`) and copy those as well!
# 
# You should then be able to run the code below and can always compare it to my version [on GitHub](https://github.com/jreades/fsds/blob/master/practicals/dtools/__init__.py).

# ### Task 5.6 Test
# 
# The next two lines of code allow you to repeatedly edit an imported package without having to restart the entire Python notebook. So whenever Jupyter sees a change to `dtools/__init__.py` it will reload the package and update the code without you having to do anything.

# In[ ]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# #### 5.6.1 Import
# 
# And now we should be able to import the package and start using the functions that we defined...

# In[ ]:


import dtools
help(dtools.read_csv)


# #### 5.6.2 Use Read_CSV

# In[ ]:


url = 'https://github.com/jreades/fsds/raw/master/data/2019-sample-crime.csv'
out = os.path.join('data','crime-sample.csv')

ds = ??.read_csv(??.get_url(url, out))


# In[ ]:


print(f"ds has {len(ds.keys())} columns, these are: " + ", ".join(ds.keys()))
print(f"There are {len(ds['ID'])} rows of data")


# #### 5.6.3 Use To_Type

# In[ ]:


cols  = ['Latitude', 'Longitude'] 
dtype = [float, float]

typed_ds = {}
for col in zip(cols, dtype): # <- This only copies these two columns to typed_ds
    colname = col[0]
    coltype = col[1]
    typed_ds[ colname ] = dtools.to_type(ds[colname], coltype)


# #### 5.6.4 Use Find_Val

# In[ ]:


idx = find_val(typed_ds['Latitude'], 'min')


# In[ ]:


print(ds['Case Number'][idx])
print(ds['Description'][idx])


# ## Task 6. Brain Teaser
# 
# <div class="alert alert-block alert-danger"><b>Difficulty level</b>: &#129327;.</div>

# And now for something completely different!
# 
# We want to create a set of 'ideal shapes' with methods allowing us to derive various properties of that shape:
# 
# - Diameter: which we'll define as the longest line that can be drawn across the inside of the shape.
# - Volume: the total volume of the shape.
# - Surface Area: the total outside area of the shape.
# 
# We will create all of these shape classes in the notebook so that we know they work and then will move them to an external package file so that they can be imported and re-used easily in other notebooks.
# 
# We're also going to make use of a few features of Python:
# 
# - You can access the class name of an instance using: `self.__class__.__name__`. And here's one key point: `self` refers to the instance, not to the class... we'll see why this matters.
# - You can raise your own exceptions easily if you don't want to implement a particular method yet.
# - You can have an 'abstract' base class that does nothing except provide a template for the 'real' classes so that they can be used interchangeably.
# 

# ### Task 6.1 Abstract Base Class
# 
# This class appears to do very little, but there are two things to notice:
# 
# 1. It provides a constructor (`__init__`) that sets the `shape_type` to the name of the class automatically (so a `square` object has `shape_type='Square'`) and it stores the critical dimension of the shape in `self.dim`.
# 2. It provides methods (which only raise exceptions) that will allow one shape to be used in the place of any other shape that inherits from `shape`.

# In[ ]:


from math import pi

# Base class shape
class shape(object): # Inherit from base class 
    def __init__(self, dimension:float=None):
        self.shape_type = self.__class__.__name__.capitalize()
        self.dim = dimension
        return
    
    def diameter(self):
        raise Exception("Unimplmented method error.")
    
    def volume(self):
        raise Exception("Unimplmented method error.")
    
    def surface(self):
        raise Exception("Unimplmented method error.")
        
    def type(self):
        return(self.shape_type)


# ### Task 6.2 Cube
# 
# Implements a cube:
# 
# 1. The diameter of the cube is given by the Pythagorean formula for the length of the hypotenuse in 3D between opposing corners: $\sqrt{d^{2} + d^{2} + d^{2}}$ which we can reduce to $\sqrt{3 d^{2}}$.
# 2. A cube's volume is given by $d^{3}$.
# 3. A cube's surface area will be the sum of its six faces: $6d^{2}$.

# In[ ]:


# Cube class
class cube(shape): # Inherit from shape 
    def __init__(self, dim:float):
        super().__init__(dim)
        return
    
    def diameter(self):
        return (3 * self.??**2)**(1/2)
    
    def volume(self):
        return self.dim**3
    
    def surface(self):
        return ??*(self.dim**2)


# ### Task 6.3 Sphere
# 
# Implements a sphere:
# 
# 1. The diameter is twice the critical dimension (radius): $2d$. 
# 2. The volume is $\frac{4}{3} \pi r^{3}$.
# 3. The surface area will be $4 \pi r^{2}$.
# 
# If we were writing something more general, we'd probably have spheres as a special case of an ellipsoid!

# In[ ]:


# Sphere code here!


# ### Task 6.4 Regular Pyramid
# 
# We're taking this to be a regular pyramid where all sides are equal: 
# 
# 1. The diameter is a line drawn across the base between opposing corners of the base so it's just $\sqrt{d^{2} + d^{2}}$.
# 2. The volume is given by $V = b * h / 3$ (where $b$ is the area of the base, which in this case becomes $d^{2} * h/3$).
# 3. The surface area will be the base + 4 equilateral triangles: $d^{2} + 4 (d^{2}\sqrt{3}/4)$ which we can reduce to $d^{2} + d^{2}\sqrt{3}$
# 
# But this requires a _height_ method that is specific to pyramids:
# 
# 4. The height is taken from the centre of the pyramid (which will be half the length of the hypotenuse for two edges): $l = \sqrt{d{^2} + d^{2}}$ and the long side ($d$ again) which gives us $\sqrt{l/2 + d^{2}}$.
# 
# Note that this has a class variable called `has_mummies` since Egyptian regular pyramids are plagued by them! 

# In[ ]:


# Pyramid class
class pyramid(shape): # Inherit from shape
    
    has_mummies = True # This is for *all* regular pyramids
    
    def __init__(self, dim:float):
        super().__init__(dim)
        self.shape_type = 'Regular Pyramid'
        return
    
    def diameter(self):
        return (self.dim**?? + self.??**2)**(1/2)
    
    def height(self):
        return (self.diameter()/?? + self.dim**2)**(1/2)
    
    def volume(self):
        return self.dim**2 * self.??() / 3
    
    def surface(self):
        return self.dim**2 + self.dim**2 * 3**(1/2)


# ### Task 6.5 Triangular Pyramid
# 
# We want triangular pyramid to inherit from regular pyramid, and all sides are equal so it's an _equilateral_ triangular pyramid. However, this is kind of a judgement call since there's very little shared between the two types of pyramid and it's arguable whether this one is actually simpler and should therefore be the parent class...
# 
# Anyway, the calculations are:
# 
# 1. The diameter (longest line through the shape) will just be the edge: $d$.
# 2. The volume $V = b * h / 3$ where $b$ is the area of an equilateral triangle.
# 3. The surface area will be $4b$ where $b$ is the area of an equilateral triangle.
# 
# So we now need two new formulas:
# 
# 5. The height of the pyramid using ([Pythagoras again](https://www.youtube.com/watch?v=ivF3ndmkMsE)): $h = \sqrt{6}d/3$.
# 6. The area of an equilateral triangle: $\frac{\sqrt{3}}{4} d^{2}$
# 
# Triangular pyramids do *not* have a problem with mummies.

# In[ ]:


# Triangular pyramid code here (extends regular pyramid)!


# ### Task 6.6 Testing Your Classes
# 
# If you've implemented everything correctly then the following code should run.

# In[ ]:


# How would you test these changes?
s = sphere(10)
print(s.type())
print(f"\tVolume is: {s.volume():5.2f}")
print(f"\tDiameter is: {s.diameter():5.2f}")
print(f"\tSurface Area is: {s.surface():5.2f}")
print("")

c = cube(10)
print(c.type())
print(f"\tVolume is: {c.volume():5.2f}")
print(f"\tDiameter is: {c.diameter():5.2f}")
print(f"\tSurface Area is: {c.surface():5.2f}")
print("")

p = pyramid(10)
print(p.type())
print(f"\tVolume is: {p.volume():5.2f}")
print(f"\tDiameter is: {p.diameter():5.2f}")
print(f"\tSurface Area is: {p.surface():5.2f}")
print(f"\tHeight is: {p.height():5.2f}")
if p.has_mummies is True:
    print("\tMummies? Aaaaaaaaagh!")
else:
    print("\tPhew, no mummies!")
print("")

p2 = t_pyramid(10)
print(p2.type())
print(f"\tVolume is: {p2.volume():5.2f}")
print(f"\tDiameter is: {p2.diameter():5.2f}")
print(f"\tSurface Area is: {p2.surface():5.2f}")
print(f"\tHeight is: {p2.height():5.2f}")
if p2.has_mummies is True:
    print("\tMummies? Aaaaaaaaagh!")
else:
    print("\tPhew, no mummies!")
print("")

# Useful demonstration of how to find out if a method or attribute is
# associated with a particular object
if hasattr(p2,'base_area'):
    print(f"Shape of type '{p2.type()}' has attribute or method 'base_area'")
else:
    print(f"Shape of type '{p2.type()}' does *not* have attribute or method 'base_area'")
print("")


# I get the following output:
# 
# ```
# Sphere
# 	Volume is: 4188.79
# 	Diameter is: 20.00
# 	Surface Area is: 1256.64
# 
# Cube
# 	Volume is: 1000.00
# 	Diameter is: 17.32
# 	Surface Area is: 600.00
# 
# Regular Pyramid
# 	Volume is: 344.92
# 	Diameter is: 14.14
# 	Surface Area is: 273.21
# 	Height is: 10.35
# 	Mummies? Aaaaaaaaagh!
# 
# Triangular Pyramid
# 	Volume is: 117.85
# 	Diameter is: 10.00
# 	Surface Area is: 173.21
# 	Height is:  8.16
# 	Phew, no mummies!
# 
# Shape of type 'Triangular Pyramid' does *not* have attribute or method 'base_area'
# ```

# ### Task 6.7 Packaging It Up
# 
# Wait, you're *still* working on this practical and haven't thrown up your hands in disgust yet? OK, in that case you can have *one* more thing to do: turn the whole shapes class hierarchy into a package that can be loaded via an `import` statement. 

# #### 6.7.1 Cell Magic
# 
# This code allows Jupyter to reload external libraries if they are edited after you import them. When you are working on your own packages this is rather useful since you tend to make a *lot* of mistakes when packaging code up this way and it's handy not to have to restart the entire notebook every time you fix a typo or change a function.

# In[ ]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# #### 6.7.2 Import Shapes
# 
# You can call your package whatever you like, but then it *has* to match what you `import` below. So remember that with `dtools` we had `dtools/__init__.py`? You'll need to do the same here so that you can import the package.

# In[ ]:





# #### 6.7.3 Adding Documentation
# 
# In an ideal world, this would also be the time to properly document your classes and methods. Here as some examples that you could add to the `__init__.py` package file.
# 
# Underneath the line `class shape(object):`, add:
# ```
#     """Abstract base class for all ideal shape classes.
# 
#     Keyword arguments:
#     dimension -- the principle dimension of the shape (default None)
#     """
# ```
# 
# Underneath the line `def type(self):`, add:
# ```
#         """
#         Returns the formatted name of the shape type. 
#         
#         This is set automatically, but can be overwritten by setting the attribute shape_type.
#         
#         :returns: the name of the class, so shapes.cube is a `Cube` shape type
#         :rtype: str
#         """
# ```

# In[ ]:


import shapes # <-- Change this if you didn't call your package `shapes`!
help(shapes.shape)
help(shapes.shape.type)

