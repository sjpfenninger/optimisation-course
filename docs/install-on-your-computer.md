# Install and run on your own computer

## Install Python, Jupyter and Pyomo

The instructions should be equally valid for macOS, Linux, and Windows.

Note: If you prefer to work with the terminal / command line, see the terminal instructions further below.

* Install the [Anaconda Python distribution](https://docs.anaconda.com/free/anaconda/install/).
* Download the [course files](https://github.com/sjpfenninger/optimisation-course/archive/refs/heads/main.zip) and unzip the content.
* Launch [Anaconda Navigator](https://docs.anaconda.com/free/navigator/getting-started/#navigator-starting-navigator) (included with the Anaconda Python distribution).
* Create a new environment in Anaconda Navigator by importing the file `environment.yaml` file inside the folder of downloaded course files, [as per the official documentation](https://docs.anaconda.com/free/navigator/tutorials/manage-environments/#importing-an-environment). Call this new environment "`optimisation-course`" or anything else you like.
* Go to the "Home" tab in Anaconda Navigator, and click "JupyterLab" to launch Jupyter Lab. Make sure your newly-created environment is active on the "Environments" tab beforehand.
* You can now navigate to where you stored the downloaded course files, open and run one of the course notebooks.

### Alternative: using the terminal

After installing the Anaconda Python distribution and downloading the course files, you can also proceed in the terminal if you prefer this:

* In a terminal window, navigate to the downloaded folder and install the requirements by executing: `conda env create -f environment.yml`
* Run Jupyter Lab inside the downloaded folder - this way you don't have to navigate to the folder within Jupyter Lab: `conda activate optimisation-course; jupyter lab`

## Using Gurobi

Gurobi is a more powerful commercial LP and MILP solver than the free and open-source GLPK used in the course notebooks. For larger problems (more than a few 10,000 variables or constraints, and/or for mixed-integer problems) Gurobi is significantly faster.

You can install a separate environment with Gurobi included by using the provided [`environment-gurobi.yaml`](https://github.com/sjpfenninger/optimisation-course/raw/main/environment-gurobi.yml) file - or install Gurobi manually as per the [download instructions in its website](https://www.gurobi.com/).

You will need to [request and install a free academic license from Gurobi](https://www.gurobi.com/downloads/end-user-license-agreement-academic/), which only works from machines on the TU Delft (or other university) network.

To use Gurobi instead of GLPK, you only need to do

```python
solver = pyo.SolverFactory('gurobi')
```

instead of

```python
solver = pyo.SolverFactory('glpk')
```

## Using an editor

If you prefer working with an editor rather than Jupyter Lab, you can still use the provided `environment.yaml` file to install all requirements.

### Visual Studio Code

See the official documentation on [how to work with "conda" type Python environments](https://code.visualstudio.com/docs/python/environments).

### PyCharm

See the official documentation on [configuring a conda virtual environment](https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html#conda-requirements).
