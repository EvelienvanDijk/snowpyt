# Snowpyt: an open-source library to visualize snowpits in Python
Simon Filhol, November 2016, copyright under the MIT license terms, see the License.txt file

LAST MODIFIED: September 2017 (or see date on github file history)

Feel free to contribute to the project!!!! Many new features can be added...

## To do:

### High Priority

- write function to save and load pit to and from pickle format (currently not working)
- reorganize package example, standard excel and csv snowpit file
- make ground appear to comfirm the user that the pit reached ground. add note about ground type.

### Low priority 
- specify the figure size and adjust font size in respect
- render the medatadata text better
- put option to adjust figure size to desired size and dpi
- add option to save pits in Pickle format or CSV
- add option to save figure in matplotlib format



## Objective
The objective of this library is to provide visualization tool for snowpit data. 
Started for the need of the Svalbard Snow Research group, this package should evolve
 to include more snowpit type and visualization scheme. 

The snow grain classification follows the guidelines provided by the UNESCO 
[International Classification for Seasonal Snow on the Ground](http://unesdoc.unesco.org/images/0018/001864/186462e.pdf) 
(Fierz et al., 2009)

Fierz, C., Amstrong, R.L., Durand, Y., Etchevers, P., Greene, E., McClung, D.M., Nishimura, K., Satyawali, P.K. and Sokratov, S.A. 2009.The International Classification for Seasonal Snow on the Ground. IHP-VII Technical Documents in 
Hydrology N°83, IACS Contribution N°1, UNESCO-IHP, Paris. 

## Installation

### Last stable version from the Pypi repository

Simply run the following in your terminal:
```bash
pip install snowpyt
```
### Last development version for contributing to the project:

Clone the github repository to a local directory using the following command in your terminal

```bash
git clone https://github.com/ArcticSnow/snowpyt.git
```
or by downloading the package

The branch 'master' consists of the latest stable version. Other develepment versions are included in other git branches.

The package contains all the functions to plot the snowpit if library requirements are met. It also contains data samples to test the library.

### requirements

Python 2.7.9 with the following libraries:
- [numpy](http://www.numpy.org/)
- [matplotlib](http://matplotlib.org/)
- [pandas](http://pandas.pydata.org/)
- xlrd

## Use

1. Snowpit must be formated following the template file "Standard_pit.xlsx"

2. Save the excel or libreoffice file in .xslx format (default Excel format).

3. Load the snowpit into snowpyt

   ```python
   from snowpyt import pit_class as pc

   path_to_file = 'snowpyt/data_example/20170209_Finse_snowpit.xlsx'

   mypit = pc.Snowpit()
   mypit.filename = path_to_file
   mypit.import_xlsx()

   mypit.plot(metadata=True)
   mypit.plot(plots_order=['density', 'temperature', 'stratigraphy','crystal size'], metadata=True)

   mypit.metadata.__dict__
   ```

4. It is also possible to load data from an .xml file formatted according to  [CAAML format](http://caaml.org/)

   ```python
   from snowpyt import pit_class as pc

   path_to_file = 'path to xml file in CAAML format'

   mypit = pc.Snowpit()
   mypit.filename = path_to_file
   mypit.import_xml()

   mypit.plot(metadata=True)
   mypit.plot(plots_order=['density', 'temperature', 'stratigraphy','crystal size'], metadata=True)

   ```

   ​

## Want to contribute?
Once you have cloned the project to your home directory, create a git branch and here you go. When your edits are stable, merge with the master branch. See this neat tutorial about git branching and merging, [here](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)

### List of Contributor
- Simon Filhol
- Guillaume Sutter
- [add your name]

## Example
![Example snowpit](snowpyt/Standard_pit.png)







