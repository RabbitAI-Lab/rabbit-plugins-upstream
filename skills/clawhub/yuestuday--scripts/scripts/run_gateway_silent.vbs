' OpenClaw Gateway - Silent Launcher
' Runs gateway.cmd with a fully hidden window (no cmd/conhost popup).
' Keeps wscript.exe alive while the gateway runs.
' Exits with non-zero code when the gateway stops, so Task Scheduler's
' RestartOnFailure policy can bring it back.
Option Explicit
Dim shell, fso, exitCode
Set shell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

Dim cmdPath
cmdPath = fso.GetParentFolderName(WScript.ScriptFullName) & "\gateway.cmd"

' 0 = hidden window, True = wait for completion
exitCode = shell.Run("""" & cmdPath & """", 0, True)

' Gateway process ended -> signal failure so the task restarts it.
WScript.Quit(1)
