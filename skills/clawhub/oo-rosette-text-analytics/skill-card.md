## Description:

Rosette Text Analytics helps agents analyze sentiment, extract entities, identify document language and categories, and tokenize text through an OOMOL-connected Rosette connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to run Rosette Text Analytics actions from an agent for text analysis tasks such as sentiment analysis, named entity extraction, language detection, categorization, and token identification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may lead an agent to run mutable remote installer scripts without verification or explicit user approval.

Mitigation: Require human approval for installation, use a trusted and versioned oo CLI installation method, and keep agent use limited to the listed Rosette analytics actions.

## Reference(s):

- [Rosette Text Analytics homepage](https://www.babelstreet.com/babel-street-insights)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-rosette-text-analytics)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
