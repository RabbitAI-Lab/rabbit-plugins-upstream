## Description:

Provides agent access to Táve through the OOMOL `tave` connector for searching and reading contacts and studio profile data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Táve connector schemas and run read-only Táve actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that can execute arbitrary code on a user's machine.

Mitigation: Use the official install guide, independently verify the installer source, and prefer a signed or checksummed installer when available.

Risk: Connector actions access Táve account data through an authenticated OOMOL connection.

Mitigation: Run only the documented read actions unless a future action is clearly reviewed and approved, and inspect the live connector schema before constructing payloads.

## Reference(s):

- [Táve Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-tave)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Táve Homepage](https://www.vsco.co/workspace)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action payloads; action results are returned as JSON by the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
