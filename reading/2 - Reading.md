# ELECTRICITY MARKET OPERATIONS
> See: Francisco D. Galiana and Antonio J. Conejo, Ch. 5 “Economics of Electricity Generation” in:
Electric Energy Systems Analysis and Operation, Edited by Antonio G.Exposito , Antonio J . Conejo , and Claudio
Canizares, CRC Press 2008, Print ISBN: 978-0-8493-7365-7


An electricity market includes different trading mechanisms, primarily the pool, bilateral contracting, and forward contracting through the futures market. Generating companies submit generating offers to the pool, while loads submit consumption bids. The market operator (APX) then uses a market-clearing procedure to determine the accepted offers and bids, and the market-clearing prices. The market operator manages the day-ahead market, which is cleared one day in advance and spans typically 24 h. The market operator also manages shorter horizon markets for deviations and adjustments. These short-term balancing markets, which are cleared every few hours, generally have a comparatively small economic impact.
Here we focus particularly on the pool operation.

Free bilateral contracting among producers and consumers is usually allowed, provided appropriate information is sent to the market operator in sufficient time. Forward contracts spanning longer time periods (one week to one year) allow both producers and consumers to hedge against the volatility of their respective profits or costs.
Retailers buy energy in the pool and through bilateral and forward contracting to supply their own consumers. As such, retailers face uncertainty from both directions: if buying, from the pool price volatility, and if selling, from the fact that customers might switch to rival retailers.

## MARKET-CLEARING PROCEDURES
For a given set of offers by producers and bids by consumers, a market-clearing procedure is an algorithm used by the market operator to determine (i) accepted offers, (ii) accepted bids, and (iii) clearing prices. These algorithms are auctions of diverse complexity.
Offers by producers are generally considered to be monotonically increasing, while bids by
consumers, monotonically decreasing.

-----

## SINGLE-PERIOD AUCTION
In the single-period auction, a single time period is considered, therefore, neglecting (or oversimplifying) intertemporal coupling. This assumption may result in operating infeasibilities for both producers and consumers. The market operator collects generating offers (increasing in price) by producers and load bids (decreasing in price) by consumers and clears the market by maximizing the social welfare, or declared social welfare if producers/consumers do not submit actual costs/utilities.

A single-period auction can be formulated as:
$$ \max SW^S = \sum_{j=1}^{N_D} \sum_{k=1}^{N_{Dj}} \lambda_{Djk} P_{Djk} - \sum_{i=1}^{N_G} \sum_{b=1}^{N_{Gi}} \lambda_{Gib} P_{Gib} $$
subject to:
$$ 0 \leq P_{Djk} \leq P^{\max}_{Djk} \ \ \ \forall j,k $$
$$ 0 \leq P_{Gib} \leq P^{\max}_{Gib} \ \ \ \forall i,b $$
$$ \sum_{j=1}^{N_D} \sum_{k=1}^{N_{Dj}} P_{Djk} = \sum_{i=1}^{N_G} \sum_{b=1}^{N_{Gi}} P_{Gib} $$

where:
- $SW^S$ : the single-period social welfare (objective function),
- $P_{Djk}$ : the power block $k$ bid by demand $j$ (optimization variable),
- $P_{Gib}$ : the power block $b$ offered by generating unit $i$ (optimization variable),
- $P^{\max}_{Djk}$ : the MW size of block $k$ bid by demand $j$ (constant, given),
- $P^{\max}_{Gib}$ : the MW size of block $b$ offered by generating unit $i$ (constant, given),
- $\lambda_{Djk}$ : the price ($/MWh) of block $k$ bid by demand $j$ (constant, given),
- $\lambda_{Gib}$ : the price ($/MWh) of block $b$ offered by generating unit $i$ (constant, given),
- $N_{Dj}$ : the number of blocks bid by demand $j$,
- $N_{Gi}$ : the number of blocks offered by generating unit $i$,
- $N_D$ : the number of demands,
- $N_G$ : the number of generating units.

### **Example** Single peroiod auction
We consider three generating units and two demands. Each unit offers three blocks, while each demand bids four blocks. The technical characteristics of the generating units are given in the table as follows:

