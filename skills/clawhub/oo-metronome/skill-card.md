## Description: <br>
Metronome helps an agent search and read Metronome customers, invoices, and billable metrics through the OOMOL oo CLI instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent inspect Metronome customers, invoices, and billable metrics through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The trigger wording is broad and could cause Metronome account lookups to be considered in contexts where that access was not intended. <br>
Mitigation: Use the skill only in contexts where Metronome customer, invoice, or billable metric lookups are intended. <br>
Risk: First-time setup may require installing the oo CLI or connecting an OOMOL account. <br>
Mitigation: Review any first-time oo CLI install or account-connection step before proceeding, and run setup only after an auth or connection failure. <br>


## Reference(s): <br>
- [ClawHub Metronome skill page](https://clawhub.ai/oomol/skills/oo-metronome) <br>
- [Metronome homepage](https://metronome.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Metronome get and list operations; connector responses include data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
