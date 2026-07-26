## Description: <br>
Operates Kommo through an OOMOL-connected account so an agent can search and read CRM data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent inspect Kommo connector schemas and run get/list actions against a connected Kommo CRM account. It is intended for CRM account, company, contact, lead, pipeline, task, and user lookup or listing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Kommo CRM records may include sensitive business or personal information. <br>
Mitigation: Install and use the skill only for intended CRM read workflows, and review agent outputs before sharing or storing retrieved records. <br>
Risk: First-time CLI installation or account connection can grant access to a connected Kommo account. <br>
Mitigation: Review install and connection steps before running them, and connect only the Kommo account and scopes needed for the task. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-kommo) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [Kommo Homepage](https://www.kommo.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides schema-first execution through the oo CLI and returns connector responses as JSON when commands are run with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
