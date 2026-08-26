## Description:

Stock Terminal helps agents turn ticker commands and natural-language stock research questions into read-only, data-grounded financial terminal reports using SentiSense market data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent builders use this skill to answer stock-research prompts such as ticker opens, daily briefs, smart-money screens, and market questions with read-only informational outputs. It is for market research and educational context, not investment advice or trade execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market-data outputs could be mistaken for personalized investment advice.

Mitigation: Frame outputs as informational market research and educational context, and do not provide personal buy, sell, or hold recommendations.

Risk: A SentiSense API key could be exposed if it enters model context, tool arguments, emitted events, or conversation history.

Mitigation: Keep SENTISENSE_API_KEY in host environment or tool-handler state, inject it only into read-only API calls, and keep it out of prompts and model-visible data.

Risk: Financial values, headlines, ratings, or dates could become stale or fabricated if quoted from memory.

Mitigation: Require tool calls or read_screen snapshots before quoting specific market data, and include freshness cues where the source provides them.

Risk: News headline resolution could become overly broad web browsing.

Mitigation: Fetch only URLs returned by SentiSense document payloads with the bounded fetcher described by the artifact, or use the slug fallback instead of exposing a general browser or fetch tool.

## Reference(s):

- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [SentiSense API Key Setup](https://app.sentisense.ai/get-api-key)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/stock-terminal)
- [ClawHub Publisher Profile](https://clawhub.ai/user/thesentitrader)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with terminal-style reports and optional shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only outputs; requires SENTISENSE_API_KEY for SentiSense API calls; no trading, purchasing, write, or wallet actions.]

## Skill Version(s):

1.8.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
