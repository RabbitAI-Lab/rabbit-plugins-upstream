## Description:

Position Size Calculator - SentiSense helps agents create an offline HTML position-sizing calculator for stocks and ETFs using SentiSense market data and user-supplied risk inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to turn a ticker, account size, risk percentage, entry, stop, and optional target into share count, dollar risk, position value, deployed account percentage, and R multiple. The output is arithmetic and educational context, not investment advice or trade execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake arithmetic position-sizing output for investment advice or a trade recommendation.

Mitigation: Present results as calculations from user-supplied inputs, and state that the skill does not select securities, entries, stops, targets, or trade amounts.

Risk: The skill requires a SentiSense API key for read-only market-data calls.

Mitigation: Provide the key through the documented SENTISENSE_API_KEY environment variable and review optional CLI authentication separately before saving credentials locally.

Risk: The generated position plan assumes the stop price is honored, while gaps, fast markets, and costs can produce larger realized losses.

Mitigation: Keep the caveat visible in user-facing guidance and avoid describing calculated risk as a guaranteed maximum loss.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [SentiSense API](https://app.sentisense.ai)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/position-size-calculator)
- [Publisher Profile](https://clawhub.ai/user/thesentitrader)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated offline HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for read-only market-data requests at build time; the generated artifact renders offline.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
