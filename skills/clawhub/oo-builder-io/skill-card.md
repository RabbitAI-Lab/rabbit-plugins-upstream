## Description:

This skill guides agents to operate Builder.io through the OOMOL oo CLI, including reading, creating, updating, and deleting Builder.io content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent manage Builder.io content through an OOMOL-connected account. It supports content reads, listings, creation, updates, and deletion while requiring confirmation for write and destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute mutable code on the user's machine.

Mitigation: Review installer commands before use and prefer a verified package, pinned release, checksum, or inspected installer.

Risk: The skill can create, update, or delete Builder.io content.

Mitigation: Confirm the exact target, payload, and expected effect before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-builder-io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Builder.io Homepage](https://www.builder.io)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing Builder.io request payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
