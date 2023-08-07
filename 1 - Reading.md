# Basic concepts of optimization for energy systems

## 1. Introduction

With the 2009/28/EC Directive, the European Union defined three objectives by 2020: 20% reduction in greenhouse gases emissions, 20% share of renewable energy and 20% improvement of energy efficiency. At the same time it is known that electric power systems have experienced continuous growth in all the three major sectors of the power system, i.e. generation, transmission and distribution. Problems in power systems related to efficient operation and planning are nowadays very complex and very often a large data set is associated. However,
allocation of customers’ load demands among the available power plants in an economic, secure and reliable way has been a subject of interest since hundred years. Optimization techniques have played therein a very important role, mostly defined as linear and non-linear programming, see Table 1.

**Table 1: Types of classical optimization problems**

| Objective function | Constraints | Decision variables continuous | Decision variables discrete | Type optimization problem                                                 |
| :----------------- | ----------: | ----------------------------: | --------------------------: | ------------------------------------------------------------------------- |
| Linear             |      Linear |                           Yes |                          No | LP (Linear Programming)                                                   |
| Linear             |      Linear |                           Yes |                         Yes | MILP (Mixed Integer Linear Programming)                                   |
| Non-linear         |      Linear |                           Yes |                          No | NLP (Non-Linear Programming)                                              |
| Non-linear         |      Linear |                           Yes |                         Yes | MINLP (Mixed Integer Non-Linear Programming)                              |
| Non-linear         |  Non-linear |                           Yes |                          No | NLPN (Non-Linear Programming with Non-linear constraints)                 |
| Non-linear         |  Non-linear |                           Yes |                         Yes | MINLPN (Mixed Integer Non-Linear Programming with Non-linear constraints) |

Over the past decade, many new methods have been developed to solve the large-scale complex decision problems which can also be found in the domain of energy systems, such as dynamic programming, neural network approaches, and genetic algorithms. It should be noted that mostly optimization methods have focused on solving single-objective problems, including constraints. There exists, however, a large number of problems that require the simultaneous optimization of several objectives which can be conflicting; these are the so-called multi-objective problems. The solution methods of multi-objective problems can be divided into three main categories: weight functions, Pareto-based optimization, and interactive methods. Methods of the group based on weight functions consist of combining all the objectives to optimize in a single mathematical function of their weighted sum. Despite its simplicity, this approach has several drawbacks, such as that it is very difficult to adjust the weights of the objectives to optimize, especially when they have different scales.

Pareto-based multi-objective optimization establishes relationships among solutions according to the Pareto-dominance concept. A Pareto optimal solution represents the situation where any further improvement in any one objective requires worsening of at least one other objective. Interactive methods use the information obtained from the decision maker in an iterative process to assign appropriate importance levels, e.g. weights to all individual objectives.

The optimization problems as described above have a static character. It means that the optimization variables are constant (independent of time). In many situations, the decision should be taken on how to steer a dynamic system during a time interval [t0, tF] in such a way that the performance criterion defined on this time interval is optimized:

$$ \bm{min J} = \int\_{t_0}^{t_F} f(x(t), u(t), t) dt + \Phi (\tau_0,\tau_F) $$

subject to:

$$ d \bm{x} (t)/dt = g(\bm{x} (t), \bm{u} (t), t) $$
$$\phi_i (\bm{u} (t), t) \geq \bm{0}, i = 1, \ldots, p$$
$$\kappa_j (\bm{x} (t), t) \geq \bm{0}, j = 1, \ldots, q$$
$$\nu_k (\tau_0,\tau_F) \geq \bm{0}, k = 1, \ldots, r$$

where:

$\bm{x} (t) = [x_1(t), \ldots, x_n(t)]^T$ **is the state vector**

$\bm{u} (t) = [u_1(t), \ldots, u_m(t)]^T$ **is the control vector (optimization variable)**

$\tau_0 = [t_0, x_1(t_0), \ldots, x_n(t_0)]^T$

$\tau_F = [t_F, x_1(t_F), \ldots, x_n(t_F)]^T$

$\Phi (\tau_0,\tau_F)$ **are the initial costs / final value function**

In this course, we will learn, step by step, how simple optimization techniques can be used to solve decision problems in power systems. It should be stressed that the methods presented are applicable for many application domains, such as industry, supply chain management, etc.

