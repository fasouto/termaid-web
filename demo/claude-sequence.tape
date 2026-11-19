Output ../img/claude-sequence.gif
Source setup.tape
Type "cd /Users/fabio/projects_work/termaid/demo && clear"
Enter
Sleep 500ms
Type "claude --permission-mode default"
Enter
Sleep 5s
Show
Type "Draw the OAuth login flow as a mermaid sequence diagram with three participants. Just the diagram."
Sleep 500ms
Enter
Wait+Screen@120s /done \d+:\d\d/
Sleep 3s
