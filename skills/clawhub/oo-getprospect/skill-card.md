## Description:

GetProspect lets an agent search leads and companies, find or verify business email addresses, and read saved contact profiles through an OOMOL-connected GetProspect account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate GetProspect from an agent, including lead and company search, business email discovery, email verification, and contact lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include internet installer commands that execute downloaded scripts.

Mitigation: Inspect and verify the installer first, or install the oo CLI through a trusted release or package-manager path before using the skill.

Risk: The skill can query business contact and lead data through a connected GetProspect account.

Mitigation: Use it only for authorized searches, inspect the live action schema before submitting payloads, and keep account access scoped to the intended use.

## Reference(s):

- [GetProspect homepage](https://getprospect.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-getprospect)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return GetProspect action responses as JSON data with execution metadata when commands are run.]

## Skill Version(s):

1.0.2 (source: release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
