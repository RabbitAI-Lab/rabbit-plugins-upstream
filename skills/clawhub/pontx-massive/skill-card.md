## Description:

Integrate Massive market data through Pontx. Use for bars, snapshots, ticker lookup, backtests, dashboards, entitlements, pagination, market-session time zones, throttling, or licensing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pontjs](https://clawhub.ai/user/pontjs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to integrate Massive market data through Pontx for bars, snapshots, ticker lookup, backtests, dashboards, and market-data rights decisions. It helps preserve market-time semantics, plan entitlements, pagination, throttling, credential handling, and licensing constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market-data access may not include the user's required history, recency, dataset, display, storage, or redistribution rights.

Mitigation: Verify the account plan, subscriber classification, and written rights before retrieval, caching, export, public display, or redistribution.

Risk: Credentials could be exposed through command arguments, URLs, logs, examples, or traces.

Mitigation: Read the credential environment variable from the current Pontx contract and never print, persist, or embed its value.

Risk: Market data can be delayed, incomplete, corrected, unavailable, or unsuitable for personalized investment advice.

Mitigation: Report as-of time, recency tier, time zone, and known gaps, and avoid presenting API results as guaranteed or as personalized investment advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pontjs/skills/pontx-massive)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires current Pontx contract lookup before execution and avoids exposing credential values.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
