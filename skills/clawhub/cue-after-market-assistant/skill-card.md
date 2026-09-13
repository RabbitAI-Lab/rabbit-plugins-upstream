## Description:

Uses Cue to generate a structured after-market recap that explains market moves, fund flows, sector signals, portfolio relevance, next-day watch items, and source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill after market close to request a Cue-generated market recap, optionally focused on watchlists, sectors, or holdings supplied by the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market-recap prompts, watchlists, and holdings entered by the user are sent to Cue's external service.

Mitigation: Avoid including account numbers, broker details, position sizes, or other personal financial data unless Cue's privacy and security practices have been reviewed.

Risk: Market analysis may be incomplete, stale, or unsuitable as the sole basis for investment decisions.

Mitigation: Review the cited sources and treat the output as informational research support, not personalized financial advice.

Risk: Cue service availability and external market data sources can affect report quality or completion.

Mitigation: Run the documented health checks before use and retry or use the listed manual market-data sources if Cue is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-after-market-assistant)
- [Cue API key setup](https://cuecue.cn/hub/api-key)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Sample after-market report](https://cuecue.cn/share/e48Yoz--t14FjIHxaxxLz)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with source links, plus shell commands and setup guidance when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report is expected to be delivered verbatim after Cue returns a successful result.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
