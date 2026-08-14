# Barcelona Metro Shortest Path Calculator

This project implements a shortest-path calculator for the Barcelona Metro network using graph theory and linear algebra.

The Barcelona Metro network is represented as an undirected graph, where stations are vertices and connections between consecutive stations are edges. The program uses the adjacency matrix of this graph to determine the minimum number of sections that must be travelled between two stations.

The project is based on real data from the TMB Open Data Portal and is implemented in Python using a Jupyter Notebook.

## Mathematical Foundation

The algorithm is based on a property of adjacency matrices.

Given the adjacency matrix `A` of a graph, the element `(i, j)` of `A^k` represents the number of walks of length `k` from vertex `i` to vertex `j`.

The program computes successive powers of the adjacency matrix:

`A, A^2, A^3, ...`

For a given origin station `i` and destination station `j`, the algorithm stops when the corresponding element `(i, j)` becomes non-zero.

The first value of `k` for which this occurs is the minimum number of edges required to travel between the two stations. In the context of the metro network, this corresponds to the route with the minimum number of sections.

This does not necessarily correspond to the fastest route, since travel time can depend on factors such as the length of each section, transfers, waiting times, and other operational conditions.

## Data Source

The data used to build the metro network was obtained from the [TMB Open Data Portal](https://developer.tmb.cat/).

Two CSV files are used:

* `stations.csv` contains the stations in the network and the metro lines associated with each station.
* `metro_lines.csv` contains the connections between consecutive stations for each metro line.

These datasets are processed to construct the graph and its corresponding adjacency matrix.

**Tools & Libraries:**

* Python 3
* NumPy
* Pandas
* Jupyter Notebook

**Concepts Applied:**

* Graph Theory
* Linear Algebra

## Project Structure

The project is contained in a Jupyter Notebook (`.ipynb`) with two main cells.

### 1. Adjacency Matrix Construction

The first cell loads the CSV files, processes the station and line information, assigns an index to each station, and constructs the adjacency matrix `A` representing the Barcelona Metro network.

### 2. Shortest Path Calculation

The second cell contains the route calculation algorithm.

The origin and destination stations can be selected by modifying the following variables:

```python
origin_test = "Mas Blau"
destination_test = "Ciutat Meridiana"

```

After running the cell, the algorithm calculates the minimum number of sections required to travel between the two stations. It also determines the number of distinct walks with that same minimum length.

## Example Output

By setting the variables to the following stations:

```python
origin_test = "Mas Blau"
destination_test = "Ciutat Meridiana"

```

The program repeatedly computes powers of the adjacency matrix until a connection is found. The output will look similar to this:

```text
Origin Station: Mas Blau (ID: 107)
Destination Station: Ciutat Meridiana (ID: 136)
-> The shortest route has a length of: 28 sections (stops).
-> There is/are 2 different path(s) that allow this shortest trip.
```


## Limitations

The algorithm optimizes only the number of sections travelled.

It does not consider:

* Travel time between stations
* Waiting times
* Transfer times
* Service frequency
* Delays or disruptions
* Differences in section length

Therefore, the result should be interpreted as the route with the minimum number of sections rather than the fastest possible journey.

## Purpose

This project was developed to apply concepts from graph theory and linear algebra to a real-world transportation network.

It demonstrates how publicly available transport data can be transformed into a mathematical graph representation and used to solve a shortest-path problem through adjacency matrix operations.