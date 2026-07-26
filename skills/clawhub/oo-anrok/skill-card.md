## Description: <br>
Anrok (anrok.com). Use this skill for ANY Anrok request - searching and reading data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to search and read Anrok customer, product, filing, transaction, product mapping, and tax category data through an OOMOL-connected Anrok account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Returned Anrok customer, transaction, filing, and tax data may contain sensitive business or customer information. <br>
Mitigation: Limit responses to the user's requested data and treat connector results as sensitive. <br>
Risk: Future versions could add write or destructive Anrok actions. <br>
Mitigation: Review updated security evidence before upgrade and require explicit user confirmation before any write or destructive action. <br>
Risk: Using an incorrect payload schema can cause failed or unintended connector requests. <br>
Mitigation: Inspect the live `oo connector schema` for the selected action before constructing each payload. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-anrok) <br>
- [Anrok homepage](https://www.anrok.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only connector actions return Anrok data and an execution ID in response metadata.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
