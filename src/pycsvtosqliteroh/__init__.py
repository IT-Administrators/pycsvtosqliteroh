"""
Pycsvtosqliteroh

A cross plattform module to convert csv files to sqlite.

Usage:
    from pycsvtosqliteroh import CsvToSqlite
    
    # Create csv object
    
    csvobj = CsvToSqlite("Filename", "DatabaseName")
    csvobj.create_table_from_csv()

Returns:
    None

Author: IT-Administrators
License: MIT

"""

# Import necessary modules
import csv
import sqlite3
from pathlib import Path

class CsvToSqlite:
    """Class for processing csv files."""
    
    _defaultdelimiter = ",",";"

    # Creating constructor.  
    def __init__(self, filename: str, database: str):
        """Creates the csvtosqlite object."""
        self.filename = filename
        self.database = database

    # Get filename without extension to use as table name.   
    def _get_filename(self):
        """Get filename of the current file without extension."""
        file = Path(self.filename).stem
        return file

    # Get the delimiter of the current file.
    # The sniffer class is used to deduce the delimiter.
    # https://docs.python.org/3/library/csv.html#csv.Sniffer
    def _get_delimiter(self):
        """Get the delimiter used in the file."""
        sniffer = csv.Sniffer()
        with open(self.filename) as csvfile:
            delimiter = sniffer.sniff(csvfile.readline()).delimiter
        return delimiter

    # Gets the header of the csv file which will be the column names of the sqlite table.
    def _get_header(self):
        """Get the header of the csv file."""
        with open(self.filename) as csvfile:
            reader = csv.DictReader(csvfile)
            return reader.fieldnames
    
    # Count headers in csv.
    def _get_header_count(self):
        """Count headers."""
        return len(self._get_header())
        
    # Create table from csv.
    def create_table_from_csv(self):
        """Create the table from the specified file if not exists and insert values."""
        # Check delimiter of file. If it is not inside _defaultdelimiter list raise Exception.
        if self._get_delimiter() not in self._defaultdelimiter:
            raise Exception('Wrong delimiter: ' + self._get_delimiter())
        
        # Create database connection and dbcursor and remove object if not used anymore.
        with _Database(self.database) as db:
            # Open file.
            with open(self.filename,'r') as f:
                # Create reader object using delimiter of the current file.
                reader = csv.reader(f, delimiter=self._get_delimiter())
                # Get first line of file by using internal next function. Only works on iterators.
                columns = next(reader)
                # Remove all blanks in the header names.
                columns = [h.strip() for h in columns]
                # Create sql query for table creation.
                sql = 'CREATE TABLE IF NOT EXISTS ' + self._get_filename() + '(%s)'%','.join(['%s'%column for column in columns])
                db.cursor.execute(sql)
                
                # Create insert query.
                query = 'INSERT INTO ' + self._get_filename() + '({0}) values({1})'
                query = query.format(','.join(columns),','.join('?' * len(columns)))
                for row in reader:
                    # Execute the insert statement.
                    db.cursor.execute(query,row)
            
            # INSERT statements explicitly needs a commit. 
            db.connection.commit()
            # Connection doesn't need to be closed because of the with statement.

class _Database:
    """Contextmanager for handling databaseconnections."""
    def __init__(self, path: str):
        self.path = path

    def __enter__(self):
        """Enter connection and return cursor and connection object."""
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close connection."""
        if exc_type is not None:
            print(f'an error occured: {exc_val}')
        self.connection.close()

# Functions/Classes that are imported by calling from <modulename> import *
# Specifying only the class, makes all member functions available.
# Specifying Class.Memberfunction makes also all functions available. 
__all__ = ["CsvToSqlite"]