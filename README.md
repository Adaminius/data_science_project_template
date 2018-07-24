[Watered down template inspired by this post for my personal use.](https://drivendata.github.io/cookiecutter-data-science/#build-from-the-environment-up)

# Project Name

**Keywords:** keyword1, keyword2, keyword3, ...

This is a repository we can clone at the start of a new project to base
its structure off of. Hopefully this will keep things organized and
consistent! A description of the project goes here.

## Requirements

Any sort of software requirements that aren't easily inferred from
python import statements should be listed here. Generally it can be
expected that these will be involved:

* Python 3.6
* Jupyter
* Pandas
* Matplotlib

You might also use a **requirements.txt** file with conda or pip.

## Goals

* Here we try and break down our project into steps
* ~~We can cross things off as we finish them~~
* Optionally place an expected total time estimate for a goal in
parentheses at the end (2h)
* Or record time actually spent on a goal in curly braces (2h){4h}

## Files

We write a small description of what's in each file here.

* **README.md** This file! It describes the project.
* **acquire_data.py** This should download or explain how to obtain data
for the project, storing it in the raw/ directory.
* **.env** Not committed. Store environment variables/secrets
 that you don't want to share here.
* **requirements.txt** Can contain a list of packages to install with
conda or pip.
    * Can generate with e.g. `pip freeze > requirements.txt` or `conda
    list --export > requirements.txt`
    * Then install packages with `pip install -r requirements.txt`
    or create conda environment with `conda create -n MY_ENV_NAME --file
     requirements.txt`
* **scripts/template.sh** Demonstrates how to use load variables from
.env file
* **raw/** This directory is where we keep our raw data.
    * We shouldn't change this data, only add to it.
    * We don't necessarily keep this data under version control
(sometimes it can be quite large)
    * We should generally be able to acquire all our raw data by running
`python acquire_data.py`, or how the data can be acquired should be at
least described in comments there.
* **data/** Processed data goes here.
* **notebooks/** Jupyter or other kinds of notebook-style files for
data exploration go here.
* **reports/** Polished figures, reports, and analyses go here.
* **scripts/** Bash, python, etc. scripts for building data

## Log

* **yyyy-mm-dd:** Here we can describe what we added or changed each day.
* **2018-06-12:** It makes it easier to remember how
the project developed and what pitfalls we ran into.
* **2018-06-13:** Optionally place an estimate of time spent working on
the project today in curly braces at the end {1h}
* **2018-06-14:** It certainly makes sense to keep the project version
controlled under git as well. This log is supplementary to your commit
history.