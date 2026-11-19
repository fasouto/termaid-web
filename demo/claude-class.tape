Output ../img/claude-class.gif
Source setup.tape
Type "cd ~/projects_work/termaid-web/demo/sample-app && clear"
Enter
Sleep 500ms
Type "claude --permission-mode default"
Enter
Sleep 5s
Show
Type "Draw a mermaid class diagram of models.py. Just the diagram."
Sleep 500ms
Enter
Wait+Screen@240s /done \d+:\d\d/
Sleep 3s
