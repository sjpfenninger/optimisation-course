# Setting up the course environment on your computer

## Recommended approach to install everything

These instructions should be equally valid for macOS, Linux, and Windows.

* Install the [Anaconda Python distribution](https://docs.anaconda.com/free/anaconda/install/).
* Download the [course files](https://github.com/sjpfenninger/optimisation-course/archive/refs/heads/main.zip) and unzip the content.
* Launch [Anaconda Navigator](https://docs.anaconda.com/free/navigator/getting-started/#navigator-starting-navigator) (included with the Anaconda Python distribution).
* Create a new environment in Anaconda Navigator by importing the file `environment.yaml` file inside the folder of downloaded course files, [as per the official documentation](https://docs.anaconda.com/free/navigator/tutorials/manage-environments/#importing-an-environment). Call this new environment "`optimisation-course`" or anything else you like.
* Go to the "Home" tab in Anaconda Navigator, and click "JupyterLab" to launch Jupyter Lab. Make sure your newly-created environment is active on the "Environments" tab beforehand.
* You can now navigate to where you stored the downloaded course files, open and run one of the course notebooks.

> [!TIP]
> If you have issues with JupyterLab not appearing in your list of installed tools, a possible workaround is to launch JupyterLab by launching a terminal from Anaconda Navigator and then typing `jupyter lab` in the terminal window that appears.

## Alternative instructions for more experienced users

### Using the terminal

The Anaconda Python distribution is optional, to make things easier for people with little Python experience. You can use any other installation of Python and just need to install the required packages. Assuming you have a working `conda` installation you can also:

* In a terminal window, navigate to the downloaded course file folder and install the requirements by executing: `conda env create -f optimisation-course-environment.yml`
* Run Jupyter Lab inside the downloaded folder - this way you don't have to navigate to the folder within Jupyter Lab: `conda activate optimisation-course; jupyter lab`

### Using an editor

If you prefer working with an editor rather than Jupyter Lab, you can still use the provided `optimisation-course-environment.yaml` file to install all requirements.

#### Visual Studio Code

See the official documentation on [how to work with "conda" type Python environments](https://code.visualstudio.com/docs/python/environments).

#### PyCharm

See the official documentation on [configuring a conda virtual environment](https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html#conda-requirements).
