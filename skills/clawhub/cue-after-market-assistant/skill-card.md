## Description:

Produces an after-market A-share review of index moves, money flows, sector themes, market drivers, portfolio impact, and next-day signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External investors use this skill to review broad A-share market and sector activity after the close, assess possible portfolio implications, and prepare next-day observation points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests API keys in chat despite contradictory privacy assurances.

Mitigation: Configure the API key locally instead of pasting it into chat, and rotate any key already shared there.

Risk: The skill runs an automatically updated external runner whose code and Cue server behavior are outside this package review.

Mitigation: Review and pin the external runner before execution.

Risk: Queries go to Cue, runs consume credits, and recurring schedules can run repeatedly.

Mitigation: Enable recurring schedules only when wanted, and account for credit use before running.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-after-market-assistant)
- [Cue platform](https://cuecue.cn)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, HTML, Guidance]

**Output Format:** [Structured Chinese market recap in Markdown, with a standalone HTML dashboard.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Market-level A-share coverage; excludes individual-stock technical analysis and labels intraday snapshots when used before the close.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
