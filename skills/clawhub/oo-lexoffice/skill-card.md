## Description:

This skill lets agents read, create, and update lexoffice data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage lexoffice articles, contacts, voucher metadata, and organization profile information through an OOMOL-connected lexoffice account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote shell installers from OOMOL endpoints.

Mitigation: Use a pinned, verifiable installer or official package-manager flow where available, and run the remote installer only after reviewing and trusting the endpoint.

Risk: Write actions can create or update lexoffice articles and contacts.

Mitigation: Confirm the exact payload and expected effect with the user before running state-changing actions against lexoffice data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lexoffice)
- [lexoffice homepage](https://office.lexware.de/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing lexoffice actions require user confirmation; connector runs return JSON data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
