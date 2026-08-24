## Description:

Pulls prediction-market odds, order books, and forecast questions from Polymarket, Kalshi, and Metaculus via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research current and historical prediction-market signals, compare event odds across Polymarket and Kalshi, and inspect Metaculus community forecasts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included Crawlora helper can make authenticated requests beyond the advertised prediction-market endpoints.

Mitigation: Use the skill in a clean environment, keep CRAWLORA_API_BASE unset unless the target is trusted, and prefer calls limited to Polymarket, Kalshi, and Metaculus endpoints.

Risk: Prediction-market outputs may be mistaken for financial advice.

Mitigation: Treat results as market data for research only and review any user-facing interpretation before relying on it.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/prediction-markets-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only market data lookups require CRAWLORA_API_KEY and return normalized JSON.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
