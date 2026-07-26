## Description: <br>
macOS截图工具免费版 helps users create screenshots and basic screen recordings on macOS with native screencapture shell commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individual macOS users and developers use this skill to capture screenshots or basic screen recordings for bug reports, operation walkthroughs, and screen-content archiving. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can capture sensitive on-screen content through screenshots or recordings. <br>
Mitigation: Close or mask confidential windows, avoid recording credential entry, and review saved files before sharing. <br>
Risk: The skill relies on command execution for macOS screen capture workflows and should not activate for unrelated tasks. <br>
Mitigation: Invoke it only for explicit capture requests and review proposed screencapture commands before execution. <br>
Risk: Saved screenshots and recordings may persist on local disk after the task is complete. <br>
Mitigation: Use intended output directories, remove unneeded captures, and prefer clipboard-only capture for temporary screenshots. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/mac-node-snapshot-tool-free) <br>
- [Source artifact SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Code, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and JSON result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save screenshots or recordings to local macOS paths or copy screenshots to the clipboard.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
