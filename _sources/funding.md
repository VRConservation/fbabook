# Funding Analysis

**Forest, Fire, and Wood Business**
Analysis of CAL FIRE's Business and Workforce Development Grants

Vance Russell | Forest Business Alliance

## Summary
The initial analysis of CAL FIRE's Business and Workforce Development Grants found the following:

- The top 10 grant-receiving counties were Tuolumne, Shasta, Yolo, Placer, Tulare, Siskiyou, Humboldt, Plumas, Fresno, and Mariposa Counties. 
- Every county had projects that requested funds but Merced, Los Angeles, Inyo, Colusa, DelNorte, Orange, Kern, Riverside, Kings, and Monterey counties had not received funding as of November 2023.
- The largest proportion of grants awarded in November 2023 went to Northern California, with 80% going to the North Coast (19%) and Sierra Cascade (61%) regions. The Central Coast (3%) and Southern California (1%) were far behind. The total requested mirrors these percentages by region, although they are slightly higher for the Central Coast (4%) and Southern California (3%).
- The counties with the highest grant success rate (% successfully funded) were Sutter, Stanislaus, San Mateo, Santa Clara, Solano, Siskiyou, Sacramento, Nevada, Mariposa, and Alpine counties. However, a bivariate analysis examining requested and awarded amounts showed that the most successful counties (high amount awarded by the low amount requested) were Ventura, Alpine, San Francisco, Sacramento, and Sutter Counties.
- To increase the analysis accuracy, more precise project location is needed. Further analysis by regions with the most need, e.g., disadvantaged communities, fire probability, or underinvestment, is also needed.

[The Forest Business Alliance](https://www.forestbusinessalliance.org/) provides technical assistance, workshops, and a peer-learning network to increase local and regional capacity for California wood products and forest health. Funding for this project is provided by CAL FIRE's [Business and Workforce Development Grants](https://www.youtube.com/watch?v=ycVSe4K3EZQ).

[CAL FIRE's Wood Products and Bioenergy Program](https://www.fire.ca.gov/what-we-do/natural-resource-management/environmental-protection-program/wood-products-and-bioenergy) manages the BWD grants and works to maintain and enhance California's wood products infrastructure to support healthy, resilient forests and the people and ecosystems that depend on them.

## Fire
Climate change and more than a century of fire suppression have created forced foreste ecosystems well outside their natural conditions. Prior to European settlement, fires were common throughout California, used as a tool for managing food, game, disease, and community safety by Tribal communities with as many as 4 million acres/yr burning throughout the state.

However, in the present, severe wildfires, negatively affecting communities and ecosystems, have burned much of the state in the past several decades (red polygons).

![California](https://i.imgur.com/YHPt5RH.png)

Some areas have burned multiple times. The bright red area southeast of Lake Berryessa, along highway 128, is the most frequently burned area in California.

![Berryessa](https://i.imgur.com/gOJHtS4.png)

In other regions, large wildfires created devastating consequences. The 2018 Camp Fire (pink) killed 85 people and destroyed Paradise. Three years later, the Dixie Fire (red) burned nearly 1 million acres and caused $1.15 billion in damage.

![Dixie](https://i.imgur.com/xu1LKsG.png))

The multitude of fires starting in the early 2000s built a wealth of support for forest health projects to thin unhealthy forest stands and reintroduce fire into forested ecosystems. Those projects created a lot of wood, especially small-diameter wood, without markets. 

CAL FIRE responded by supporting the creation and expansion of wood products and bioenergy businesses and organizations focused on processing this wood. The Forest Business Alliance conducted an initial study on where the funds went to analyze patterns and identify areas of potential future need or funding focus.

## Analysis
The initial funding analysis examined awards by county. The darker green counties indicate a higher amount awarded from CAL FIRE's Business and Workforce Development Grant Program. The total amounts ('000s $USD) are normalized by each county's total square kilometers of forest (total awarded/sq. km forest).

![Awarded_CA](https://i.imgur.com/oeoKMBw.png)

Not surprisingly, the highest grants/square km of forest are in the north state, dominated by Sierra and North Coast counties. Surprisingly, some agriculturally dominant counties rank highly, e.g., Yolo, in part because large bioenergy projects were funded there.

![Northstate](https://i.imgur.com/lWONb8a.png)

Much of Southern California is chaparral and desert, and fire mitigation is focused more on preventing ignition sources. As of autumn 2023, only two counties had projects with funding in Southern California: San Luis Obispo and Ventura (Tulare not considered part of Socal).

![Socal](https://i.imgur.com/eYDXVi5.png)

A bivariate analysis querying the data by total requests and awards paints a slightly different picture than the awards analysis. The bivariate map colors can be interpreted as

white = low requests/low awarded
pink/red = high requests/low awarded
light blue = low requests/high rewarded
light purple = medium requests/medium rewarded
dark purple = high requests/high rewarded

In short, white/pink/red counties had low success rates, and light blue/purple countes had high success rates. Use the slider on the map to compare the awarded counties (left) to success rates in counties to the right.

![Bivariate](https://i.imgur.com/ayd3rHL.png)

The total funding requests and awards by county shows the divide between the northern and southern portions of the state. However, the totals do not explain what may happen across organizations and businesses by region, county, and community. The Forest Business Alliance addresses the lack of capacity in each entity's ability to apply for grants to strengthen sustainable forest businesses and process more wood to ultimately increase forest health across the state.

![chart](chart.png)

## Next
The Forest Business Alliance will continue to add new projects to the Business and Workforce Development database. More precise data will be useful to refine the analysis and start tying funding to change forest health and increase rural economic development. We recommend the following:

- To more accurately reflect where the funding is directed, more specific project locations can be latitude/longitude points.
- Connection from projects supported to acres treated and the CNRA tracking databaseAs more grant rounds are funded, what do the funding and funding success rates look like temporally, and how do they change?
- More analysis is needed to determine the reasons for the county and regional differences. Is it organizational and business capacity? Is it more related to capabilities to create strong projects and proposals? Or could it be something more pervasive, such as regional economics or broader institutional support?

## Data
The proposal data is freely available on CAL FIRE's Wood Products & Bioenergy  website . To conduct the analysis, we removed statewide grants since they could not be placed geographically. For projects covering multiple counties, we averaged the total requests and awards across each county identified for the project. The data was compiled in Excel and then joined to a county spatial (California Tiger Census layer) and a vegetation layer (Calveg) to create the spatial database. For any questions, please contact us at forestbusinessalliance@gmail.com.

### Acknowledgements
Funding for the Forest Business Alliance is provided by the CAL FIRE Business and Workforce Development Grant Program.

```{image} /calfire.png
:height: 300px
:name: vance
```