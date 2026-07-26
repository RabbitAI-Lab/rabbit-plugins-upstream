## Description: <br>
Stock Terminal turns chat commands and natural-language market questions into read-only financial terminal reports across price, sentiment, smart-money flows, analyst ratings, AI insights, options, and news. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesentitrader](https://clawhub.ai/user/thesentitrader) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and financial research agents use this skill to answer stock-market questions with dense, data-grounded terminal screens or concise text replies. It is for informational market research and implementation guidance, not trading execution or personalized investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SENTISENSE_API_KEY exposure through prompts, tool arguments, logs, or user-visible output. <br>
Mitigation: Keep the key in host environment state, inject it only inside read-only handlers, and never pass it to the model or display it to users. <br>
Risk: Market output could be mistaken for personalized financial advice. <br>
Mitigation: Frame responses as informational, data-grounded context only; do not present buy, sell, solicitation, or personalized recommendation language. <br>
Risk: Stale or fabricated market numbers can mislead users. <br>
Mitigation: Require a read-only data call or trusted screen cache before quoting prices, ratings, headlines, or dates, annotate batch freshness, and say when data is unavailable instead of guessing. <br>
Risk: Optional headline or social embeds can introduce untrusted third-party fetch and markup behavior. <br>
Mitigation: Use only a narrow hardened fetcher for URLs returned by SentiSense, sanitize or sandbox embeds, and fall back to URL slugs when that protection is not available. <br>


## Reference(s): <br>
- [Stock Terminal on ClawHub](https://clawhub.ai/thesentitrader/skills/stock-terminal) <br>
- [SentiSense Website](https://sentisense.ai) <br>
- [SentiSense API Reference](https://sentisense.ai/skill.md) <br>
- [SentiSense API Key](https://app.sentisense.ai/get-api-key) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown terminal screens, concise prose, implementation guidance, API examples, and inline bash or code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for read-only SentiSense API calls; no trading, purchasing, wallet access, or write operations.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
