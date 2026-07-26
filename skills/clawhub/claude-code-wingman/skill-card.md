## Description: <br>
Claude Code Wingman orchestrates multiple Claude Code sessions across projects and lets users monitor and control them from WhatsApp. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yossiovadia](https://clawhub.ai/user/yossiovadia) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and technical users use this skill to delegate coding tasks to Claude Code sessions, monitor progress, and approve or deny tool actions from WhatsApp or chat. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote Claude Code orchestration and auto or always approval flows can allow high-impact actions with limited human review. <br>
Mitigation: Use the skill only when remote orchestration is intended; prefer manual approval, avoid auto or always approvals on sensitive repositories or production systems, and review each approval prompt before allowing it. <br>
Risk: Sessions operate in user-selected working directories and can run shell commands through Claude Code. <br>
Mitigation: Restrict target directories to appropriate projects, avoid sessions containing secrets, and attach to or monitor tmux sessions when tasks affect important code or systems. <br>
Risk: WhatsApp approval handling depends on webhook configuration and temporary state files. <br>
Mitigation: Review webhook token, phone allow-list, and /tmp state handling before use; keep notification configuration limited to trusted recipients. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yossiovadia/skills/claude-code-wingman) <br>
- [Publisher profile](https://clawhub.ai/user/yossiovadia) <br>
- [ClawdHub skill listing from artifact docs](https://clawdhub.com/skills/claude-code-wingman) <br>
- [Clawdbot dashboard](https://clawd.bot) <br>
- [Claude Code Wingman GitHub link from artifact docs](https://github.com/yossiovadia/claude-code-wingman) <br>
- [Claude Code Orchestrator GitHub link from artifact docs](https://github.com/yossiovadia/claude-code-orchestrator) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and optional JSON status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can start, monitor, and control long-running tmux sessions for Claude Code when required dependencies are present.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
