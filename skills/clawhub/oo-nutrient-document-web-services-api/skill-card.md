## Description:

Nutrient DWS helps agents operate Nutrient Document Web Services through an OOMOL-connected account using schema-first oo CLI actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with Nutrient Document Web Services through an OOMOL connection, including estimating Build API credit usage, creating or revoking restricted JWT auth tokens, and retrieving sanitized account information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow may execute a live remote oo CLI installer without an integrity check.

Mitigation: Review the installer before use and prefer verified official documentation or a pinned, checksum-verified release.

Risk: Write and destructive Nutrient DWS actions can create or revoke auth tokens.

Mitigation: Confirm the exact payload and effect with the user, and require explicit approval before running write or destructive actions.

## Reference(s):

- [Nutrient DWS homepage](https://www.nutrient.io/api/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-nutrient-document-web-services-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include oo CLI commands that inspect connector schemas or run Nutrient DWS actions through a connected OOMOL account.]

## Skill Version(s):

1.0.2 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
