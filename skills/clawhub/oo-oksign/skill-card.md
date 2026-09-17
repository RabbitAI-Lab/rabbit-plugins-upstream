## Description:

OKSign (oksign.be). Use this skill for ANY OKSign request: searching and reading data through the OOMOL-connected OKSign connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, operators, and developers use this skill to inspect OKSign account credits, document metadata, linked document identifiers, active documents, and configured users through OOMOL's OKSign connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute local code.

Mitigation: Review before installing; prefer a verified, signed, or package-manager installation path for the oo CLI when available.

Risk: OKSign actions depend on account authentication, connector availability, and sufficient OOMOL credits.

Mitigation: Run setup or billing steps only after a matching command failure and retry after the account connection or credit issue is resolved.

## Reference(s):

- [OKSign ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-oksign)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [OKSign Homepage](https://www.oksign.be/en/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing OKSign requests.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