The optimization problems which will be discussed during this course are related to the operation and design of the (future) power system and contain economic dispatch, optimal power flow, unit commitment, design choices for electricity and heat for eco-cities, and optimal charging of electric vehicles.

# 2. Economic Dispatch

The economic dispatch (ED) problem consists in allocating the total demand among generating units so that the production cost is minimized. Generating units have different production costs depending on the prime energy source used to produce electricity (mainly coal, oil, natural gas, uranium, and water stored in reservoirs). These costs vary significantly; for example, the marginal costs for nuclear, coal, and gas units may vary considerably. It includes determining the set of generators that are providing power and their output levels. If an inappropriate set of generators is dispatched, the dispatch is said to be inefficient.

For each generating unit "i" a function $C_i(P_{Gi})$ is assigned characterizing its generating cost in €/h in terms of the power produced in MW, $P_{Gi}$, during 1 h. Here we assume that each unit has a constant marginal cost (fuel efficiency) $C_i$, independent of the amount of power produced. So the overall cost of producing an amount PG becomes:

$$C(PG) = \sum_{i=1}^{n} C_i(P_{Gi}) = \sum_{i=1}^{n} C_i * P_{Gi} \tag{1}$$

where $P_G$ is the column vector of the unit generation levels $P_{Gi}$.

If the system total demand is $P^{total}_D$ and all generating units contribute to supply this demand, then the total production or generation must equal the total demand plus transmission losses, $P_{loss}$, that is:

$$\sum_{i=1}^{n} P_{Gi} = P^{total}_D + P_{\text{loss}} \tag{2} $$

The ED problem consists of minimizing the total cost $C(P_G)$ as defined in equation (1) with respect to the unit generation outputs, $P_{Gi}$, subject to the power balance, equation (2), and to the generating unit operational limits:

$$P^{\text{min}}_{Gi} \leq P_{Gi} \leq P_{\text{max}_i} \tag{3}$$

where superscripts "min" and "max" indicate minimum and maximum, respectively.

We first consider the basic ED without losses. Such a decision problem can be described as a linear programming problem.

# 3 Linear Programming problem (LP)

A linear programming (LP) problem is a constrained optimization problem, in which the maximum or minimum value of a linear expression, called the objective function, subject to a number of linear constraints has to be found. Linear programming is one of the widely used optimization techniques. The term linear programming was given by George Dantzing in 1947 to problems in which both the objective function and the constraints are linear. The word programming does not refer to computer programming, but means optimization. This is also true in the term nonlinear programming.

As with each optimization problem, an LP problem can be described by specifying:

1. Decision variables (optimization variables / degrees of freedom)
2. Objective function (performance criterion)
3. Equality and/or inequality constraints

Each of these problems may involve many variables, many equations, and many inequalities. With the aid of modern software, LP problems with many thousands of variables and constraints can be solved.

The objective function (criterion) is given by:

$$f(x) = c_1x_1 + c_2x_2 + c_3x_3 + \ldots + c_nx_n \tag{4}$$

subject to a number of linear constraints of the form:

$$a_{11}x_1 + a_{12}x_2 + a_{13}x_3 + \ldots + a_{1n}x_n \leq b_1$$
$$a_{21}x_1 + a_{22}x_2 + a_{23}x_3 + \ldots + a_{2n}x_n \leq b_2$$
$$\ldots$$
$$a_{m1}x_1 + a_{m2}x_2 + a_{m3}x_3 + \ldots + a_{mn}x_n \leq b_m \tag{5}$$

The variables $(x_1, x_2, x_3, \ldots, x_n)$ are called the **decision variables**.

The largest or smallest value of the objective function is called the **optimal value**, and a collection of values $(x_1^*, x_2^*, x_3^*, \ldots, x_n^*)$ that gives the optimal value is called an **optimal solution**.

To formulate a real problem as a linear programming problem, the following steps should be done:

1. Identify and define the decision variables for the problem.
2. Define the objective function.
3. Identify and express mathematically all constraints.

Realize that problem formulation is the most important and usually the most difficult part of solving a real problem. Solving a problem that is not modeled adequately is useless.

### Solving an LP Problem

To find the optimal solution, we should first determine the so-called **feasible region**. The feasible region is the set of all feasible points that satisfy all of the constraints. The optimal solution is then a feasible solution that gives the best (the highest or the lowest) value of the objective function. The corners of the feasible region are called **extreme points** (they lie on the intersection of two or more constraints).

