Output ../img/claude-repo.gif
Source setup.tape
Type "cd /Users/fabio/projects_work/termaid && clear"
Enter
Sleep 500ms
Type "claude --permission-mode default"
Enter
Sleep 5s
Show
Type "How does termaid --claude-hook handle a reply? Answer with a mermaid flowchart of at most 10 nodes and one sentence."
Sleep 500ms
Enter
Wait+Screen@300s /done \d+:\d\d/
Sleep 3s
