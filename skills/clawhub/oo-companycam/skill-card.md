## Description:

CompanyCam (companycam.com). Use this skill for ANY CompanyCam request - reading, creating, updating, and deleting data. Whenever a task involves CompanyCam, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate CompanyCam through an OOMOL-connected account, including reading company, user, project, and tag data and performing confirmed project or tag changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run remote installer scripts when the oo CLI is missing.

Mitigation: Require explicit user approval before installing the oo CLI, and prefer a verified package or manually reviewed installer.

Risk: Write, archive, delete, login, and connection setup actions can change account state or authentication state.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running those actions.

## Reference(s):

- [CompanyCam homepage](https://companycam.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live connector schema before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: evidence release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