If an **optimal solution** exists, it will be an extreme point, but it may not be unique. If the problem is infeasible (it is impossible to satisfy all the constraints) or it is unbounded (the constraints do not define a closed area), there is no solution at all.

To find the optimal solution, the value of the objective function for all the extreme points (corners of the feasible region) should be calculated. The one which produces the best value of the objective function would be the optimal solution. In practice, this approach is not efficient for problems with a large number of extreme points (e.g. for real problems with hundreds or thousands of variables and/or constraints). The graphical method performed according to the above-mentioned steps is only practical for problems with two decision variables.

The **Simplex method** is an efficient (and mostly used) procedure for solving linear programming problems (LP). It starts with the identification of any initial extreme point. Next, the algorithm looks along each edge from this initial extreme point to the next extreme point. For all neighboring extreme points, the value of the objective function is calculated. The extreme point with the best objective-function value will then be the new "initial" extreme point, and the algorithm repeats the previous step. The procedure moves only from one extreme point to a better one – this means that many extreme points are skipped (not checked). If the objective-function values do not improve by moving along edges, the extreme point with the best value so far is the optimal solution.





# 4 Duality in Linear Programming

Duality is a mathematical concept that links two mathematical structures and allows extracting information from one of these structures based on information available from the other one.

Duality in Linear Programming relates a linear programming problem (primal problem) with a so-called dual problem.

A **primal linear programming problem** (LP) can be formulated as:

$$\max J(x) = c^Tx$$

subject to equality and inequality constraints:

$$\bm{A}_E \bm{x} = \bm{b}_E$$
$$\bm{A}_I \bm{x} \leq \bm{b}_I$$
$$x_1, ..., x_n \geq 0$$

- $\bm{c} \in \mathbb{R}^n$ is the cost coefficient of the n-dimensional decision vector $x$.
- $\bm{A}_E \in \mathbb{R}^{m \times n}$ and $\bm{b}_E \in \mathbb{R}^m$ define the m linear equality constraints.
- $\bm{A}_I \in \mathbb{R}^{l \times n}$ and $\bm{b}_I \in \mathbb{R}^l$ define the l linear inequality constraints.

The following linear minimization problem is the dual of the primal LP problem formulated above:

$$\min F(\bm{\lambda}, \bm{\mu}) = \bm{bE^T \lambda} + \bm{bI^T\mu}$$

so that the constraints are satisfied:

- $\bm{ A}_E^T\lambda + \bm{A}_I^T\mu \geq c$

- $ \lambda_1, ..., \lambda_m $ are unrestricted in sign (free)

- $\mu_1, ..., \mu_l \geq 0$

The following observations can be made:

- The primal problem has n decision variables and m+l constraints; the dual problem has m+l decision variables ($\lambda$ and $\mu$) and n constraints.
- The constraints of the dual problem involve the transposed of the matrices $A_E$ and $A_I$ defining the constraints of the primal problem.
- The constant vectors $b_E$ and $b_I$ on the right-hand side of the primal constraints form the cost coefficients of the dual linear objective function $F$.
- The cost coefficient vectors $\bm{c}$ of the primal linear objective function $J$ appear on the right-hand side of the dual constraints.
- The direction of the primal problem (maximization) is opposite to the dual one (minimization) or vice versa.
- Signs of the primal constraints set the bounds on the associated variables, and the other way around (see Yable 1)

***Table 2:*** *Relationships between primal (to maximize) and dual LP problems*
![Table 2](/images/1Reading_Table2.png)

### _Example 1_

Consider a primal problem:

$$\max J(\bm{x}) = 5x_1 - 2x_2$$

subject to the following constraints:

$$2x_1 + x_2 \leq 9$$
$$x_1 - 2x_2 \leq 2$$
$$-3x_1 + 2x_2 \leq 3$$
$$x_1, x_2 \geq 0$$

The dual problem for this primal problem is:

$$\min F(\bm{\mu}) = 9\mu_1 + 2\mu_2 + 3\mu_3$$

subject to the constraints:

$$2\mu_1 + \mu_2 - 3\mu_3 \geq 5$$
$$\mu_1 - 2\mu_2 + 2\mu_3 \geq -2$$
$$\mu_1, \mu_2, \mu_3 \geq 0$$

### _Solution example 1_

Solution to the primal problem is:
$$ x*1^* = 4; x*2^* = 1; $$
$$ J(x) = 18$$

