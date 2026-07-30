## Description: <br>
This skill enables agents to operate a Respond.io workspace through OOMOL's respond_io connector for reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to let an agent inspect contacts, channels, users, and conversations and perform approved contact or conversation changes in a connected Respond.io workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change Respond.io account data through write actions. <br>
Mitigation: Confirm the exact payload and effect with the user before running write actions. <br>
Risk: Destructive actions can delete contacts or remove tags. <br>
Mitigation: Confirm the target and obtain explicit user approval before running destructive actions. <br>
Risk: Payloads can be incorrect if an action schema is assumed instead of checked. <br>
Mitigation: Inspect the live action schema with oo connector schema before constructing an action payload. <br>


## Reference(s): <br>
- [Respond.io homepage](https://respond.io/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Text] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector action responses are JSON objects containing data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
