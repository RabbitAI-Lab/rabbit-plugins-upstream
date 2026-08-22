## Description:

Stock terminal for AI agents that turns typed commands or natural-language market questions into synthesized read-only reports across price, sentiment, insider trades, congressional disclosures, institutional flows, analyst ratings, AI insights, and embedded news.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and market researchers use this skill to query SentiSense's read-only market data through an agent-style financial terminal. It supports ticker screens, daily briefs, smart-money screens, flow analysis, options positioning, earnings context, and sentiment-tagged news while framing output as informational research rather than investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects an agent to SentiSense using an API key and may issue many read-only market-data requests.

Mitigation: Keep SENTISENSE_API_KEY secret, inject it only in host-side handlers, avoid putting it in prompts or logs, and apply rate-limit-aware request handling.

Risk: Market-data synthesis can be mistaken for personal investment advice or a trading recommendation.

Mitigation: Present outputs as informational financial research, keep the no-advice frame, and avoid personalized buy, sell, or hold recommendations.

Risk: Headline or embed resolution can expand the network surface if implemented as a general URL fetcher.

Mitigation: Use the documented hardened fetcher pattern for headline and embed resolution, or fall back to slug-derived titles when safe fetching is unavailable.

## Reference(s):

- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [ClawHub Skill Listing](https://clawhub.ai/thesentitrader/skills/stock-terminal)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with terminal-style tables, structured report screens, inline code blocks, and implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for authenticated read-only SentiSense data calls; output is informational and should not be treated as investment advice.]

## Skill Version(s):

1.8.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
