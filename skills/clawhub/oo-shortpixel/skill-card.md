## Description:

ShortPixel (shortpixel.com). Use this skill for ShortPixel requests including reading, creating, updating, and deleting account data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to operate ShortPixel domains through an OOMOL-connected account, including CDN usage lookup, domain association, cache purge, storage purge, and domain revocation. It is intended for users managing ShortPixel account resources who need schema-checked connector commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path documents remote installer commands that execute downloaded scripts without verification.

Mitigation: Install the oo CLI only from a verified, versioned, signed, or checksum-validated source, and avoid running those installer commands from an elevated shell.

Risk: ShortPixel write and destructive actions can change account state, purge cached content, purge stored optimized variants, or revoke a domain association.

Mitigation: Inspect the live action schema, confirm the exact target and effect with the user, and require explicit approval before write, purge, storage purge, or revoke actions.

## Reference(s):

- [ClawHub ShortPixel skill release](https://clawhub.ai/oomol/skills/oo-shortpixel)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ShortPixel homepage](https://shortpixel.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should inspect the live connector schema before execution and request confirmation for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
