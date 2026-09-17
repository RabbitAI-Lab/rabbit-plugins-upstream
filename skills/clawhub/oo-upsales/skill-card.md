## Description:

Upsales enables agents to read, create, update, and delete Upsales companies, contacts, and users through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users with connected Upsales access can use this skill to manage CRM records, including companies, contacts, and users. It supports read operations directly and requires user confirmation before write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Review the installer path before enabling the skill and prefer a version-pinned, verifiable oo CLI installation source.

Risk: The skill can create, update, and delete Upsales CRM records.

Mitigation: Require explicit user confirmation of the target, payload, and intended effect before running write or destructive actions.

## Reference(s):

- [ClawHub Upsales skill page](https://clawhub.ai/oomol/skills/oo-upsales)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Upsales homepage](https://www.upsales.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing Upsales connector payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
