[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png

# `optimisation-course`: SEN1511 Engineering Optimization and Integrating Renewables in Electricity Markets

Materials for the TU Delft COSeM MSc course [SEN1511](https://studiegids.tudelft.nl/a101_searchCtrl.do?course_code=sen1511&surname=&item_value=&onlyElectives=Y&tag_id=&deleteTag_id=&operation=searchOnCode).


## Run locally on your machine

> [!TIP]
> This is the recommended approach.

See the [separate instructions](install-on-your-computer.md).

## Run notebooks online

This is an alternative option if you do not want to set up Python on your own computer.

You will work in a temporary session in your web browser. You can either run the notebooks on Binder or on Google Colab. Try both and see which you prefer. Google Colab requires you to be logged in with your Google Account but has the advantage that you can easily save modified copies of the notebooks to your account.


| No. | Topic | Binder | Google Colab |
|---|---|---|---|
| 1.a | Getting started - Python basics | [Link](https://mybinder.org/v2/gh/sjpfenninger/optimisation-course/HEAD?labpath=1a%20-%20Getting%20started%20-%20Python%20basics.ipynb) | [Link](https://colab.research.google.com/github/sjpfenninger/optimisation-course/blob/main/1a%20-%20Getting%20started%20-%20Python%20basics.ipynb)|
| 1.b | Getting started - Pyomo introduction | [Link](https://mybinder.org/v2/gh/sjpfenninger/optimisation-course/HEAD?labpath=1b%20-%20Getting%20started%20-%20Pyomo%20introduction.ipynb) | [Link](https://colab.research.google.com/github/sjpfenninger/optimisation-course/blob/main/1b%20-%20Getting%20started%20-%20Pyomo%20introduction.ipynb)|

> [!WARNING]
> When running on Google Colab, you need to install the required Python packages and solvers because this does not happen automatically.

The following lines can be copy-pasted as a new cell at the beginning of a Colab notebook to install everything that is necessary for all types of problems discussed in this course:

```python
!pip install pyomo==6.4.1
!apt install glpk-utils
!pip install optimutils
!wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.12.0-Linux-x86_64.sh
!chmod +x Miniconda3-py37_4.12.0-Linux-x86_64.sh
!bash ./Miniconda3-py37_4.12.0-Linux-x86_64.sh -b -f -p /usr/local/
!conda install -y -c conda-forge ipopt
!conda install -y -c gurobi gurobi
```

## License

Authors: Stefan Pfenninger, Uğurcan Işık, Meike Lafeber

[![CC BY 4.0][cc-by-image]][cc-by]

This work is licensed under a [Creative Commons Attribution 4.0 International License][cc-by].
