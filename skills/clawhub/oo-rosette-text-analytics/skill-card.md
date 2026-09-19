## Description:

Rosette Text Analytics helps agents use an OOMOL-connected Rosette Text Analytics account to analyze sentiment, extract entities, identify languages, classify categories, and tokenize text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to route Rosette Text Analytics requests through the OOMOL `oo` CLI for sentiment analysis, entity extraction, language identification, category identification, and tokenization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute changing external code.

Mitigation: Prefer official verified package or release instructions, and review or verify any installer before running it.

Risk: The skill depends on trust in OOMOL and the Rosette connector path for credential handling and request execution.

Mitigation: Use it only when OOMOL and the connector path are trusted, and connect or refresh credentials only through the documented OOMOL account flow.

## Reference(s):

- [Rosette Text Analytics ClawHub page](https://clawhub.ai/oomol/skills/oo-rosette-text-analytics)
- [Rosette Text Analytics homepage](https://www.babelstreet.com/babel-street-insights)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an authenticated OOMOL account, and a connected Rosette Text Analytics API key; live action schemas are checked before payload construction.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
