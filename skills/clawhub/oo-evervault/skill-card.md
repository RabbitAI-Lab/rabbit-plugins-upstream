## Description:

Evervault helps agents operate Evervault through an OOMOL-connected account for encryption, decryption, and token-inspection tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Evervault connector schemas and run OOMOL `oo` CLI actions for encrypting JSON, decrypting JSON, and inspecting encrypted tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Decryption actions may reveal sensitive data.

Mitigation: Confirm the exact decryption payload and intended handling of decrypted output before running `decrypt_json`.

Risk: Broad automatic guidance could trigger sensitive encryption or decryption workflows outside the user's intent.

Mitigation: Use the skill only for explicit Evervault encrypt, decrypt, or token-inspection tasks, and inspect the live action schema before constructing payloads.

Risk: Account setup, connection, or billing commands may affect the user's OOMOL environment.

Mitigation: Run setup, login, connection, or billing recovery steps only after a matching command failure and with user awareness.

## Reference(s):

- [ClawHub Evervault Skill Page](https://clawhub.ai/oomol/skills/oo-evervault)
- [Evervault Homepage](https://evervault.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands target the OOMOL `oo` CLI and may include JSON request payloads and setup guidance.]

## Skill Version(s):

1.0.0 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
