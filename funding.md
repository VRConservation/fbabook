# Funding Analysis

**Forests and Business**: An Analysis of CAL FIRE's Business and Workforce Development Grants

Forest Business Alliance

## Summary
To better understand the geographic distribution, success rates, and funding gaps/needs, [The Forest Business Alliance](https://www.forestbusinessalliance.org/) undertook a preliminary study examining CAL FIRE's Business and Workforce Development Grants. The initial analysis of CAL FIRE's Business and Workforce Development Grants found the following:

- The funding requests or needs far outstrip the grant funds awarded.
- The top 10 grant-receiving counties were Tuolumne, Shasta, Yolo, Placer, Tulare, Siskiyou, Humboldt, Plumas, Fresno, and Mariposa Counties. 
- Every county had projects that requested funds, but Merced, Los Angeles, Inyo, Colusa, DelNorte, Orange, Kern, Riverside, Kings, and Monterey counties had not received funding as of November 2023.
- The largest proportion of grants awarded in November 2023 went to Northern California, with 80% going to the North Coast (19%) and Sierra Cascade (61%) regions. The Central Coast (3%) and Southern California (1%) were far behind. The total requested mirrors these percentages by region, although they are slightly higher for the Central Coast (4%) and Southern California (3%).
- The counties with the highest grant success rate (% successfully funded) were Sutter, Stanislaus, San Mateo, Santa Clara, Solano, Siskiyou, Sacramento, Nevada, Mariposa, and Alpine counties. However, a bivariate analysis examining requested and awarded amounts showed that the most successful counties (high amount awarded by the low amount requested) were Ventura, Alpine, San Francisco, Sacramento, and Sutter Counties.
- To increase the analysis accuracy, a more precise project location is needed. Further analysis by regions with the most need, e.g., disadvantaged communities, fire probability, or underinvestment, is also needed.

## Fire
Climate change and more than a century of fire suppression have created forced forest ecosystems well outside their natural conditions. Before European settlement, fires were common throughout California and were used as a tool for managing food, game, disease, and community safety by Tribal communities. Approximately 4.4 million acres burned annually in California prior to 1800 {cite}`stephens_etal_2007`.

However, in the present, severe wildfires, negatively affecting communities and ecosystems, have burned much of the state in the past several decades ({numref}`california`).

```{figure} /figures/california.png
:name: california
California Fires 1878-2022 (CAL FIRE FRAP). 
```

Some areas have burned multiple times. The bright red area southeast of Lake Berryessa, along Highway 128, is the most frequently burned area in California ({numref}`berryessa`).

```{figure} /figures/berryessa.png
:name: berryessa
Coast Range fires near Lake Berryessa, east of Sacramento. 
```

In other regions, large wildfires created devastating consequences({numref}`dixie`). The 2018 Camp Fire (pink) killed 85 people and destroyed Paradise. Three years later, the Dixie Fire (red) burned nearly 1 million acres and caused $1.15 billion in damage {cite}`camp,dixie`.

```{figure} /figures/dixie.png
:name: dixie
Camp (pink) and Dixie (red) fires. 
```

The preponderance of large fires in the early 2000s built a wealth of support for forest health projects to thin unhealthy forest stands and reintroduce fire into forested ecosystems. Those projects created a lot of wood, especially small-diameter wood, without markets. 

CAL FIRE responded by creating the Wood Products and Bioenergy Program with the first grants awarded in 2022. The Forest Business Alliance conducted an initial study on where the funds went to analyze patterns and identify areas of potential future need or funding focus.

## Analysis
The initial funding analysis examined awards by county from the 1st quarter of 2022 to the 3rd quarter of 2023 ({numref}`awarded_ca`). The darker green counties indicate a higher amount awarded from CAL FIRE's Business and Workforce Development Grant Program. The total amounts (1,000s $USD) are normalized by each county's total square kilometers of forest (total awarded/sq. km forest).

### Awarded
```{figure} /figures/awarded_ca.png
:name: awarded_ca
Awarded grants by California County. Numbers in thousands $USD. 
```

Not surprisingly, the highest grants/square km of forest are in the north state, dominated by the Sierra Nevada and North Coast counties ({numref}`norcal`). Surprisingly, some agriculturally dominant counties rank highly, e.g., Yolo, in part because large bioenergy projects were funded there.

```{figure} /figures/norcal.png
:name: norcal
Grant concentrations in Northern California. 
```

As of autumn 2023, only two counties had projects with funding in Southern California: San Luis Obispo and Ventura ({numref}`socal`). Much of Southern California is chaparral and desert, and fire mitigation is focused more on preventing ignition sources rather than thinning forests and processing sawlogs or biomass.

```{figure} /figures/socal.png
:name: socal
Grant concentrations in Southern California. Note: Tulare is not considered part of the Socal region.
```

### Bivariate
A bivariate analysis querying the data by total requests and awards paints a slightly different picture than the awards analysis ({numref}`biv`). Where the success rate is the value of funded/requested grants, the lightest shades tend to indicate low success rates, whereas the light blue to dark purple indicate counties with high grant success rates.

```{figure} /figures/biv.png
:name: biv
Bivariate analysis comparing amounts of requested to awarded grants simultaneously.
```

### Gaps
The total funding requests and awards by county show the divide between the northern and southern portions of the state({numref}`chart`). The large number of grants requested and awarded in the Sierra Cascade Region. However, the totals do not explain what may happen across organizations and businesses by region, county, and community. The Forest Business Alliance addresses the lack of capacity in each entity's ability to apply for grants to strengthen sustainable forest businesses and process more wood to ultimately increase forest health across the state.

```{figure} /figures/chart.png
:name: chart
Stacked bar chart of requested and awarded grants by Wildfire Task Force Region and county.
```

Funding by project type showed the most funding for workforce development training, biomass, transportation, and equipment projects ({numref}`type`). Business development, marketing, and thinning projects were the least funded project types.

```{figure} /figures/type.png
:name: type
:height: 300px
Awarded grants by project type.
```
The number of unfunded projects by county reveals interesting patterns ({numref}`nofund`). Many of the applicants that were not funded are located in Northern California, largely from the Sierra Cascade counties.

```{figure} /figures/nofund.png
:name: nofund
:height: 300px
Unfunded requests by California County.
```

## Next
The Forest Business Alliance will continue to add new projects to the Business and Workforce Development funding analysis database as applications are submitted and awards granted. More precise data will be useful to refine the analysis and start tying funding to change forest health and increase rural economic development. We recommend the following:

- More accurate project locations, e.g., latitude/longitude points should be added to reflect where the funding is directed.
- As more projects are funded through subsequent grant rounds how do the funding success rates change geographically?
- More analysis is needed to determine the reasons for the county and regional differences. Is it organizational and business capacity? Is it more related to capabilities to create strong projects and proposals? Or could it be something more pervasive, such as regional economics or broader institutional support?
- Given the need for wildfire mitigation in the state, the bottleneck of processing biomass in a sustainable manner, and the mismatch in requested vs. funded businesses, we highly recommend the state consider increasing funding for this valuable program.

## Data
The proposal data is freely available on CAL FIRE's Wood Products & Bioenergy website. To conduct the analysis, we removed statewide grants since they could not be placed geographically. For projects covering multiple counties, we averaged the total requests and awards across each county identified for the project. The data was compiled in Excel and then joined to a county spatial (California Tiger Census layer) and a vegetation layer (Calveg) to create the spatial database. For any questions, please contact us at forestbusinessalliance@gmail.com.

## Acknowledgements
Funding for the Forest Business Alliance is provided by the CAL FIRE Business and Workforce Development Grant Program. [CAL FIRE's Wood Products and Bioenergy Program](https://www.fire.ca.gov/what-we-do/natural-resource-management/environmental-protection-program/wood-products-and-bioenergy) manages the BWD grants and works to maintain and enhance California's wood products infrastructure to support healthy, resilient forests and the people and ecosystems that depend on them.

[The Forest Business Alliance](https://www.forestbusinessalliance.org/) provides technical assistance, workshops, and a peer-learning network to increase local and regional capacity for California wood products and forest health. Funding for this project is provided by CAL FIRE's [Business and Workforce Development Grants](https://www.youtube.com/watch?v=ycVSe4K3EZQ).

```{image} /calfire.png
:height: 200px
:name: calfire
```