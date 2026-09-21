## Description:

This skill helps agents handle SeaTable requests through the OOMOL-connected SeaTable connector, including reading, creating, updating, and deleting data instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate SeaTable through an OOMOL-connected account, including reading base metadata and rows, appending or updating rows, and deleting rows after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup commands execute remote oo CLI installer scripts without checksum or signature validation.

Mitigation: Review the installation method before use and prefer a verified package manager or an installer with checksum or signature validation.

Risk: SeaTable write and delete actions can change or remove table data.

Mitigation: Fetch the live action schema, confirm the exact payload and target rows with the user, and require explicit approval before write or destructive actions.

## Reference(s):

- [SeaTable homepage](https://seatable.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [SeaTable skill on ClawHub](https://clawhub.ai/oomol/skills/oo-seatable)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI to inspect connector schemas and run SeaTable actions; action responses are JSON.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
