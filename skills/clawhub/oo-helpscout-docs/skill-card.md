## Description:

Help Scout Docs (helpscout.com). Use this skill for ANY Help Scout Docs request -- searching and reading data. Whenever a task involves Help Scout Docs, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search, list, and retrieve Help Scout Docs content through an OOMOL-connected Help Scout Docs account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote install commands that can execute changing code on the user's machine.

Mitigation: Review the oo CLI installation path and prefer a verified package, pinned release, checksum, or signature validation before installation.

Risk: Using the connector requires connecting Help Scout Docs credentials through OOMOL.

Mitigation: Confirm the credential-sharing model is acceptable before connecting the Help Scout Docs account.

## Reference(s):

- [Help Scout Docs skill page](https://clawhub.ai/oomol/skills/oo-helpscout-docs)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Help Scout](https://www.helpscout.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect connector schemas and return Help Scout Docs action results as JSON.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
