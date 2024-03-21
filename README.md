# Python Pen Plotting Template

Template for creating generative art for pen plotters, powered by [svg.py](https://pypi.org/project/svg.py/)

## Usage

Install dependencies and start a static server:

```bash
poetry install
python3 -m http.server 8000
```

Then generate the SVG file:

```bash
poetry run task draw
```

Open a browser to http://localhost:8000 to see the results.
