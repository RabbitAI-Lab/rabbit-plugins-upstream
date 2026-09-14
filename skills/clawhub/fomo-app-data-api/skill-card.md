## Description:

Read-only Fomo App API for public market-research data through ReplyNodes prepaid credits with one long-lived Bearer fetcher key; per-operation credit cost follows the authoritative catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query public Fomo market, token, user, trade, thesis, alert, and notification data through ReplyNodes for market research without write access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses one long-lived ReplyNodes fetcher API key.

Mitigation: Store REPLYNODES_API_KEY only in the agent secret store, never in prompts, logs, URLs, source files, or returned data.

Risk: Requests consume prepaid ReplyNodes credits and may incur paid usage if a cap is enabled.

Mitigation: Monitor credit usage and require an explicit paid-overage cap before allowing overage.

Risk: Fomo user balances, trades, alerts, and notifications are described as public data, but access expectations can affect privacy assumptions.

Mitigation: Do not present returned data as private or privileged unless Fomo and ReplyNodes explicitly document that access model.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/replynodes-ai/skills/fomo-app-data-api)
- [ReplyNodes publisher profile](https://clawhub.ai/user/replynodes-ai)
- [ReplyNodes account setup](https://app.replynodes.com/auth)
- [ReplyNodes developer keys](https://app.replynodes.com/developers)
- [Fomo operations catalog](references/operations.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with HTTP examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves ReplyNodes gateway response envelopes and request IDs when reporting results.]

## Skill Version(s):

2.0.1 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
