import itertools

import pandas as pd
import pyomo.environ as pyo
from IPython.display import display, HTML


# Source: https://stackoverflow.com/a/47428575
def type_of_script():
    try:
        ipy_str = str(type(get_ipython()))
        if "zmqshell" in ipy_str:
            return "jupyter"
        if "terminal" in ipy_str:
            return "ipython"
    except:
        return "terminal"


# Source: https://stackoverflow.com/a/57832026
def display_side_by_side(dfs: list, captions: list):
    """Display tables side by side to save vertical space
    Input:
        dfs: list of pandas.DataFrame
        captions: list of table captions
    """
    output = ""
    combined = dict(zip(captions, dfs))
    for caption, df in combined.items():
        output += (
            df.style.set_table_attributes("style='display:inline'")
            .set_caption(caption)
            ._repr_html_()
        )
        output += "\xa0\xa0\xa0"
    display(HTML(output))


def get_constraint_info(model, constraint):
    name = constraint.name
    value = constraint()
    try:
        dual = model.dual[constraint]
    except KeyError:
        dual = None
    # slack = constraint.slack()
    expr = constraint.expr.to_string()
    result = {"Name": name, "Expression": expr, "Value": value}
    if dual is not None:
        result["Shadow price"] = dual
        result["Binding"] = True if round(dual, 9) != 0 else False
    return result


def get_variable_info(model, variable):
    name = variable.name
    value = variable()
    return {"Name": name, "Value": value}


def get_objective_info(model, objective):
    name = objective.name
    value = objective()
    return {"Name": name, "Value": value}


def summarise_results(model):
    components = list(model.component_objects())
    objectives = [i for i in components if isinstance(i, pyo.base.objective.Objective)]
    scalar_variables = [i for i in components if isinstance(i, pyo.base.var.ScalarVar)]
    scalar_constraints = [
        i for i in components if isinstance(i, pyo.base.constraint.ScalarConstraint)
    ]
    indexed_variables = [
        i[j]
        for i in components
        if isinstance(i, pyo.base.var.IndexedVar)
        for j in i.index_set()
    ]
    indexed_constraints = [
        i[j]
        for i in components
        if isinstance(i, pyo.base.constraint.IndexedConstraint)
        for j in i.index_set()
    ]
    variables = scalar_variables + indexed_variables
    constraints = scalar_constraints + indexed_constraints

    df_objectives = pd.DataFrame([get_objective_info(model, c) for c in objectives])
    df_variables = pd.DataFrame([get_variable_info(model, c) for c in variables])
    df_constraints = pd.DataFrame([get_constraint_info(model, c) for c in constraints])

    env = type_of_script()

    if env == "jupyter":
        display_side_by_side(
            [df_objectives, df_variables, df_constraints],
            captions=["Objective", "Variables", "Constraints"],
        )
    else:
        print("Objective")
        print("=========")
        print(df_objectives)
        print("\n")
        print("Variables")
        print("=========")
        print(df_variables)
        print("\n")
        print("Constraints")
        print("===========")
        print(df_constraints)
