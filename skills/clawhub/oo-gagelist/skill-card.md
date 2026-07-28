## Description: <br>
GageList enables an agent to read and manage data in a connected GageList account through OOMOL's `oo` CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users with connected OOMOL and GageList accounts use this skill to retrieve account, gage, calibration, and manufacturer records and to manage manufacturer data after confirming state-changing actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can change manufacturer data in the connected GageList account. <br>
Mitigation: Confirm the exact payload and intended effect with the user before running create or update actions. <br>
Risk: Destructive actions can delete manufacturer records from the connected GageList account. <br>
Mitigation: Confirm the target record and obtain explicit approval before running delete actions. <br>
Risk: Connector payload fields may change over time. <br>
Mitigation: Inspect the live connector schema before constructing or running each action payload. <br>


## Reference(s): <br>
- [ClawHub GageList skill page](https://clawhub.ai/oomol/skills/oo-gagelist) <br>
- [GageList homepage](https://gagelist.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands inspect the live connector schema before execution and return connector responses as JSON when actions are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
