## Description: <br>
SupportBee helps agents operate a connected SupportBee account through OOMOL to read, create, update, and delete support-desk data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Support teams and developers use this skill to inspect SupportBee connector schemas and run OOMOL connector actions for tickets, labels, teams, users, and customer groups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write and destructive SupportBee actions can change support-desk records, including tickets, replies, comments, users, and labels. <br>
Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write or destructive actions. <br>
Risk: The skill operates a connected SupportBee account through OOMOL, so actions may affect real customer-support data. <br>
Mitigation: Install and use it only for accounts where agent operation through OOMOL is intended, and prefer read-only actions unless a change is explicitly requested. <br>


## Reference(s): <br>
- [SupportBee Skill Page](https://clawhub.ai/oomol/skills/oo-supportbee) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [SupportBee Homepage](https://supportbee.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector action responses are JSON objects with data and meta.executionId when actions run.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
