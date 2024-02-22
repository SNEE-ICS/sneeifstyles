# SNEE IF Styles

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python Version](https://img.shields.io/pypi/pyversions/sneeifstyles.svg)](https://pypi.org/project/sneeifstyles/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/ambv/black)

SNEE IF Styles is a python package with a light and a dark [`matplotlib`](https://github.com/matplotlib/matplotlib) style.

Line plot style | Distribution plot style
|---------------|----------------------- |
| ![Line plot](https://github.com/SNEE-ICS/sneeifstyles/blob/master/examples/line_plot.png "Line plot") | ![Distribution plot](https://github.com/SNEE-ICS/sneeifstyles/blob/master/examples/distribution_plot.png "Distribution plot") |

## How do I install SNEE IF Styles?

`sneeifstyles` is a Python package. To install it, simply run:


```bash
pip install git+https://github.com/SNEE-ICS/sneeifstyles.git
```

## How do I use SNEE IF Styles?

We are only using the light theme in our SNEE IF styling
To use the light Matplotlib style theme, you can do the following: 

```python
from sneeifstyles import mpl_style

mpl_style()
```

### How do I use SNEE IF Styles in Jupyter Notebooks?

> ⚠️ Please make sure you run `from sneeifstyles import mpl_style` and `mpl_style()` in **code cells** as shown below. 

```python
from sneeifstyles import mpl_style
mpl_style()
```

## What chart types can use SNEE IF Styles?

- Line plots
- Scatter plots
- Bubble plots
- Bar charts
- Pie charts
- Histograms and distribution plots
- 3D surface plots
- Stream plots
- Polar plots

## Can you show me a few examples?

To run the examples in [`example.ipynb`](https://github.com/quantumblacklabs/sneeifstyles/blob/master/example.ipynb), install the required packages using ``pip install -r requirements_notebook.txt`` in a Python virtual environment of your choice.

```python
import matplotlib.pyplot as plt
from sneeifstyles import mpl_style

def plot(dark):
    mpl_style(dark)
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # the following functions are defined in example.ipynb 
    line_plot(axes[0, 0])
    scatter_plot(axes[0, 1])
    distribution_plot(axes[1, 0])
    ax = plt.subplot(2, 2, 4, projection='polar')
    polar_plot(ax)

plot()
```

![png](https://github.com/SNEE-ICS/sneeifstyles/blob/master/examples/sample_plots.png)

```

All of `matplotlibrc`'s options can be found [here](https://matplotlib.org/tutorials/introductory/customizing.html#a-sample-matplotlibrc-file).

## What license do you use?

QB Styles is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
