## Description:

Launch Sentiment Sweep helps agents run a one-time Reddit and X reaction sweep for a product launch or announcement and report volume, representative quotes, themes, notable accounts, and credits spent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[veezee-build](https://clawhub.ai/user/veezee-build)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to capture a fixed-window snapshot of Reddit and X reactions to launches, announcements, releases, or news moments without setting up ongoing monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Launch names, search terms, selected social posts, and related context may be sent to Veezee.

Mitigation: Avoid confidential launch details unless third-party processing is acceptable, and keep queries scoped to the intended launch window.

Risk: Using the all-platform MCP mount can expose a broader integration than a Reddit and X launch sweep requires.

Mitigation: Use the narrower Reddit and X MCP endpoints unless the broader mount is specifically needed.

Risk: Large, real-time, or deep cursor sweeps can require paid credits and may stop when trial caps or budgets are exceeded.

Mitigation: Check usage before the sweep, set max_credits on calls, and stop on budget or trial-cap errors so the human can decide whether to upgrade.

## Reference(s):

- [Launch Sentiment Sweep on ClawHub](https://clawhub.ai/veezee-build/skills/veezee-launch-sentiment-sweep)
- [Veezee Reddit MCP endpoint](https://mcp.veezee.io/reddit)
- [Veezee X MCP endpoint](https://mcp.veezee.io/x)
- [Veezee API key mint endpoint](https://api.veezee.io/v1/keys/mint)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown readout with representative quotes, links, themes, notable accounts, and credits spent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quotes are verbatim from returned Reddit and X text with real links; the report includes credits spent.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
