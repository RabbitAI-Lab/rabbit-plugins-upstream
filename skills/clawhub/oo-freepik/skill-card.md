## Description:

Magnific (Freepik) lets agents search stock images and templates, retrieve resource metadata, and create resource download URLs through the OOMOL-connected Freepik connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected Magnific (Freepik) account from an agent, including resource search, metadata lookup, and download URL creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer scripts executed directly in a shell.

Mitigation: Review and prefer an inspectable, version-pinned, or checksum-verified installation path before installing the oo CLI, and avoid administrator or root execution unless intentionally accepted.

Risk: Creating Freepik download URLs may consume account credits or trigger licensing obligations.

Mitigation: Confirm that the requested download is intended for the connected account and complies with the user's Freepik licensing and credit expectations before generating download URLs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-freepik)
- [Magnific (Freepik) homepage](https://www.magnific.com/freepik)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId fields when actions run successfully.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
