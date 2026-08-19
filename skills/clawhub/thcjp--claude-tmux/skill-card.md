## Description:

Claude终端复用工具 is an instruction-only tmux assistant for managing local tmux sessions, windows, and related command workflows through an agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to ask an AI agent for tmux session and window management, command workflow support, and troubleshooting on a local machine. It is suited to explicit terminal multiplexing tasks, not autonomous or sensitive session changes without review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad tmux and command-execution authority could disrupt active sessions, files, credentials, or running processes.

Mitigation: Use the skill only for explicit tmux management tasks and require confirmation before close, kill, rename, switch, copy, paste, or command execution.

Risk: The release security verdict is suspicious because the instructions grant broad authority without clear operational safeguards.

Mitigation: Review and scan the skill before installation, then run it with least-privilege access in a constrained agent environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/claude-tmux)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-like status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or execute tmux-related session, window, copy, paste, and command operations when the host agent grants the required tools.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
