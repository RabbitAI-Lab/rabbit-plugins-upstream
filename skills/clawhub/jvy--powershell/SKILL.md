---
name: powershell
description: Prevent file-writing via Windows PowerShell to avoid GBK encoding corruption. Use when Kimi Code CLI is running on Windows and the task involves creating, writing, or modifying text files, especially when content contains Chinese or other non-ASCII characters.
---

# Avoid PowerShell GBK Encoding Issues

On Chinese Windows systems, the PowerShell console and redirection operators (`>`, `>>`) often use the system default encoding (GBK / code page 936). Writing UTF-8 text through PowerShell can silently corrupt Chinese characters into garbled text.

## Prohibited practices

Do **not** use PowerShell to write or overwrite files:

- `echo "..." > file.txt`
- `echo "..." >> file.txt`
- `Set-Content file.txt "..."`
- `Out-File file.txt` without explicit `-Encoding UTF8`
- Any other PowerShell command that creates or modifies file bytes indirectly

These methods are unreliable because encoding defaults vary by locale and PowerShell version.

## Preferred approach

Always use the dedicated file tools:

- `WriteFile` for creating or overwriting files
- `StrReplaceFile` for editing existing files

These tools write UTF-8 deterministically and avoid shell encoding pitfalls.

## When Shell is unavoidable

If a script or command must write files through PowerShell, force UTF-8 explicitly:

```powershell
"content" | Out-File -FilePath "file.txt" -Encoding UTF8
```

Or use .NET directly:

```powershell
[System.IO.File]::WriteAllText("file.txt", "content", [System.Text.Encoding]::UTF8)
```

Always verify the produced file is readable and not garbled before finishing.

## Verify encoding

Check the active console code page:

```powershell
chcp
```

If it returns `936`, PowerShell redirection is especially unsafe for UTF-8 content. Fall back to file tools.
