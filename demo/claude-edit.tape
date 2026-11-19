Output ../img/claude-edit.gif
Source setup.tape
Type "cd ~/projects_work/termaid-web/demo/sample-app && clear"
Enter
Sleep 500ms
Type "claude --permission-mode default"
Enter
Sleep 5s
Show
Type "Draw the checkout flow of this service as a mermaid flowchart, at most 6 nodes. Just the diagram."
Sleep 500ms
Enter
Wait+Screen@240s /done \d+:\d\d/
Sleep 4s
Type "Add a step that retries a failed payment once. Just the diagram."
Sleep 500ms
Enter
Sleep 30s
Sleep 3s