The active constraints are:
$$ 2x_1 + x_2 = 9$$
$$ x_1 - 2x_2 = 2$$

The shadow prices (Lagrange multipliers) for the active constraints are 1,6 and 1,8 resp. This means that if the bound of the first constraint is changed from 9 to 10, the value of the objective function increases by 1,6 and become 19,6 (=18+1,6). Changing the bound of the second constraint from 2 to 3, results in increasing of the objective function by 1,8.

Solution of the dual problem is:
$$μ_1^* = 1,6; μ_2^* = 1,8, μ_3^*=0 $$
$$F(μ^{*}) = 18$$

### Conclusion

the optimum value of the primal and the dual objective function is equal to 18.
The optimal values of the decision variables of the dual problem are equal to the
Lagrange multipliers of the primal problem.
Other way around, the shadow prices (Lagrange multipliers) of the dual problem
are equal to the solution of the primal problem.

### _Example 2_

The primal problem is given by:

$ \text{Max } J(\mathbf{x}) = x_1 + 4x_2 $

subject to:

- $ x_1 + 2x_2 \leq 5 $
- $ 2x_1 + x_2 = 4 $
- $ x_1 - x_2 \geq 1 $ (this is the same as $ x_1 + x_2 \leq -1 $)
- $ x_1, x_2 \geq 0 $

Since there are three primal constraints (one equality and two inequalities), there
are three dual variables for the problem: $ \lambda_1 $, $ \mu_1 $, and $ \mu_2 $. Therefore the dual problem
is:

$$ \text{Min } F(\lambda, \mu) = 5\mu_1 + 4\lambda_1 - \mu_2 $$

subject to:

- $ \mu_1 + 2\lambda_1 - \mu_2 \geq 1 $
- $ 2\mu_1 + \lambda_1 + \mu_2 \geq 4 $
- $ \mu_1, \mu_2 \geq 0 $
- $ \lambda_1 $ is unrestricted in sign (free).

Solution to the primal problem is:

$ x_1^{*} = 1.666667 $

$ x_2^{*} = 0.666667 $

$ J(\mathbf{x}^{*}) = 4.33333 $

The active constraints are:

$ 2x_1 + x_2 = 4 $ and
$ -x_1 + x_2 = -1 $

The shadow prices (Lagrange multipliers) for these active constraints are:

$ \mu_1 = 1.666667 $, $ \mu_2 = 2.333333 $

The solution to the dual problem is:

$ \mu_1 = 0 $

$ \mu_2 = 2.333333 $

$ \lambda_1 = 1.666667 $

$ F(\bm{\lambda^{*}}, \bm{\mu^{*}}) = 4.333333 $

### _Example 3_

Consider an electricity market that includes two power producers: A and B. Each
of them runs a power plant with a capacity of 100 MW. Producer A offers to sell
energy at €10/MWh, while producer B does it at €30/MWh. A demand of 130
MWh is to be supplied.

The dispatch is defined by, where PA and PB are the amounts of power sold by A
resp., B in the coming hour:

$ \min (10 P_A + 30P_B) $

subject to:

$P_A + P_B = 130$

$0 \leq P_A \leq 100$

$0 \leq P_B \leq 100$

This dispatch problem is trivial; the solution is $P_A$ = 100MW and $P_B$ = 30MW. To
define the clearing (marginal) price for energy the dual problem can be solved.
The primal problem is to minimize an objective function, therefore the
relationship from Table 2 is converted into Table 3.

***Table 3.*** *Relationship between Primal problem (to minimize) and Dual LP*

![Table 3](/images/1Reading_Table3.png)


$ \max (130 \lambda_1 + 100 \mu_1 + 100 \mu_2)$

subject to:

- $\lambda_1 + \mu_1 + 0 \mu_2 \leq 10$

- $\lambda_1 + 0\mu_1 + \mu_2 \leq 30$

- $\lambda_1$ is unrestricted in sign (free)

- $\mu_1, \mu_2 \leq 0$


Here $\lambda_1^{*}$ = 30 (the dual variable of the equality constraint), that is the clearing
price for energy.



# 5 Illustrative example of duality in Linear Programming

An illustrative small example of the relationship between primal and dual linear programs will show that these two problems arise from two different perspectives on the same application. As an example, we introduce a diet problem.

