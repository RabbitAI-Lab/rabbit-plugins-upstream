## Description: <br>
Loop Returns (loopreturns.com). Use this skill for Loop Returns requests that involve searching and reading data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to let an agent inspect Loop Returns return details, return lists, destinations, and destination lookups through an OOMOL-connected Loop Returns account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Loop Returns return, order, and destination information through the connected OOMOL account. <br>
Mitigation: Install and use it only when that account-level read access is intended. <br>
Risk: Future connector actions could include write or destructive behavior even though the current disclosed actions are read-only. <br>
Mitigation: Review the live action schema and require explicit user approval before running any action tagged write or destructive. <br>
Risk: First-time CLI installation and account connection steps change the local tool environment and account access state. <br>
Mitigation: Run setup steps only when an auth, connection, or missing CLI error requires them. <br>


## Reference(s): <br>
- [Loop Returns homepage](https://www.loopreturns.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-loop-returns) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents to inspect live connector schemas before running Loop Returns read actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: skill metadata and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
