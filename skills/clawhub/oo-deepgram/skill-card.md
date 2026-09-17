## Description:

This skill lets an agent query Deepgram account, project, model, balance, and key information through an OOMOL-connected Deepgram account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Deepgram resources and retrieve read-only account information through the OOMOL oo CLI. It is intended for Deepgram lookup workflows such as listing projects, models, balances, and project keys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute unreviewed code when the oo CLI is missing.

Mitigation: Install the oo CLI through a verified package or manually inspect the installer before running it.

Risk: Deepgram project data and API key listings are routed through the OOMOL connector.

Mitigation: Use least-privilege Deepgram credentials and request sensitive project or key data only when needed.

## Reference(s):

- [ClawHub Deepgram Skill](https://clawhub.ai/oomol/skills/oo-deepgram)
- [Deepgram Homepage](https://deepgram.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are described as JSON objects with data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
