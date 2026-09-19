## Description:

Kraken.io (kraken.io). Use this skill for ANY Kraken.io request - searching and reading data. Whenever a task involves Kraken.io, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Kraken.io through an OOMOL-connected account, inspect the live connector schema, check plan status, and optimize images from URLs or uploads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image optimization may send images or public URLs through OOMOL/Kraken.io, including private or sensitive content.

Mitigation: Ask for explicit user confirmation before running optimize_image and avoid submitting sensitive images unless the user accepts that data path.

Risk: The documented CLI installer uses pipe-to-shell commands.

Mitigation: Do not run the installer unless the user independently trusts and verifies the installer source.

Risk: Connector actions depend on live schemas, account connection state, and billing status.

Mitigation: Inspect the live connector schema before building payloads and handle authentication, connection, or billing errors through the documented recovery steps.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/oomol/skills/oo-kraken-io)
- [Kraken.io Homepage](https://kraken.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce connector action results such as account quota data or optimized image transit references.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
