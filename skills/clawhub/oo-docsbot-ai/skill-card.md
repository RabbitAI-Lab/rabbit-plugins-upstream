## Description:

DocsBot AI helps an agent search DocsBot-trained source chunks and retrieve teams, bots, and reconstructed documents through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support teams use this skill to query DocsBot AI knowledge bases, inspect available DocsBot resources, and fetch documents without handling raw service credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to execute remote installer scripts directly, which can install privileged local software without an integrity check.

Mitigation: Review the installer path first and prefer a verified, versioned oo CLI source with checksum or signature validation.

Risk: DocsBot AI credentials are connected through OOMOL-brokered connector requests.

Mitigation: Connect DocsBot AI only when the user is comfortable with OOMOL brokering those requests and avoid opening connection or login flows unless a command fails with the matching setup error.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-docsbot-ai)
- [DocsBot AI homepage](https://docsbot.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running DocsBot AI actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
