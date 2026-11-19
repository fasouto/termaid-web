Set Shell "bash"
Set FontSize 14
Set Width 1100
Set Height 820
Set Padding 15
Set Margin 15
Set MarginFill "#d6d3cd"
Set BorderRadius 10
Set WindowBar Colorful
Set TypingSpeed 10ms
Set Framerate 20
Env "PS1" "$ "
Hide
Type "unset $(env | grep -o '^CLAUDE[A-Z_]*') ANTHROPIC_LOG; export PS1='$ '; clear"
Enter
Sleep 500ms
