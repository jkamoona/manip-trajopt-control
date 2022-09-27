# Installing the development environment

After you are done installing Python and Git following the instructions in the Project Plan, it is time to setup the porject using pip and venv.

Venv is a standard Python module which will enable us to create a Python virtual environments in which the project packages will be installed.
Pip is a package installer for Python, it will help us install Python packages in a consistent manner.

## Creating a virtual environment for the project

In you terminal, go to the project directory and create a virtual environments containing the files required for the project.

Linux/MacOs:

```console
python3.10 -m venv /path_to_project_folder/env
```

Windows:

```console
python3.10 -m venv c:\path_to_project_folder\env
```

(Note: Since the main difference between Linux/MacOs and Windows is that we replace forward slash by backslashes and the name of the root directory '/' vs 'c:\' all further paths will only be written with Linux/MacOs path convention.)

## Entering the project virtual environment

Anytime you wish to run the python interpreter of the project, the project virtual environment should be activated. It is sufficient to activate the virtual environment once per session.

Activating the virtual environment:

Linux/MacOs:

```console
source /path_to_project_folder/env/bin/activate
```

Windows:

```console
. c:\path_to_project_folder\env\bin\activate
```

Sanity check, if you run:

```console
python --version
```

The output must be python 3.10.minor-version.
On my laptop:

```console
$ python --version
Python 3.10.4
```

## Installing packages in the environment

After having gone to the project root repository and having activated the environment, run:

```console
python -m pip install --upgrade pip setuptools wheel pip-tools
pip-sync
```

Your Python development environment is now setup. Good job!
