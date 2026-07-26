## Description: <br>
Recruit CRM lets agents search and read candidates, companies, contacts, and jobs through an OOMOL-connected Recruit CRM account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiting teams and agents use this skill to retrieve individual Recruit CRM records and list candidates, companies, contacts, and jobs from a connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill retrieves recruiting data from a connected Recruit CRM account through OOMOL's CLI and connector. <br>
Mitigation: Install and use it only when you trust OOMOL with read access to that Recruit CRM data. <br>
Risk: Future connector action changes could alter expected inputs or effects. <br>
Mitigation: Inspect the live action schema before execution and require explicit user confirmation for any write or destructive action if such actions are introduced. <br>


## Reference(s): <br>
- [ClawHub Recruit CRM skill page](https://clawhub.ai/oomol/skills/oo-recruitcrm) <br>
- [Recruit CRM homepage](https://recruitcrm.io) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces instructions for schema inspection and read-only Recruit CRM get/list actions through the oo CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
