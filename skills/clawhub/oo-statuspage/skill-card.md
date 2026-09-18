## Description:

Statuspage (atlassian.com). Use this skill for ANY Statuspage request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Atlassian Statuspage pages, components, incidents, events, and automation email details through an OOMOL-connected account. It supports read workflows as well as confirmed write and destructive Statuspage actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands could install unverified code if the installer source or delivery path is compromised.

Mitigation: Review the installer path before installing and prefer a trusted, versioned, verifiable oo CLI source.

Risk: Write and destructive actions can create, update, or delete Statuspage components and incidents.

Mitigation: Confirm the exact page, component or incident, payload, and intended effect with the user before running write or destructive actions.

Risk: Connector payloads may be wrong if they are built from stale assumptions about the live action schema.

Mitigation: Inspect the current action schema with the oo CLI before constructing each action payload.

## Reference(s):

- [Statuspage homepage](https://www.atlassian.com/software/statuspage)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-statuspage)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the oo CLI and may return JSON connector responses.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