| **Unit data** | **Unit 1** | **Unit 2** | **Unit 3** |
|---------------|------------|------------|------------|
| Capacity (MW) | 30         | 25         | 25         |

Offers by generators and bids by demands are provided in the tables as follow:

| Offers        	| Unit_1 	|   	|    	|     	| Unit_2 	|     	|   	|   	| Unit_3 	|    	|    	|    	|   	|   	|
|---------------	|--------	|---	|----	|-----	|--------	|-----	|---	|---	|--------	|----	|----	|----	|---	|---	|
| Block         	|        	| 1 	| 2  	| 3   	|        	| 1   	| 2 	| 3 	|        	| 1  	| 2  	| 3  	| 4 	|   	|
| Power (MW)    	|        	| 5 	| 12 	| 13  	|        	| 8   	| 8 	| 9 	|        	| 10 	| 10 	| 5  	| 3 	|   	|
| Price ($/MWh) 	|        	| 1 	| 3  	| 3.5 	|        	| 4.5 	| 5 	| 6 	|        	| 8  	| 9  	| 10 	| 3 	|   	|

| Bids          	| Dem_1 	|    	|    	|   	|   	| Dem_2 	|    	|    	|    	|   	|   	|
|---------------	|-------	|----	|----	|---	|---	|-------	|----	|----	|----	|---	|---	|
| Block         	|       	| 1  	| 2  	| 3 	| 4 	|       	| 1  	| 2  	| 3  	| 4 	|   	|
| Power (MW)    	|       	| 8  	| 5  	| 5 	| 3 	|       	| 7  	| 4  	| 4  	| 3 	|   	|
| Price ($/MWh) 	|       	| 10 	| 15 	| 7 	| 4 	|       	| 18 	| 16 	| 11 	| 3 	|   	|

Single period auction can be solved as Linear Programming problem:

> **Degrees of freedom**
> $$P_{Djk}, \forall j,k \ \text{and} \ P_{Gib}, \forall i,b$$

> **Objective function**
> $$\max SW^S = \sum_{j=1}^{N_D} \sum_{k=1}^{N_{Dj}} \lambda_{Djk} P_{Djk} - \sum_{i=1}^{N_G} \sum_{b=1}^{N_{Gi}} \lambda_{Gib} P_{Gib}$$

> **Constraints**
> $$ 0 \leq P_{Djk} \leq P^{\max}_{Djk} \ \ \ \forall j,k $$
> $$ 0 \leq P_{Gib} \leq P^{\max}_{Gib} \ \ \ \forall i,b $$
> $$ \sum_{j=1}^{N_D} \sum_{k=1}^{N_{Dj}} P_{Djk} = \sum_{i=1}^{N_G} \sum_{b=1}^{N_{Gi}} P_{Gib} $$

The solution is: 

![fig 1](/images/2Reading_fig1.png)

If ramping up and ramping down limits for generating units are considered, the constraints below should be added to problem:
$$ P^0_{Gi} - \sum_{b=1}^{N_{Gi}} P_{Gib} \leq R^{\text{down}}_{Gi} \ \ \ \forall i $$
$$ \sum_{b=1}^{N_{Gi}} P_{Gib} - P^0_{Gi} \leq R^{\text{up}}_{Gi} \ \ \ \forall i $$

where:
- $P^0_{Gi}$ is the generating level of unit $i$ just before the auction period,
- $R^{\text{down}}_{Gi}$ and $R^{\text{up}}_{Gi}$ are its ramping down and ramping up limits, respectively.

If minimum and maximum generating levels are imposed on the units, the constraints indicated below should also be added to the problem. Note that in this case a binary variable, $u_i$, is required per generating unit to force the optimization scheme to consider all possible combinations of active power generation limits.

$$ u_i P_{Gi}^{\min} \leq \sum_{b=1}^{N_{Gi}} P_{Gib} \leq u_i P_{Gi}^{\max} \ \ \ \forall i $$
Similarly a minimum demand level can be imposed on any load, that is:
$$ P_{Dj}^{\min} \leq \sum_{k=1}^{N_{Dj}} P_{Djk} \ \ \ \forall j $$

