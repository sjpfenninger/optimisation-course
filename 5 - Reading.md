# **Robustness Analysis in Optimization**
## *Analyzing the change in optimal solutions vs. the performance of the solutions*

By: Dick den Hartog, Aharon Ben-Tal, Ruud Brekelmans, Ernst Roos \
From: https://pubsonline.informs.org/do/10.1287/orms.2021.02.08/full/ 


We advocate the use of robustness analysis (RA) instead of, or in addition to, sensitivity analysis (SA) in optimization. SA analyzes the change in the optimal solution as the input data changes. Based on abundant practical experience, however, we feel that the performance of the obtained solutions under different values of the uncertain parameters is what really matters in practice. RA analyzes that performance.

**Too Much Trust** \
An analysis of linear optimization problems from the Netlib repository [1] found that 27 of the 90 problems studied have an optimal solution that severely violates at least one constraint when parameters deviate by 1%. For one problem, an error in the parameter values of 0.1% can result in a 450% violation of one of the constraints. Despite that, optimization practitioners often do not analyze how the obtained solution performs under possible changes in the parameter values.

Apart from parameter uncertainty another source of uncertainty in optimization problems is implementation errors – the discrepancy that may occur between the computed optimal or feasible solution and its actual implementation by the practitioner. This is particularly common in engineering applications. In professional reports written by optimization consultants, there are often no warnings on the lack of robustness of the solution and the possible adverse effects of implementation errors. The same holds for scholarly papers on optimization applications, which often report solutions and objective values to striking precision.

**Why this Overconfidence?** \
Why does there seem to be a lack of interest in the robustness of the solution? In our view there are several reasons. In the early days of operations research the focus was on data, but later the focus shifted toward theory, models and algorithms. In addition, university educators do not always have practical experience, resulting in education that is often not suspicious of data. The same holds for many optimization textbooks. Another potential reason is that, especially for linear models, many users believe that small errors in the parameter values cannot lead to large constraint violations, which is not true as mentioned above. Finally, optimization software does support SA but does not support a robustness analysis.

**Sensitivity Analysis is Not Enough** \
Classical SA is not very useful to study the effects of uncertainty in the parameters because SA only analyzes how the given optimal solution may change if the data changes. For example, for linear optimization it is well known that if there are multiple (almost) optimal solutions, then a small change in data may lead to totally different solutions. Moreover, for linear optimization the optimal solution is often a vertex, and only for uncertain parameters within a restricted interval, the solution stays the same. Finally, if SA shows that a solution is too sensitive, then there is no generic methodology available to find a solution that is less sensitive.

**Robustness Analysis is Needed** \
To determine how the solution performs in case the parameter values are different from the estimated ones, we advise performing a robustness analysis (RA). The first step of RA is to identify which parameters of the model are subject to uncertainty. Once the uncertain parameters have been identified, the next important step is to determine the so-called uncertainty set, which is the set of possible scenarios for the uncertain parameters. Then the effect of the scenarios in the uncertainty set on the performance of the obtained solution is calculated.

The key characteristics that are computed to analyze this effect are split into those concerning the optimality of the solution and those concerning its feasibility. For the objective function value, we compute the worst-case and average value over the parameters in the uncertainty set. The key characteristics concerning feasibility are similar: the worst-case and average constraint violation per constraint that includes uncertain parameters. The worst-case constraint violation is computed in exactly the same manner as the worst-case objective value. The average constraint violation, on the other hand, is more complicated to compute and interpret because it is simply zero for many scenarios in the uncertainty set. Therefore, it is best to compute it through sampling from the uncertainty set, and to instead report the following two characteristics: probability of violation and average violation conditional on the existence of violation.

**When the Solution is Not Robust** \
Now suppose that the RA indicates that the obtained solution is not robust. There are two possible next steps. First, one could use robust optimization to obtain solutions that are robust with respect to the uncertainty set. In this methodology the uncertainty is explicitly added to the model and a solution is obtained that is optimal with respect to the worst-case scenario of the uncertainty set. One of the advantages of the robust optimization methodology is that it is scalable, i.e., large-scale optimization problems can be solved [2].

If RA detects that the solution obtained is not robust, a second possible step is to gather more information to reduce the size of the uncertainty set.

Textbooks on (linear) optimization pay little attention to uncertainty in the parameter values, and if it is mentioned, only SA is recommended. As previously noted, SA is not enough to analyze the impact of uncertainty on an optimization model. One reason textbooks support sensitivity analysis is because the information required for SA is often obtained for free after the optimization has been solved. We recommend authors add a chapter on robustness analysis to their textbooks and that software developers add RA features to existing optimization software. Such features are easy to implement, especially for those packages that already incorporate the robust optimization methodology.

**References** \
Ben-Tal, A. and Nemirovski, A., 2000, “Robust solutions of linear programming problems contaminated with uncertain data,” Mathematical Programming, Vol. 88, No. 3, pp. 411-424. \
Ben-Tal, A., El Ghaoui, L. and Nemirovski, A., 2009, “Robust Optimization,” Princeton University Press: Princeton, N.J.