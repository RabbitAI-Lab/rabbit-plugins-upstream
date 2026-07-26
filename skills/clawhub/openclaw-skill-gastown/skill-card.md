## Description: <br>
Openclaw Skill Gastown guides an agent in using Gas Town and Claude Code to coordinate multi-agent coding work with persistent work tracking, supervised worker sessions, and merge workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[saesak](https://clawhub.ai/user/saesak) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering teams use this skill to delegate non-trivial coding tasks to a Gas Town workspace, where agents can break work into tracked units, dispatch parallel workers, monitor progress, and process merges. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can start persistent local AI coding sessions and automated workers. <br>
Mitigation: Use it only in repositories where automated workers are acceptable, and monitor active sessions and work queues. <br>
Risk: The skill can modify repositories and process merges through delegated agents. <br>
Mitigation: Require human review of generated changes and merge decisions before accepting them into protected branches. <br>
Risk: Setup steps install command-line tools and may alter shell configuration or local workspace state. <br>
Mitigation: Review setup commands before execution and prefer pinned or verified tool versions. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/saesak/skills/openclaw-skill-gastown) <br>
- [Publisher profile](https://clawhub.ai/user/saesak) <br>
- [Gas Town Architecture](references/architecture.md) <br>
- [Gas Town GitHub](https://github.com/steveyegge/gastown) <br>
- [Beads GitHub](https://github.com/steveyegge/beads) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May lead an agent to start local coding sessions, modify repositories, create persistent work state, and process merges.] <br>

## Skill Version(s): <br>
0.1.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
