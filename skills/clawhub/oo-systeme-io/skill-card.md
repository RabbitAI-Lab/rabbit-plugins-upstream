## Description:

Systeme.io (systeme.io). Use this skill for ANY Systeme.io request — reading, creating, updating, and deleting data. Whenever a task involves Systeme.io, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Systeme.io through an OOMOL-connected account for contact, tag, webhook, enrollment, course, subscription, and custom field workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer scripts that execute directly in a shell.

Mitigation: Review setup commands before installing and prefer a trusted, verifiable oo CLI release or documented package flow.

Risk: Write and destructive Systeme.io actions can create, update, cancel, detach, or delete records.

Mitigation: Check the exact target and payload, and require explicit user approval before write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-systeme-io)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Systeme.io homepage](https://systeme.io)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo connector schema checks before constructing action payloads; responses are JSON from the oo CLI.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
