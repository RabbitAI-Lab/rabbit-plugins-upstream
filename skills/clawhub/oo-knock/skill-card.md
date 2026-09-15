## Description:

Knock (knock.app). Use this skill for ANY Knock request -- reading, creating, updating, and deleting data. Whenever a task involves Knock, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Knock users and trigger Knock workflows through an OOMOL-connected account. It supports read, write, and destructive actions through the oo CLI connector workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that can execute arbitrary code.

Mitigation: Review the oo CLI installer source or use a vendor-supported installation path with version pinning or checksum/signature verification before installing.

Risk: Write and destructive Knock actions can change user state, trigger workflows, or permanently delete user data.

Mitigation: Inspect the live connector schema first, then confirm the exact target, payload, and effect with the user before approving write or destructive actions.

## Reference(s):

- [ClawHub Knock skill page](https://clawhub.ai/oomol/skills/oo-knock)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Knock homepage](https://knock.app/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
