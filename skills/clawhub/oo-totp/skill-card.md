## Description:

Operates the OOMOL TOTP Authenticator connector through the oo CLI to inspect the live action schema and generate a current six-digit TOTP code for a configured website account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate time-based one-time password codes for accounts connected through OOMOL without handling raw authenticator secrets locally. It is intended for TOTP code retrieval after the oo CLI, OOMOL authentication, and the TOTP connector are already configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path may encourage running remote installer scripts directly in a shell.

Mitigation: Review the oo CLI installation path before installing and prefer a signed or package-manager installation when available.

Risk: Generated TOTP codes are sensitive authentication material.

Mitigation: Limit code exposure to the active authentication flow and avoid logging, storing, or sharing generated codes.

Risk: The skill depends on OOMOL for TOTP code generation and server-side credential injection.

Mitigation: Install and use the skill only when that third-party service dependency is acceptable for the account being accessed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-totp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [TOTP RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for schema inspection and connector execution; generated TOTP codes are sensitive authentication material.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
