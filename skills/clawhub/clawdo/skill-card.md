## Description: <br>
Todo list and task management for AI agents, with persistent SQLite storage, autonomy levels, heartbeat and cron workflows, and structured JSON CLI output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lepetitpince](https://clawhub.ai/user/lepetitpince) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to let agents capture, review, prioritize, and complete queued tasks across conversations, heartbeat loops, cron jobs, and non-interactive automation. It is intended for agent task tracking where humans approve proposed work and autonomy levels constrain unattended execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A global npm CLI with persistent local task storage may retain task content across sessions. <br>
Mitigation: Install only in environments where local persistent task queues are acceptable, and avoid adding credentials, private data, or sensitive account details to tasks. <br>
Risk: Unattended heartbeat or cron execution can act on queued tasks without immediate human review. <br>
Mitigation: Limit unattended use to pre-approved, low-risk work and require human review for production systems, accounts, money, credentials, public content, or private data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lepetitpince/skills/clawdo) <br>
- [Project homepage](https://github.com/LePetitPince/clawdo) <br>
- [npm package](https://www.npmjs.com/package/clawdo) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown] <br>
**Output Format:** [Markdown with inline shell commands and JSON-oriented CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the clawdo CLI binary; CLI commands support structured JSON output.] <br>

## Skill Version(s): <br>
1.1.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
