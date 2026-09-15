## Description:

Semantic Scholar lets agents search and retrieve Semantic Scholar paper and author data through OOMOL's oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Semantic Scholar, inspect paper and author records, retrieve citations and references, and generate paper recommendations through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that could execute arbitrary local code.

Mitigation: Do not let an agent run the installer automatically; use a trusted installation method and review the installer source, install location, and removal path before use.

Risk: The skill depends on an OOMOL-connected Semantic Scholar account or API key.

Mitigation: Connect only accounts and credentials appropriate for the task, and review OOMOL account, connection, and billing state before retrying failed connector actions.

## Reference(s):

- [Semantic Scholar homepage](https://www.semanticscholar.org/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-semantic-scholar)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Skill icon](https://static.oomol.com/logo/third-party/semantic_scholar.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Semantic Scholar connector JSON responses containing data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
