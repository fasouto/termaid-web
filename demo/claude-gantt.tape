Output ../img/claude-gantt.gif
Source setup.tape
Type "cd ~/projects_work/termaid-web/demo/sample-app && clear"
Enter
Sleep 500ms
Type "claude --permission-mode default"
Enter
Sleep 5s
Show
Type "Plan a 6 week v2 launch for this service as a mermaid gantt chart with 3 sections. Just the diagram."
Sleep 500ms
Enter
Wait+Screen@240s /done \d+:\d\d/
Sleep 3s
