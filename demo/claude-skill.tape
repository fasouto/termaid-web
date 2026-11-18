Output ../img/claude-skill.gif
Source setup.tape
Type "cd ~/projects_work/termaid-web/demo/sample-app && clear"
Enter
Sleep 500ms
Type "claude --permission-mode auto"
Enter
Sleep 5s
Show
Type "/termaid:mermaid show the diagrams in README.md"
Sleep 500ms
Enter
Wait+Screen@180s /done \d\d:\d\d/
Sleep 6s
