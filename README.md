Hawaii Climate analysis. 

Analytical Project providing a climate analysis api.

## Data Engineering

The climate data for Hawaii is provided through two CSV files. Start by using Python and Pandas to inspect the content of these files and clean the data.

* `data_engineering.ipynb` for Data Engineering tasks.

* Pandas to read in the measurement and station CSV files as DataFrames.

* NaNs Inspected and missing values are replaced.

* Output clean data version.

---

## Database Engineering

SQLAlchemy to model table schemas and create a sqlite database for tables. 

* `database_engineering.ipynb` Database Engineering work.

* Pandas to cleaned measurements and stations CSV data.

* `engine` and connection string to create a database called `hawaii.sqlite`.

* `declarative_base` and create ORM classes for each table.

  * a class for `Measurement` and for `Station`.

* Database Tables

---

## Climate Analysis and Exploration

Python and SQLAlchemy for  climate analysis and data exploration

* `climate_analysis.ipynb` climate analysis and data exporation.
* Precipitation Analysis
* Station Analysis
* Temperature Analysis


## Climate App

Flask api based on the queries .

* FLASK data routes.