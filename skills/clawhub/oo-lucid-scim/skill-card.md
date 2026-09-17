## Description:

Lucid SCIM helps agents read Lucid SCIM users, groups, and service-provider configuration through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, administrators, and developers use this skill to inspect Lucid SCIM users, groups, and service-provider configuration from a connected Lucid account. It supports read-only SCIM lookup workflows with schema validation before each connector call.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review the installer before execution, prefer an official signed package or pinned release when available, and install the oo CLI only from trusted OOMOL sources.

Risk: The skill operates against a connected Lucid SCIM account through the OOMOL CLI.

Mitigation: Connect only the Lucid SCIM account scopes intended for the workflow and re-check live action schemas before sending payloads.

## Reference(s):

- [ClawHub Lucid SCIM skill](https://clawhub.ai/oomol/skills/oo-lucid-scim)
- [Lucid SCIM homepage](https://lucid.co)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only connector actions return Lucid SCIM data through the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
