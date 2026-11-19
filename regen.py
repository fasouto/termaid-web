"""Re-render every stored diagram output with the installed termaid,
then rebuild the static gallery in examples.html.

Usage:
    pip install termaid   # the same release the site pulls from PyPI
    python regen.py
"""

import json
import re
from html import escape
from pathlib import Path
from urllib.parse import quote

from termaid import render

HERE = Path(__file__).parent

SECTIONS = [
    ("Core", [
        ("flowchart", "Flowchart", "Decision trees, process flows, and directed graphs"),
        ("sequence", "Sequence", "Message exchanges between participants over time"),
        ("class", "Class", "Object-oriented class hierarchies and relationships"),
        ("er", "ER Diagram", "Entity-relationship models for databases"),
        ("state", "State Diagram", "State machines with transitions and conditions"),
    ]),
    ("Charts", [
        ("gantt", "Gantt", "Project schedules with tasks, sections, and dependencies"),
        ("pie", "Pie Chart", "Proportional data as labeled slices"),
        ("xychart", "XY Chart", "Bar charts, line charts, and combinations"),
        ("quadrant", "Quadrant Chart", "2x2 grids with plotted data points"),
    ]),
    ("Other", [
        ("architecture", "Architecture", "Service groups with directional connections"),
        ("block", "Block", "Grid-based block layouts"),
        ("git", "Git Graph", "Branch and merge histories"),
        ("treemap", "Treemap", "Hierarchical data as nested rectangles"),
        ("mindmap", "Mindmap", "Radial idea maps branching from a root"),
        ("journey", "User Journey", "Task timelines with satisfaction scores"),
        ("packet", "Packet", "Bit-aligned network protocol layouts"),
        ("timeline", "Timeline", "Chronological event lists with details"),
        ("kanban", "Kanban", "Column-based task boards with cards"),
    ]),
]

GALLERY_MARKERS = re.compile(r"(<!-- gallery:start -->\n).*?(<!-- gallery:end -->)", re.S)


def regen(entries) -> int:
    changed = 0
    for entry in entries:
        out = render(entry["source"], **entry.get("options", {}))
        if out != entry.get("output"):
            entry["output"] = out
            changed += 1
    return changed


def card_html(ex) -> str:
    try_href = "/?src=" + quote(ex["source"], safe="-_.!~*'()")
    return (
        '<div class="diagram-card"><div class="diagram-card-inner">'
        '<div class="diagram-source"><div class="diagram-source-header">'
        '<div class="diagram-source-label">Mermaid</div>'
        f'<a class="try-link" href="{escape(try_href)}">Try it &rarr;</a></div>'
        f'<pre>\n{escape(ex["source"], quote=False)}</pre></div>'
        f'<div class="diagram-output"><pre>\n{escape(ex["output"], quote=False)}</pre></div>'
        "</div></div>"
    )


def gallery_html(gallery) -> str:
    sidebar, content = [], []
    for title, items in SECTIONS:
        links = "".join(f'<a href="#{key}">{escape(label)}</a>' for key, label, _ in items)
        sidebar.append(f'<div class="sidebar-group"><div class="sidebar-group-title">{title}</div>{links}</div>')
        for key, label, desc in items:
            examples = gallery.get(key) or []
            if not examples:
                continue
            parts = [f'<section class="diagram-section" id="{key}">',
                     f"<h2>{escape(label)}</h2>", f'<p class="desc">{escape(desc)}</p>']
            for ex in examples:
                if len(examples) > 1:
                    parts.append(f'<h3 class="variation-label">{escape(ex["title"])}</h3>')
                    parts.append(f'<p class="variation-desc">{escape(ex["desc"])}</p>')
                parts.append(card_html(ex))
            parts.append("</section>")
            content.append("\n".join(parts))
    return (
        '<nav class="sidebar">' + "".join(sidebar) + "</nav>\n"
        '<div class="content">\n' + "\n".join(content) + "\n</div>"
    )


def main() -> None:
    examples_path = HERE / "examples.json"
    gallery_path = HERE / "gallery.json"
    page_path = HERE / "examples.html"
    examples = json.loads(examples_path.read_text(encoding="utf-8"))
    gallery = json.loads(gallery_path.read_text(encoding="utf-8"))

    n = regen(examples.values())
    examples_path.write_text(json.dumps(examples, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"examples.json: {n} outputs updated")

    n = regen([item for items in gallery.values() for item in items])
    gallery_path.write_text(json.dumps(gallery, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"gallery.json: {n} outputs updated")

    page = page_path.read_text(encoding="utf-8")
    page, found = GALLERY_MARKERS.subn(lambda m: m.group(1) + gallery_html(gallery) + "\n" + m.group(2), page)
    if found != 1:
        raise SystemExit("examples.html: gallery markers not found")
    page_path.write_text(page, encoding="utf-8")
    print("examples.html: gallery rebuilt")


if __name__ == "__main__":
    main()
