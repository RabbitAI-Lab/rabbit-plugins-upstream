## Description:

Truvera (truvera.io). Use this skill for ANY Truvera request -- reading, creating, updating, and deleting data. Whenever a task involves Truvera, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Truvera through an OOMOL-connected account, including DID and credential schema reads, creation, deletion, profile lookup, and job status polling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes downloaded installer scripts executed directly in a shell.

Mitigation: Review the setup path before installing and prefer a verified, inspectable, versioned oo CLI release instead of allowing automated curl | bash or irm | iex execution.

Risk: Write and destructive Truvera actions can create or delete DIDs and credential schemas.

Mitigation: Confirm the exact payload, target, and effect with the user before running any write or destructive action.

## Reference(s):

- [ClawHub Truvera Skill](https://clawhub.ai/oomol/skills/oo-truvera)
- [Truvera Homepage](https://truvera.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the oo CLI to inspect Truvera action schemas and run connector actions; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
