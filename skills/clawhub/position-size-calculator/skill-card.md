## Description:

Generates a self-contained position-size calculator for stocks and ETFs that uses read-only SentiSense market data to prefill delayed price, recent range, and sentiment context while computing share count, position value, account deployment, dollar risk, and optional R multiple from the user's own inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to create an offline HTML calculator that turns a ticker, account size, risk percentage, entry, stop, and optional target into position sizing arithmetic. It is intended for research and educational risk-context reporting, not investment advice or trade recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends SENTISENSE_API_KEY to app.sentisense.ai for market data requests.

Mitigation: Provide the key through the environment, keep it out of prompts and generated files, and use the bundled script path that locks requests to the documented HTTPS API origin.

Risk: The generated report is written to a user-selected --out path and can overwrite an existing file.

Mitigation: Choose an explicit output path and confirm before reusing a filename that may already contain work.

Risk: Readers may mistake arithmetic output for trading advice.

Mitigation: Present results as calculations from the user's own inputs, state that the skill does not choose securities, entries, stops, targets, or amounts, and avoid recommendation language.

Risk: Delayed prices, historical range data, slippage, gaps, costs, and portfolio correlation are not modeled as guarantees.

Mitigation: Label market data as delayed or historical, preserve the artifact's caveats, and treat the report as educational context rather than a forecast or risk limit.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/position-size-calculator)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)
- [SentiSense API origin](https://app.sentisense.ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with shell commands, optional JSON data, and a generated self-contained HTML report file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for build-time read-only market data requests; the generated HTML report renders offline after data is bound.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
