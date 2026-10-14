' OpenClaw Gateway - Hidden launcher (does not wait)
Option Explicit
Dim shell, fso, cmdPath
Set shell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
cmdPath = fso.GetParentFolderName(WScript.ScriptFullName) & "\gateway.cmd"
shell.Run """" & cmdPath & """", 0, False
