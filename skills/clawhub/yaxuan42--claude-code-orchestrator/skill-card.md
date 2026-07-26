## Description: <br>
Orchestrates Claude Code development tasks in observable tmux sessions with startup checks, progress monitoring, completion reports, and OpenClaw wake callbacks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[Yaxuan42](https://clawhub.ai/user/Yaxuan42) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to delegate coding work to Claude Code in tmux, monitor long-running local or SSH sessions, and receive completion reports for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run autonomous Claude Code sessions with broad local or remote execution authority. <br>
Mitigation: Use it only in trusted sandboxes or disposable workspaces, avoid sensitive repositories and secrets, and review scripts before installation. <br>
Risk: The workflow launches Claude Code with permission bypass enabled. <br>
Mitigation: Disable or gate permission bypass where possible and require human review of completion reports, diffs, lint results, build results, and risk summaries before accepting changes. <br>
Risk: Remote SSH execution and proxy settings can affect systems outside the local workspace. <br>
Mitigation: Use only SSH targets and proxy settings you control, and verify any MINI_HOST or proxy configuration before starting a task. <br>
Risk: User-provided lint and build commands are executed in the target workdir. <br>
Mitigation: Provide only lint/build commands you fully control, or leave them empty when verification should be skipped deliberately. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/Yaxuan42/claude-code-orchestrator) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Markdown, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON/Markdown completion reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces tmux session names, attach/status commands, task summaries, and completion report paths.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
