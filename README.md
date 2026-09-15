# termaid.com

Web playground for [termaid](https://github.com/fasouto/termaid). Renders Mermaid diagrams as Unicode text art directly in the browser.

Uses [Pyodide](https://pyodide.org/) to run the Python package client-side via WebAssembly. No backend needed.

## Development

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.


## Updating the examples

The playground installs the latest termaid from PyPI at runtime, but the example outputs in `examples.json` and `gallery.json` are pre-rendered. After a termaid release, re-render them:

```bash
pip install -U termaid
python regen.py
```
