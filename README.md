# termaid.com

Web playground for [termaid](https://github.com/fasouto/termaid). Renders Mermaid diagrams as Unicode text art directly in the browser.

Uses [Pyodide](https://pyodide.org/) to run the Python package client-side via WebAssembly. No backend needed.

## Development

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.


## Updating the examples

The playground installs the latest termaid from PyPI at runtime, but the example outputs in `examples.json` and `gallery.json` are pre-rendered, and `examples.html` is static HTML built from `gallery.json`. After a termaid release, or after editing `gallery.json`, re-render them:

```bash
pip install -U termaid
python regen.py
```

## Recording the Claude Code GIFs

The GIFs on `claude-code.html` are real Claude Code sessions recorded with [VHS](https://github.com/charmbracelet/vhs). They need `termaid` on your PATH and the termaid plugin installed. Each run talks to Claude, so the output changes between recordings.

```bash
cd demo
vhs claude-sequence.tape   # writes ../img/claude-sequence.gif
```

`demo/record-all.sh` records every tape, one at a time. The termaid hook sometimes leaves a diagram as Mermaid source, so check the last frame of each GIF before committing it.