As minimum demands generally need to be supplied, no binary variables are used in the demand constraints. In other words, the demand will always be above its specified minimum value since no binary variable allows the demand to become zero. If the non-continuous constraints are considered, the mixed-integer problem should be solved to calculate the clearing price

-----------
## MULTI-PERIOD AUCTION
In a multi-period auction several time periods (typically 24) are considered simultaneously, in such a way that the intertemporal constraints of the generating units can be taken into account. The objective is to maximize the social welfare of the multi-period market horizon.

The multi-period auction is then formulated as:
> **Degrees of freedom**
> $$P_{Djkt}, \ \forall j,k,t $$
> $$ P_{Gibt}, \ \forall i,b,t$$
> $$ u_{it}, \ \forall i,t$$

> **Objective function**
> $$\max SW^M = \sum_{t=1}^{T} \bigg[  \sum_{j=1}^{N_D} \sum_{k=1}^{N_{Djt}} \lambda_{Djkt} P_{Djkt} - \sum_{i=1}^{N_G} \sum_{b=1}^{N_{Git}} \lambda_{Gibt} P_{Gibt} \bigg]$$

> **Constraints**
> $$ 0 \leq P_{Djkt} \leq P^{\max}_{Djkt} \ \ \ \forall j,k,t $$
> $$ 0 \leq P_{Gibt} \leq P^{\max}_{Gibt} \ \ \ \forall i,b,t $$
> $$ \sum_{j=1}^{N_D} \sum_{k=1}^{N_{Djt}} P_{Djkt} = \sum_{i=1}^{N_G} \sum_{b=1}^{N_{Git}} P_{Gibt} \ \ \ \forall t $$
> $$ \sum_{b=1}^{N_{Gi,t-1}} P_{Gib,t-1} - \sum_{b=1}^{N_{Git}} P_{Gibt} \leq R^{\text{down}}_{Gi} \ \ \ \forall i,t $$
> $$ \sum_{b=1}^{N_{Git}} P_{Gibt} - \sum_{b=1}^{N_{Gi,t-1}} P_{Gib,t-1} \leq R^{\text{up}}_{Gi} \ \ \ \forall i,t $$
> $$ u_{it} P_{Gi}^{\min} \leq \sum_{b=1}^{N_{Git}} P_{Gibt} \leq u_{it} P_{Gi}^{\max} \ \ \ \forall i,t $$
> $$ P_{Dj}^{\min} \leq \sum_{k=1}^{N_{Djt}} P_{Djkt} \ \ \ \forall j,t $$

The objective function is similar to the objective function for single auction, but includes an additional summation over time. It represents the social welfare (or declared social welfare) over the multi-period market horizon, $SW^M$, where:

- $P_{Djkt}$ : the power block $k$ bid by demand $j$ at time $t$ (optimization variable),
- $P_{Gibt}$ : the power block $b$ offered by generating unit $i$ at time $t$ (optimization variable),
- $P^{\max}_{Djkt}$ : the MW size of block $k$ bid by demand $j$ at time $t$ (constant),
- $P^{\max}_{Gibt}$ : the MW size of block $b$ offered by generating unit $i$ at time $t$ (constant),
- $\lambda_{Djkt}$ : the price (\$/MWh) of block $k$ bid by demand $j$ at time $t$ (constant),
- $\lambda_{Gibt}$ : the price (\$/MWh) of block $b$ offered by generating unit $i$ at time $t$ (constant).
- $N_{Djt}$ : the number of blocks bid by demand $j$ at time $t$ (constant),
- $N_{Git}$ : the number of blocks offered by generating unit $i$ at time $t$ (constant).
-$u_{it}$: the status binary variable of unit $i$ at time $t$ (1 if on 0 if off) (optimization variable).
- $P_{Djt}^{\min}$: the minimum load of demand $j$ at time $t$
- $T$: the number of time periods in the auction horizon.

Note that $\sum_{b=1}^{N_Gi0} P_{Gib0}$ is equal to the intial power output of unit $i$.

The problem results in a moderate sized mixed-integer non-linear programming problem that can be easily solved.
