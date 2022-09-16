# CellTrackVis: Interactive Browser-based Visualization for Analyzing Cell Trajectories and Lineages

The code for the official implementation of **CellTrackVis**.
- [Tutorial](https://scbeom.github.io/ctv_tutorial/)
<!-- Detail instructions are described in [Tutorial](doc/tutorial.pdf). -->

## Introduction 

CellTrackVis supports a quick and easy analysis of cell movements with relevant information.
Interconnected views help users effortlessly discover meaningful patterns of cell motions and divisions, and also each component is customizable for various biological tasks.

## Quick Start

**Requirements:** 
- MAC OS, Linux or Windows
- Python 3.7+

**Steps of using CellTrackVis:** 

- Install Python ref to [Download Python](https://www.python.org/downloads/).

- Download the source codes and extract files.

- The directory of CellTrackVis shows the following structure:

```bash
CellTrackVis
    |server.py
    |celltrackvis.html
    |data
      |...
    |images
      |...
    |preprocessors
      |...
```

- Run CelTrackVis server. 

```bash
python server.py
```

- After running the server, CellTrackVis is available on the web browser (e.g., Chrome).

```url
127.0.0.1:8000/celltrackvis.html
```

## License
For academic use, this project is licensed under the GNU Lesser General Public License v3.0 - see the LICENSE file for details. For commercial use, please contact the authors. 
