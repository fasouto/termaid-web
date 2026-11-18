Output ../img/claude-er.gif
Source setup.tape
Type "cd ~/projects_work/termaid-web/demo/sample-app && clear"
Enter
Sleep 500ms
Type "claude --permission-mode auto"
Enter
Sleep 5s
Show
Type "Draw an ER diagram of schema.sql as mermaid. Just the diagram."
Sleep 500ms
Enter
Wait+Screen@240s /done \d\d:\d\d/
Sleep 4s
