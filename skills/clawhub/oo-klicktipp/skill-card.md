## Description: <br>
KlickTipp helps an agent operate a connected KlickTipp account through OOMOL using schema-checked connector actions for subscriber list-building workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to run KlickTipp subscriber workflows from an agent without handling raw credentials. It supports creating or updating subscribers, unsubscribing contacts, and removing the configured Listbuilding API tag after checking the live action schema. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill description emphasizes searching and reading, while the documented actions can create, update, unsubscribe, and remove subscriber tags. <br>
Mitigation: Require explicit user confirmation before running signin, signoff, or signout, including the exact email address, payload, and expected subscriber-state change. <br>
Risk: signoff and signout can remove access or tags from contacts and may have business impact if run on the wrong address. <br>
Mitigation: Treat signoff and signout as sensitive operations even when action labels are missing, and verify the target contact before execution. <br>
Risk: Connector action schemas may change independently of the static skill text. <br>
Mitigation: Fetch the live action schema with oo connector schema before constructing each payload. <br>


## Reference(s): <br>
- [KlickTipp skill page](https://clawhub.ai/oomol/skills/oo-klicktipp) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [KlickTipp homepage](https://www.klicktipp.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
