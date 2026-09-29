<!-- .gitignore 模板：Go 版。实例化时去掉本注释行，内容原样落盘 .gitignore。 -->

# Binaries
*.exe
*.exe~
*.dll
*.so
*.dylib
{{project_name}}
/bin/

# Test / coverage
*.test
*.out
coverage.html

# Go workspace
go.work
go.work.sum

# Environment
.env
.env.*
!.env.example

# Editor & OS
.vscode/*
!.vscode/extensions.json
.idea/
.DS_Store
Thumbs.db
