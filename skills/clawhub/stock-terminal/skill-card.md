## Description:

Stock Terminal turns chat commands and natural stock questions into read-only, data-grounded financial terminal screens across price, sentiment, insider trades, congressional disclosures, institutional flows, analyst ratings, AI insights, and embedded news.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and financial research agents use this skill to answer ticker and market-research questions as terminal-style reports or to build a host application that wraps the read-only SentiSense API. It supports informational stock research and explicitly excludes trading, purchasing, wallet access, or personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key for read-only market data.

Mitigation: Use environment-variable authentication by default, keep the key out of model context and user-facing output, and use the CLI credential cache only when that local storage behavior is acceptable.

Risk: Financial terminal output can be mistaken for investment advice or can become misleading if values are stale or guessed.

Mitigation: Frame output as informational research, avoid buy/sell recommendations, fetch prices and market facts from tools before reporting them, and annotate delayed or batch data with freshness where available.

Risk: Optional news headline and social embed resolution can expand the skill into unsafe arbitrary URL fetching or untrusted HTML rendering.

Mitigation: Use only a narrow hardened fetcher for URLs returned by SentiSense documents, block private and metadata-network destinations across redirects, cap time and size, and sanitize or sandbox any embed HTML; otherwise fall back to URL slug titles.

## Reference(s):

- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Key Signup](https://app.sentisense.ai/get-api-key)
- [Stock Terminal on ClawHub](https://clawhub.ai/thesentitrader/skills/stock-terminal)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with terminal-style reports, inline code, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a SentiSense API key for read-only market data; outputs should be grounded in tool/API results and framed as informational research, not trading advice.]

## Skill Version(s):

1.9.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
