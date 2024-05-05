# pycsvtosqliteroh

_The pycsvtosqliteroh module is a module to convert csv to sqlite._

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

I've written this module to bulk convert csv files in to sqlite tables. The database is used as a test database in another project.

At the moment only the conversion from csv to sqlite is possible. The supported delimiters for the .csv file are "," and ";". 

All testfiles in the [testfiles](/tests/testfiles/) folder, are created via powershell, using the ```Export-Csv``` cmdlet with different delimiters.

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

Example 1:

```python
# Import module.
from pycsvtosqliteroh import *
# Create object and than convert to sqlite table.
csvobj = CsvToSqlite(file, database)
csvobj.create_table_from_csv()
```

### Using the cli

To show the help run the following command:

```python
python -m pycsvtosqliteroh.main -h
```
Result:
```
usage: main.py [-h] [-file FILE] [-database DATABASE]  

options:
  -h, --help            show this help message and exit

CsvToSqlite:
  -file FILE, --file FILE
                        Csv file that will be converted.
  -database DATABASE, --database DATABASE
                        Sqlite table.
```

Using the conversion:

```python
python -m pycsvtosqliteroh --file "Filename" --database "TestDb.sqlite"
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