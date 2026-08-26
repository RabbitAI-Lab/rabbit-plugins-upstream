## Description:

Stock Screener helps agents translate plain-language US stock and ETF screening requests into SentiSense screen plans using sentiment, analyst, technical, momentum, price, and market-cap filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to find stock and ETF research candidates across sentiment, analyst, momentum, technical, price, and size criteria. Outputs are informational research context and should not be treated as personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Screener results may be mistaken for personalized investment advice.

Mitigation: Present outputs as research context, show the screen plan and matched counts, and avoid buy or sell recommendations.

Risk: The skill requires a SentiSense API key and the CLI supports optional local key storage.

Mitigation: Prefer the documented environment variable path, or confirm local storage expectations before using CLI authentication.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [SentiSense Screener API Endpoint](https://app.sentisense.ai/api/v1/screener/execute)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/stock-screener)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only screen plans and financial research context; no trading, purchases, wallet access, or account modification.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
