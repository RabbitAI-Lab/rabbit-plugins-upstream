## Description:

Wolfram|Alpha provides agents with concise answers, spoken-style results, and query validation through an OOMOL-connected Wolfram|Alpha connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask Wolfram|Alpha questions, validate whether a query can be interpreted, and retrieve short or spoken-style results through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path recommends executing a remote installer directly in a shell.

Mitigation: Download and inspect or verify the installer before running it, prefer an official pinned package when available, and avoid elevated shells.

Risk: Wolfram|Alpha queries are sent through OOMOL as the connector provider.

Mitigation: Install and use the skill only when that connector path is acceptable for the intended data and organization.

## Reference(s):

- [Wolfram|Alpha API](https://products.wolframalpha.com/api/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on live OOMOL connector schemas and Wolfram|Alpha service availability.]

## Skill Version(s):

1.0.3 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
