## Description: <br>
Supervises Claude Code sessions running in tmux with lifecycle hooks, bash pre-filtering, and fast LLM triage to detect errors, stuck agents, and task completion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johba37](https://clawhub.ai/user/johba37) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent harness operators use this skill to supervise long-running Claude Code sessions, detect stuck or completed work, and route actionable notifications. It is intended for monitored automation in trusted coding projects where tmux, Claude Code, and the configured notification backend are available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Background hooks and watchdog scripts can observe terminal state and influence live Claude Code sessions. <br>
Mitigation: Install only in trusted projects, inspect generated hooks before use, and limit supervised sessions to repositories where this level of automation is acceptable. <br>
Risk: Project-local .claude-code-supervisor.yml controls triage and notification commands that execute from the local environment. <br>
Mitigation: Review project-local supervisor configuration as executable code before running hooks or the watchdog. <br>
Risk: Remote LLM or webhook notification backends may receive sensitive repository or terminal context. <br>
Mitigation: Avoid remote triage or notification backends for sensitive repositories, or configure local/private alternatives. <br>
Risk: The watchdog can send automatic tmux input when it detects idle sessions. <br>
Mitigation: Run the watchdog only when automatic tmux nudging is desired and configure idle messages, timeouts, and escalation limits conservatively. <br>


## Reference(s): <br>
- [State Detection Patterns](references/state-patterns.md) <br>
- [Escalation Rules](references/escalation-rules.md) <br>
- [Five Levels from Spicy Autocomplete to the Software Factory](https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON/YAML configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup guidance, hook behavior descriptions, event classifications, and notification patterns for supervised coding sessions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
