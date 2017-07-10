# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10, 2017

@author: Simon Filhol

Collection of functions to import snowpit data stored in the xlsx file format

******************
   Xlsx file must be formated following the package example
******************

"""
from __future__ import division
import xlrd
import pit_class as pc
import pandas as pd

def find_row_with_values(sh, val):
    '''
    Function to find cell location of particular values indicated by a field
    :param sh: excel sheet (open with xlrd library)
    :param val: values of the fields (the first 4 character for each field) in a list format
    :return: return a dictionnary of the row where the value wanted is
    '''

    rows = []
    values = []
    for row_index in xrange(sh.nrows):
        for value in val:
            if value == (str(sh.row(row_index)[0].value)[:4]):
                rows.append(row_index)
                values.append(value)
    return dict(zip(values, rows))

def get_cell_val_str(sh, cRrow, cCol):
    '''
    Function to grab cell value as str
    :param sh:
    :param cRrow:
    :param cCol:
    :return:
    '''
    value = sh.cell(cRrow, cCol)
    # if value.value.__len__() == 0:
    # value.value = np.nan
    return str(value.value)

def open_xlsx(path_xlsx, sheet=None):

    if path_xlsx[-4:] != 'xlsx':
            print 'Input file is not of .xlsx format'
            return

    wb = xlrd.open_workbook(path_xlsx)
    print wb.sheet_names()
    if sheet is None:
        sheet = wb.sheet_names()[0]
    sh = wb.sheet_by_name(sheet)

    return sh

def get_metadata(sheet):

    Metadata = pc.metadata()
    # Load metadata:
    fields = ['East', 'Nort', 'Elev', 'Date', 'Obse', 'Loca', 'Air ', 'Weat', 'Comm', 'Snow', 'Time', 'Gene',
              'Stra']
    values = find_row_with_values(sheet, fields)

    Metadata.date = get_cell_val_str(sheet, values.get('Date'), 1)
    Metadata.time = get_cell_val_str(sheet, values.get('Time'), 1)
    Metadata.location_description = get_cell_val_str(sheet, values.get('Gene'), 1)
    Metadata.east = get_cell_val_str(sheet, values.get('East'), 1)
    Metadata.east_unit = get_cell_val_str(sheet, values.get('East'), 2)
    Metadata.north = get_cell_val_str(sheet, values.get('Nort'), 1)
    Metadata.north_unit = get_cell_val_str(sheet, values.get('Nort'), 2)
    Metadata.elevation = get_cell_val_str(sheet, values.get('Elev'), 1)
    Metadata.elevation_unit = get_cell_val_str(sheet, values.get('Elev'), 2)
    Metadata.observer = get_cell_val_str(sheet, values.get('Obse'), 1)
    Metadata.air_temperature = get_cell_val_str(sheet, values.get('Air '), 1)
    Metadata.air_temperature_unit = get_cell_val_str(sheet, values.get('Air '), 2)
    Metadata.sky_conditions = get_cell_val_str(sheet, values.get('Weat'), 1)
    Metadata.comments = get_cell_val_str(sheet, values.get('Comm'), 1)

    # Will need to add other fields (wind speed, precipitation, srsName, to be conform to CAAML terminology

    return Metadata

def get_table(path_xlsx, sheet):
    table = pd.read_excel(path_xlsx, sheet=sheet, skiprows=int(values.get('Stra')) + 1, engine='xlrd')
    return table


def get_layers(sheet):

def get_temperature(sheet):
    TProfile = pc.temperature_profile()

    TProfile.depth = []
    TProfile.depth_unit = None
    TProfile.temp = []
    TProfile.temp_unit = None

def get_density(sheet):



def load_xlsx(self, path=None, sheet=None):
    '''
    Fucntion to load pit directly from a sheet of a xlsx file
    :param path: path to the file
    :param sheet: indicate the name of the sheet to load
    :return:
    '''

    def find_row_with_values(sh, val):
        '''
        Function to find cell location of particular values indicated by a field
        :param sh: excel sheet (open with xlrd library)
        :param val: values of the fields (the first 4 character for each field) in a list format
        :return: return a dictionnary of the row where the value wanted is
        '''

        rows = []
        values = []
        for row_index in xrange(sh.nrows):
            for value in val:
                if value == (str(sh.row(row_index)[0].value)[:4]):
                    rows.append(row_index)
                    values.append(value)
        return dict(zip(values, rows))

    def get_cell_val_str(sh, cRrow, cCol):
        '''
        Function to grab cell value as str
        :param sh:
        :param cRrow:
        :param cCol:
        :return:
        '''
        value = sh.cell(cRrow, cCol)
        # if value.value.__len__() == 0:
        # value.value = np.nan
        return str(value.value)

    if path is None:
        path = self.filename

        if path[-4:] != 'xlsx':
            print 'Input file is not of .xlsx format'
            return

    wb = xlrd.open_workbook(path)
    if sheet is None:
        sheet = wb.sheet_names()[0]
    sh = wb.sheet_by_name(sheet)

    # Load metadata:
    fields = ['East', 'Nort', 'Elev', 'Date', 'Obse', 'Loca', 'Air ', 'Weat', 'Comm', 'Snow', 'Time', 'Gene',
              'Stra']
    values = find_row_with_values(sh, fields)
    self.date = get_cell_val_str(sh, values.get('Date'), 1)
    self.Time = get_cell_val_str(sh, values.get('Time'), 1)
    self.General_loc = get_cell_val_str(sh, values.get('Gene'), 1)
    self.East = get_cell_val_str(sh, values.get('East'), 1)
    self.East_unit = get_cell_val_str(sh, values.get('East'), 2)
    self.North = get_cell_val_str(sh, values.get('Nort'), 1)
    self.North_unit = get_cell_val_str(sh, values.get('Nort'), 2)
    self.Elevation = get_cell_val_str(sh, values.get('Elev'), 1)
    self.Elevation_unit = get_cell_val_str(sh, values.get('Elev'), 2)
    self.Observer = get_cell_val_str(sh, values.get('Obse'), 1)
    self.AirTemp = get_cell_val_str(sh, values.get('Air '), 1)
    self.weather_conditions = get_cell_val_str(sh, values.get('Weat'), 1)
    self.comments = get_cell_val_str(sh, values.get('Comm'), 1)

    # Load data:
    self.profile_raw_table = pd.read_excel(path, sheet=sh, skiprows=int(values.get('Stra')) + 1, engine='xlrd')
    self.load_profile_from_raw_table()


def sheet_names_xlsx(self, path=None):
    '''
    Functiont to print and return the list of sheet included in an excel file
    :param path:
    :return:
    '''
    if path is None:
        path = self.filename
    wb = xlrd.open_workbook(path)
    print wb.sheet_names()
    return wb.sheet_names()
