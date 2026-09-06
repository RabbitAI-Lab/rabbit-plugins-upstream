## Description:

Generates a self-contained offline HTML position-size calculator for stocks and ETFs using delayed SentiSense market data and the user's own account, risk, entry, stop, and optional target inputs.

This skill is for research and development only.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to build an offline calculator that turns a user-provided risk budget, entry, stop, and optional target into share count, position value, dollar risk, account deployment percentage, and R multiple for a stock or ETF. It is for arithmetic and context only, not trade selection or investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key could be sent to a non-SentiSense server if SENTISENSE_BASE_URL is set unexpectedly.

Mitigation: Use the bundled node scripts/prepare_data.mjs path and make sure SENTISENSE_BASE_URL is unset unless the endpoint is intentionally trusted.

Risk: Optional external CLI execution can run with credential access.

Mitigation: Prefer the bundled zero-dependency script over the optional npx CLI path, and review any external command before execution.

Risk: Position-size output may be mistaken for trading advice or for a guaranteed loss limit.

Mitigation: Present results as arithmetic from user inputs, state that the skill does not choose trades or recommend actions, and disclose that stops may fill worse than planned.

Risk: The calculator uses delayed price data and historical average true range.

Mitigation: Describe market data as delayed and historical, and avoid presenting the generated values as live, predictive, or complete portfolio risk analysis.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/position-size-calculator)
- [Publisher Profile](https://clawhub.ai/user/thesentitrader)
- [SentiSense Homepage](https://sentisense.ai)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [SentiSense API Base](https://app.sentisense.ai)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Code, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands plus a JSON-backed self-contained HTML file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; generated HTML renders offline after build-time data fetch.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
