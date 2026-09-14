## Description:

Queries off-exchange index fund and ETF feeder fund information through Index Hub, including fund details, fees, holdings, returns, dividends, tracking error, keyword search, and batch comparison.

This skill is ready for commercial/non-commercial use.

## Publisher:

[e-fintech](https://clawhub.ai/user/e-fintech)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve and summarize factual information about off-exchange index funds, ETF feeder funds, and related ETF reference data. It supports objective screening and comparison workflows while avoiding personalized investment advice, trading instructions, and performance promises.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fund-query requests are sent to the Index Hub service at www.etf.com.cn.

Mitigation: Install and use the skill only when the user is comfortable with that service relationship and with sending fund-query requests to the provider.

Risk: The skill requires an API key that could be exposed through command history, logs, or final answers if handled carelessly.

Mitigation: Use ./install.sh and enter the key at the hidden prompt, store it in ~/.config/index-hub/api_key, and avoid displaying credentials, authorization headers, or raw configuration.

Risk: Fund facts and comparisons could be misunderstood as investment advice or future performance claims.

Mitigation: Keep answers factual, include the provider disclaimer, avoid personalized recommendations and trading instructions, and use the bundled answer guardrails before final output.

Risk: Service outages, invalid credentials, or missing permissions can prevent current fund data from being returned.

Mitigation: Use the installer smoke test where possible, and when data is unavailable explain the access or availability limit rather than fabricating fund values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/e-fintech/skills/open-fund-query)
- [Index Hub AI Skills help document](https://cdn.efunds.com.cn/eda/h5/itcenter/pd/ai-skills-doc/help.pdf)
- [OEF catalog reference](artifact/references/catalog-oef.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text answers, with setup shell commands and internal JSON API results summarized for users.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an Index Hub API key; final user-facing answers include the provider disclaimer and should not expose credentials, raw responses, or internal service details.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
