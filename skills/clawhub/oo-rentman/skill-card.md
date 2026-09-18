## Description:

Rentman (rentman.io) skill for searching and reading Rentman contacts, contact persons, equipment, and projects through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Rentman business data, including contacts, contact persons, equipment, and projects, through the OOMOL `oo` CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup guidance includes remote installer commands for the OOMOL CLI.

Mitigation: Do not run remote installer commands unattended; prefer a verified package or inspect and verify the installer before execution.

Risk: Rentman data access is mediated through OOMOL-connected credentials.

Mitigation: Install only when use of OOMOL as an intermediary is acceptable, and confirm the Rentman connection and scopes before use.

Risk: Future Rentman connector actions could include write or destructive behavior even though this release lists read-only actions.

Mitigation: Inspect each live connector schema and require explicit user approval before any write or destructive Rentman action.

## Reference(s):

- [ClawHub Rentman Skill Page](https://clawhub.ai/oomol/skills/oo-rentman)
- [Rentman Homepage](https://rentman.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; available actions are read-only get and list operations.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
