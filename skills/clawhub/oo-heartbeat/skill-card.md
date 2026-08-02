## Description: <br>
Heartbeat (heartbeat.chat). Use this skill for Heartbeat search and read requests through the OOMOL `oo` CLI and the `heartbeat` connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent search and read Heartbeat community data, including users, groups, channels, and events, through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can read Heartbeat community data through the user's connected OOMOL account. <br>
Mitigation: Install only when that data access is acceptable, and keep use limited to the documented get, list, and search actions. <br>
Risk: The allowed `oo` CLI surface is broad enough that future or unintended Heartbeat actions could include writes. <br>
Mitigation: Require explicit user confirmation before any new, write, or destructive Heartbeat action is run. <br>
Risk: Incorrect action payloads can cause failed or unintended connector calls. <br>
Mitigation: Fetch the live connector schema before each action and build payloads to match the current API contract. <br>


## Reference(s): <br>
- [Heartbeat homepage](https://www.heartbeat.chat) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-heartbeat) <br>
- [Publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before actions; expected connector responses are JSON objects with data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
