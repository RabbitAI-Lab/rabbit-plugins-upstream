## Description: <br>
Structured session lifecycle for Claude Code — start, checkpoint, end, and daily heartbeat commands that maintain project state across conversations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[conorbronsdon](https://clawhub.ai/user/conorbronsdon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Claude Code users use this skill to preserve project context across conversations with start, checkpoint, close, and daily check-in workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can persist plain-text session history and project state that may include sensitive information. <br>
Mitigation: Install only where plain-text state files are acceptable, and redact secrets, access tokens, private customer data, legal or HR details, and confidential discussion content. <br>
Risk: Incorrect or stale summaries could carry misleading project context into later sessions. <br>
Mitigation: Review generated summaries, state updates, and memory proposals before accepting them; the skill is user-triggered and documents confirmation steps for durable updates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/conorbronsdon/skills/session-management) <br>
- [agent-workspace canonical home](https://github.com/conorbronsdon/agent-workspace) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and state-file templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces user-facing briefings, checkpoints, session summaries, state-file updates, and memory proposals when invoked.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