Johanna is deciding what to purchase for lunch. She has two choices:
1. Soup, which costs $2.80 per$ portion,
2. Salad with fresh vegetables, which costs $3.20 per$ portion.

In this lunchroom, it is possible to purchase a fraction of an item if the client wishes. Also, the farmer can sell a fraction of a vegetable to the owner of the lunchroom.

The soup ingredients are: onion, carrot, and tomato. The ingredients for the salad are onion, carrot, and apple. The amount of the ingredients is specified in recipes presented in the table below:

| Ingredient | Soup (x_1) | Fresh salad (x_2) |
|-----------|----------|------------------|
| Onion     | 1        | 0.5              |
| Carrot    | 2.5      | 3                |
| Tomato    | 2        | 0                |
| Apple     | 0        | 1                |
| Cost      | 280      | 320              |

Requirements:
- Onion: 0.5
- Carrot: 4
- Tomato: 1.5
- Apple: 1.5

Johanna wants to minimize the lunch cost by finding the least expensive combination of soup and fresh salad that meets her requirements, whereby she needs at least 1 onion, 3 carrots, 1 tomato, and 1 apple for lunch.

This decision problem can be formulated as an LP problem as follows:

Minimize $280x_1 + 320x_2$

subject to:

$ x_1 + 0.5x_2 \geq 0.5 $

$ 2.5x_1 + 3x_2 \geq 4 $

$ 2x_1 \geq 1.5 $

$ x_2 \geq 1.5 $

$ x_1, x_2 \geq 0 $

By applying the Linear Programming method to this problem, we can find easily that the unique solution is $ x_1 = 0.75 $ and $ x_2 = 1.5 $, i.e. it means ¾ portion soup and 1½ portion salad.

The value of the cost function for the optimal solution is $ 280 \times 0.75 + 320 \times 1 = 690 $.

There are 2 active constraints: $ 2x_1 \geq 1.5 $ and $ x_2 \geq 1.5 $.

The shadow price is 140 for the active constraint $ 2x_1 \geq 1.5 $, i.e., the cost will be 830 if the wish would be to eat at least 2.5 tomatoes.

The shadow price is 320 for the active constraint $ x_2 \geq 1.5 $, i.e., the cost will be 1010 if the wish would be to eat at least 2.5 apples.

Let us have a look at this problem from the perspective of the farmer who supplies the lunchroom with vegetables. The owner of the lunchroom needs to buy at least 0.5 onion, 4 carrots, 1.5 tomatoes, and 1.5 apples.

The farmer wants to maximize his revenues. His decision problem is: How can I set the prices per onion, carrot, tomato, and apple so that the lunchroom owner will buy them from me, and my revenue is maximized?

The lunchroom owner will buy vegetables only if the total cost of soup is below 2.80€ and for the salad below 320€.

These restrictions impose the following constraints on the prices $ \mu_1, \mu_2, \mu_3, $ and $ \mu_4 $ for onions, carrots, tomatoes, and apples:

$ 1 \mu_1 + 2.5 \mu_2 + 2 \mu_3 + 0 \mu_4 \leq 280 $

$ 0.5 \mu_1 + 3 \mu_2 + 0 \mu_3 + 1 \mu_4 \leq 320 $

Clearly, all the prices for all these vegetables should be nonnegative.

The revenue of the farmer is $ (0.5 \mu_1 + 4 \mu_2 + 1.5 \mu_3 + 1.5 \mu_4) $ and it should be maximized. This gives us the following dual problem:

Maximize $ F(\mu) = 0.5 \mu_1 + 4 \mu_2 + 1.5 \mu_3 + 1.5 \mu_4 $

subject to:

$ 1 \mu_1 + 2.5 \mu_2 + 2 \mu_3 \leq 280 $

$ 0.5 \mu_1 + 3 \mu_2 + \mu_4 \leq 320 $

$ \mu_1, \mu_2, \mu_3, \mu_4 \geq 0 $

By applying the Linear Programming method to this dual problem, we can find easily that the unique solution is $ \mu_1 = 0, \mu_2 = 0, \mu_3 = 140, \mu_4 = 320 $.

It may seem strange that the farmer charges nothing for onion ($ \mu_1 = 0 $) and carrot ($ \mu_2 = 0 $). He charges 1.40€ per tomato and 3.20€ per apple. It is better for him to give onions and carrots for free and charge as much as possible for tomatoes and apples.
