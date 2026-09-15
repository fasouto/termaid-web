"""Re-render every stored diagram output with the installed termaid.

Usage:
    pip install termaid   # the same release the site pulls from PyPI
    python regen.py
"""

import json
from pathlib import Path

from termaid import render

HERE = Path(__file__).parent


def regen(path: Path, entries) -> int:
    changed = 0
    for entry in entries:
        out = render(entry["source"], **entry.get("options", {}))
        if out != entry.get("output"):
            entry["output"] = out
            changed += 1
    return changed


def main() -> None:
    examples_path = HERE / "examples.json"
    gallery_path = HERE / "gallery.json"
    examples = json.loads(examples_path.read_text(encoding="utf-8"))
    gallery = json.loads(gallery_path.read_text(encoding="utf-8"))

    n = regen(examples_path, examples.values())
    examples_path.write_text(json.dumps(examples, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"examples.json: {n} outputs updated")

    n = regen(gallery_path, [item for items in gallery.values() for item in items])
    gallery_path.write_text(json.dumps(gallery, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"gallery.json: {n} outputs updated")


if __name__ == "__main__":
    main()
