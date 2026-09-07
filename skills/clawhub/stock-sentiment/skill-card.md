## Description:

Sentiment and smart-money positioning for US stocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch read-only US equity sentiment, market mood, smart-money positioning, analyst activity, AI insights, and sentiment-tagged news from the SentiSense API. The skill is intended to synthesize educational market context, not to provide order entry, portfolio management, or personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional npx-based execution and remote skill installation may run code outside the reviewed artifact.

Mitigation: Prefer the bundled Python client or direct curl GET requests; only use npx or remote collection installation when the SentiSense package, dependencies, and remote source are trusted and isolated.

Risk: Financial sentiment and smart-money summaries can be misread as personalized trading advice.

Mitigation: Frame outputs as educational market context and avoid buy, sell, order-entry, portfolio-management, or personalized recommendation language.

## Reference(s):

- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API skill reference](https://sentisense.ai/skill.md)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-sentiment)
- [ClawHub publisher profile](https://clawhub.ai/user/thesentitrader)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with API response synthesis, inline shell commands, and optional Python client usage.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY and network access to app.sentisense.ai; outputs read-only informational context.]

## Skill Version(s):

0.4.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
