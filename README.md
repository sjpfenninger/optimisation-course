[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
[![CC BY 4.0][cc-by-shield]][cc-by]

# SEN1511: Engineering Optimization and Integrating Renewables in Electricity Markets

Materials for the TU Delft COSEM MSc course [SEN1511](https://studiegids.tudelft.nl/a101_searchCtrl.do?course_code=SEN1511&surname=&item_value=&onlyElectives=Y&tag_id=&deleteTag_id=&operation=searchOnCode).

## Run notebooks online

This is the easiest option if you do not want to set up Python on your own computer or to work in a computer room.

You will work in a temporary session in your web browser. You can either run the notebooks on Binder or on Google Colab. Try both and see which you prefer. Google Colab requires you to be logged in with your Google Account but has the advantage that you can easily save modified copies of the notebooks to your account.

| No. | Topic | Binder | Google Colab |
|---|---|---|---|
| 0 | Getting started | [Link](https://mybinder.org/v2/gh/sjpfenninger/sen1511/HEAD?labpath=0%20-%20Getting%20started.ipynb) | [Link](https://colab.research.google.com/github/sjpfenninger/sen1511/blob/main/0%20-%20Getting%20started.ipynb)|
| 1 | LP | [Link](https://mybinder.org/v2/gh/sjpfenninger/sen1511/HEAD?labpath=1%20-%20LP.ipynb) | [Link](https://colab.research.google.com/github/sjpfenninger/sen1511/blob/main/1%20-%20LP.ipynb)|
| 1 | LP - Solutions | [Link](https://mybinder.org/v2/gh/sjpfenninger/sen1511/HEAD?labpath=1%20-%20LP%20-%20Solutions.ipynb) | [Link](https://colab.research.google.com/github/sjpfenninger/sen1511/blob/main/1%20-%20LP%20-%20Solutions.ipynb)|
| 2 | MILP - Solutions| [Link](https://mybinder.org/v2/gh/sjpfenninger/sen1511/HEAD?labpath=2%20-%20MILP%20-%20Solutions.ipynb) | [Link](https://colab.research.google.com/github/sjpfenninger/sen1511/blob/main/2%20-%20MILP%20-%20Solutions.ipynb)|
| 4 | NLP - Solutions| [Link](https://mybinder.org/v2/gh/sjpfenninger/sen1511/HEAD?labpath=4%20-%20NLP%20-%20Solutions.ipynb) | [Link](https://colab.research.google.com/github/sjpfenninger/sen1511/blob/main/4%20-%20NLP%20-%20Solutions.ipynb)|

## Run locally on your machine

(work in progress)

* [Install Anaconda](https://docs.anaconda.com/anaconda/install/)
* Install the requirements by executing in a terminal window: `conda env create -f environment.yml; conda activate sen1511`
* Run jupyter lab by executing in a terminal window: `jupyter lab`
* Open one of the notebooks and make sure you select the `sen1511` environment so that the necessary packages are available

### Using Gurobi

Gurobi is a more powerful commercial solver than the free and open-source GLPK used in the course notebooks. For larger problems (more than a few 10,000 variables or constraints, and/or for mixed-integer problems) Gurobi is significantly faster.

You can install a separate environment with Gurobi: `conda env create -f environment-gurobi.yml` or install it manually as per the [download instructions in its website](https://www.gurobi.com/).

You will need to [request and install a free academic license from Gurobi](https://www.gurobi.com/downloads/end-user-license-agreement-academic/), which only works from machines on the TU Delft (or other university) network.

To use Gurobi instead of GLPK, you only need to do

```python
solver = pyo.SolverFactory('gurobi')
```

instead of

```python
solver = pyo.SolverFactory('glpk')
```

## License

[![CC BY 4.0][cc-by-image]][cc-by]

This work is licensed under a [Creative Commons Attribution 4.0 International License][cc-by].
