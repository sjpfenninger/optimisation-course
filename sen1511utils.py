import pandas as pd
import pyomo.environ as pyo
from IPython.display import display, HTML


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
    except Keyerror:
        dual = None
    slack = constraint.slack()
    expr = constraint.expr.to_string()
    return {
        "Name": name,
        "Expression": expr,
        "Value": value,
        "Shadow price": dual,
        "Binding": True if slack == 0 else False,
    }


def get_variable_info(model, variable):
    name = variable.name
    value = variable()
    return {"Name": name, "Value": value}


def get_objective_info(model, objective):
    name = objective.name
    value = objective()
    return {"Name": name, "Value": value}


def summarise_lp_results(model):
    components = list(model.component_objects())
    objectives = [i for i in components if isinstance(i, pyo.base.objective.Objective)]
    variables = [i for i in components if isinstance(i, pyo.base.var.Var)]
    constraints = [
        i for i in components if isinstance(i, pyo.base.constraint.Constraint)
    ]

    df_objectives = pd.DataFrame([get_objective_info(model, c) for c in objectives])
    df_variables = pd.DataFrame([get_variable_info(model, c) for c in variables])
    df_constraints = pd.DataFrame([get_constraint_info(model, c) for c in constraints])

    display_side_by_side(
        [df_objectives, df_variables, df_constraints],
        captions=["Objective", "Variables", "Constraints"],
    )
