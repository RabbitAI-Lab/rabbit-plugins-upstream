## Description:

Provides read-only US stock market quotes, sentiment, analyst ratings, trading disclosures, institutional flows, options positioning, and screening through the SentiSense CLI or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and market researchers use this skill to retrieve US equity data for terminal queries, scripts, and read-only analysis. Its data is informational, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the CLI downloads and executes an npm package locally with access to the SentiSense API key.

Mitigation: Review the package and request approval before first-time CLI execution; prefer REST calls when shell commands are unnecessary.

## Reference(s):

- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)
- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/sentisense-cli)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON market data; Markdown guidance with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; stable CLI exit codes for scripting]

## Skill Version(s):

0.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
