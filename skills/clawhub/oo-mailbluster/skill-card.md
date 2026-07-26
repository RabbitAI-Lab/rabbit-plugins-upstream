## Description: <br>
MailBluster helps agents read, create, update, and delete MailBluster data through the OOMOL oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage MailBluster leads and custom fields through an OOMOL-connected account. It supports routine lead lookup as well as carefully reviewed create, update, and delete actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can modify MailBluster lead data. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running create or update actions. <br>
Risk: Destructive actions can delete lead records. <br>
Mitigation: Confirm the target lead and obtain explicit user approval before running delete actions. <br>
Risk: Broad account access could expose more MailBluster data than needed for a task. <br>
Mitigation: Use a MailBluster account with only the access needed for the intended work. <br>
Risk: Incorrect payloads can produce unintended changes. <br>
Mitigation: Fetch the live connector schema before constructing action payloads. <br>


## Reference(s): <br>
- [ClawHub MailBluster Skill](https://clawhub.ai/oomol/skills/oo-mailbluster) <br>
- [MailBluster Homepage](https://mailbluster.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the oo CLI and an OOMOL-connected MailBluster account; write and destructive actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
