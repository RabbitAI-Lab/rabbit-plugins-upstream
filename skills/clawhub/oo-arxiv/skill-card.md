## Description:

arXiv lets an agent search and retrieve arXiv paper data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and other external users use this skill to search arXiv, retrieve paper metadata by identifier, list recent papers by category, and inspect live connector schemas before read-only requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup instructions can execute unreviewed code.

Mitigation: Prefer a verified package or installer source before installing the oo CLI; avoid blind curl | bash or irm | iex execution.

Risk: arXiv queries and connector metadata route through OOMOL as an intermediary.

Mitigation: Use the skill only when that routing is acceptable, and avoid sending confidential research topics through the connector.

Risk: The connector may require OOMOL account authentication even for read-only arXiv search workflows.

Mitigation: Sign in only when intentionally using the OOMOL-backed connector and confirm billing or credit requirements before retrying failed requests.

## Reference(s):

- [arXiv homepage](https://arxiv.org/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub arXiv skill page](https://clawhub.ai/oomol/skills/oo-arxiv)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before connector calls; read actions return JSON data with execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
