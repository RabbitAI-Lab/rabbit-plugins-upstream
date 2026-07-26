## Description: <br>
Generates ready-to-run automation loop commands for Claude Code, Gemini CLI, or Grok CLI across PowerShell, Windows CMD, and Bash/Linux. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[walkamolee](https://clawhub.ai/user/walkamolee) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and CLI users use this skill to create copy-pasteable loop commands that repeatedly run an AI CLI against PROMPT.md with selected model, shell, iteration, delay, time-limit, and stop-file controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated loop commands can repeatedly run agentic CLI tools with approval-bypass or auto-approve flags. <br>
Mitigation: Inspect generated commands before execution, remove bypass flags unless they are deliberately needed, and test in a version-controlled or disposable workspace. <br>
Risk: PROMPT.md contents are passed to the selected AI CLI and may contain sensitive data. <br>
Mitigation: Keep secrets and confidential data out of PROMPT.md and verify the destination CLI and model before running the command. <br>
Risk: Infinite or long-running loops may continue making changes or consuming API quota. <br>
Mitigation: Prefer fixed iteration limits, time limits, delays, and stop files, and monitor the loop while it runs. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/walkamolee/skills/ralph-loop-writer) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Timestamped Markdown file containing a shell-specific command block and run/stop instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates ralphcommand-YYYY-MM-DD-HHMMSS.md in the current directory; generated commands may include approval-bypass or auto-approve flags depending on the selected CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
