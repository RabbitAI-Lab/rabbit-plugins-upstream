## Description:

DocsBot AI lets agents search and read DocsBot AI data through the OOMOL-connected connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search DocsBot AI source chunks, retrieve teams and bots, and fetch reconstructed document text through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes a remote shell installer pattern for the OOMOL CLI.

Mitigation: Review the installer before use and prefer verified vendor documentation or a trusted package manager for installation.

Risk: Connected DocsBot AI credentials may allow the agent to search or read account-visible bots, teams, and document content.

Mitigation: Connect only DocsBot AI accounts and scopes that are intended for agent-assisted search and retrieval.

## Reference(s):

- [DocsBot AI homepage](https://docsbot.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-docsbot-ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live connector schema before submitting action payloads.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
