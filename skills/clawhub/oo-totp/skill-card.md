## Description:

Operates TOTP Authenticator through an OOMOL-connected account to generate current six-digit TOTP codes using the totp connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to generate the current six-digit TOTP code for a configured website account through the OOMOL totp connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated TOTP codes are authentication secrets and can enable account access while valid.

Mitigation: Treat generated codes like passwords; only invoke the connector for the intended account and avoid logging or sharing returned codes.

Risk: The skill depends on a connected OOMOL account and live connector access.

Mitigation: Use it only when the user intends to access the connector; resolve auth, connection, or billing errors through the documented setup steps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-totp)
- [TOTP Authenticator homepage](https://www.rfc-editor.org/rfc/rfc6238)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated TOTP codes and connector execution metadata; treat codes as sensitive.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
