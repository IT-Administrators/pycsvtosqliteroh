![PyPI - Version](https://img.shields.io/pypi/v/pycsvtosqliteroh)
![PyPI - License](https://img.shields.io/pypi/l/pycsvtosqliteroh)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pycsvtosqliteroh)
[![Publish PyPi](https://github.com/IT-Administrators/pycsvtosqliteroh/actions/workflows/release.yml/badge.svg?branch=main)](https://github.com/IT-Administrators/pycsvtosqliteroh/actions/workflows/release.yml)
[![CI](https://github.com/IT-Administrators/pycsvtosqliteroh/actions/workflows/ci.yaml/badge.svg)](https://github.com/IT-Administrators/pycsvtosqliteroh/actions/workflows/ci.yaml)

# pycsvtosqliteroh

_The pycsvtosqliteroh module is a module to convert csv to sqlite and back._

## Table of contents

1. [Introduction](#introduction)
2. [Getting started](#getting-started)
    1. [Prerequisites](#prerequisites)
    2. [Installation](#installation)
3. [How to use](#how-to-use)
    1. [How to import](#how-to-import)
    2. [Using the module](#using-the-module)
    3. [Using the cli](#using-the-cli)
4. [Releasing](#releasing)
5. [License](/LICENSE)

## Introduction

I've written this module to bulk convert csv files into sqlite tables. The database is used as a test database in another project.

The supported delimiters for the .csv file are "," and ";". 

All testfiles in the [testfiles](/tests/testfiles/) folder, are created via powershell, using the ```Export-Csv``` cmdlet with different delimiters.

You can now convert csv to sqlite as well as sqlite to csv. 
When exporting a sqlite table to .csv
the delimiter is "," by default.

## Getting started

### Prerequisites

- Python installed
- Operatingsystem: Linux or Windows, not tested on mac
- IDE like VS Code, if you want to contribute or change the code

### Installation

There are two ways to install this module depending on the way you work and the preinstalled modules:

1. ```pip install pycsvtosqliteroh```
2. ```python -m pip install pycsvtosqliteroh```

## How to use

### How to Import

You can import the module in two ways:

```python
import pycsvtosqliteroh
```

- This will import all functions. Even the ones that are not supposed to be used (helper functions).

```python
from pycsvtosqliteroh import *
```

- This will import only the significant functions, meant for using. 

### Using the module

Depending on the way you imported the module, the following examples look a bit different.

Example 1: Converting csv to sqlite.

```python
# Import module.
from pycsvtosqliteroh import *
# Create object and than convert to sqlite table.
csvobj = CsvToSqlite(file, database)
csvobj.create_table_from_csv()
```

Example 2: Converting sqlite table to csv file.

```python
# Import module.
from pycsvtosqliteroh import *
# Create object and than convert to .csv file.
sqliteobj = SqliteToCsv(file, database, tablename)
sqliteobj.convert_table_to_csv()
```

### Using the cli

To show the help run the following command:

```python
python -m pycsvtosqliteroh.main -h
```
Result:
```
usage: __main__.py [-h] [-file FILE] [-db DATABASE] [-table TABLENAME]

options:
  -h, --help            show this help message and exit

CsvToSqlite:
  -file FILE, --file FILE
                        Csv file that will be converted.
  -db DATABASE, --database DATABASE
                        Sqlite database.
  -table TABLENAME, --tablename TABLENAME
                        Sqlite table.
```

Using the conversion:

Converts a .csv file to a sqlite table:

```python
python -m pycsvtosqliteroh --file "Filename" --database "TestDb.sqlite"
```

Converts a sqlite table to a .csv file:
```python
python -m pycsvtosqliteroh --file "NewFileCreated" --database "TestDb.sqlite" --table "Tablename"
```
## Releasing

Releases are published automatically when a tag is pushed to GitHub.

```Powershell
# Create release variable.
$Release = "x.x.x"
# Create commit.
git commit --allow-empty -m "Release $Release"
# Create tag.
git tag -a $Release -m "Version $Release"
# Push from original.
git push origin --tags
# Push from fork.
git push upstream --tags
```

## License

[MIT](/LICENSE)