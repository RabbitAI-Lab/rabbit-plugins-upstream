## Description: <br>
Coordinates Claude agent teams via filesystem protocol. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to coordinate multiple Claude CLI agents on parallel implementation, review, refactoring, testing, and task handoff workflows. It is most relevant when work can be split across agents and coordinated through explicit tasks, messages, roles, and health checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Team task and message history may be stored in plaintext local files. <br>
Mitigation: Avoid putting secrets, credentials, or sensitive data in task descriptions, team messages, or local coordination files. <br>
Risk: The skill can launch and manage multiple local Claude agents. <br>
Mitigation: Use it only in repositories where parallel agent work is acceptable, and review team formation, task ownership, and agent roles before starting work. <br>
Risk: Stalled-agent recovery may terminate or replace local agent panes. <br>
Mitigation: Review team deletion, pane-kill, restart, and replacement actions before allowing them to run. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-conjure-agent-teams) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/athola) <br>
- [Clawdis Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conjure) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces coordination patterns for local agent teams, including task files, inbox messages, team configuration, role routing, and health-monitoring guidance.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
