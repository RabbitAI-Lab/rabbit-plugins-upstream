## Description:

Check a Nodary AirnodeHub crypto feed every five minutes, compare each price to the prior check, and announce an attested alert only after a 5% or greater change.

This skill is ready for commercial/non-commercial use.

## Publisher:

[metobom](https://clawhub.ai/user/metobom)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure a recurring alert for a specific Nodary AirnodeHub crypto price feed and receive a notification only when the observed price changes by at least 5%.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates a recurring automation that contacts Nodary every five minutes and posts qualifying alerts into the requesting conversation.

Mitigation: Confirm the feed name, interval, comparison rule, and job ID with the user, and update or remove an existing job instead of creating duplicates.

Risk: Crypto price alerts may be mistaken for trading advice.

Mitigation: Treat alerts as informational only and do not request credentials, trading authority, or execute trades.

Risk: External feed responses may be unavailable, ambiguous, or non-numeric.

Mitigation: Use only explicit recognized feeds, require numeric current and prior prices before alerting, and reset the baseline without notifying when values are missing or invalid.

## Reference(s):

- [AirnodeHub LLMs Reference](https://airnode-v2-hub.api3.org/llms.txt)
- [Nodary AirnodeHub Endpoint](https://airnode-nodary.fly.dev/)
- [ClawHub Skill Page](https://clawhub.ai/metobom/skills/coin-price-alert)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration, Text]

**Output Format:** [Markdown or plain text with JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates a five-minute recurring alert job and produces short notification text only for qualifying price changes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
