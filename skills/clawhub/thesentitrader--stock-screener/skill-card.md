## Description:

Stock Screener helps agents translate plain-language screening requests into read-only SentiSense stock and ETF screen plans using sentiment, analyst, technical, momentum, price, and market-cap filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to build and run read-only US stock and ETF screens from natural-language requests. It supports candidate discovery across SentiSense sentiment, social attention, analyst, technical, momentum, price, and market-cap signals without placing trades or modifying accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends screening requests to SentiSense and requires a SentiSense API key.

Mitigation: Use the required SENTISENSE_API_KEY only for intended read-only screening requests and avoid including unnecessary sensitive context in screen plans.

Risk: Screening output is informational financial data that users could mistake for personalized trading advice.

Mitigation: Present results as research context, show the screen plan and matched count, and avoid personalized buy, sell, or portfolio-allocation recommendations.

Risk: The optional CLI auth helper can store the API key locally until removed.

Mitigation: Prefer environment-based authentication where appropriate, or remove locally stored CLI credentials when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-screener)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)
- [SentiSense screener API endpoint](https://app.sentisense.ai/api/v1/screener/execute)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON screen plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SentiSense screener filters, sort order, matched counts, and read-only result summaries; not investment advice.]

## Skill Version(s):

1.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
