## Description:

Researches public sportsbook markets, event schedules, live status, and game context using DraftKings Sportsbook, ESPN, and SofaScore through the Crawlora API. Use for odds snapshots and event comparisons, not wagering, account actions, or financial advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect timestamped sportsbook market snapshots and compare them with event schedules, live status, and team or player context for research and reporting. It should not be used to place bets, access accounts, or provide financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sportsbook odds, market availability, and event status can change quickly and can vary by jurisdiction.

Mitigation: Timestamp snapshots and independently verify current odds, operator terms, and local rules before relying on the information.

Risk: The skill uses a Crawlora API key and sends sports research queries to Crawlora.

Mitigation: Keep the API key out of untrusted environments and install only when sending these queries and credentials to Crawlora is acceptable.

Risk: Odds snapshots can be mistaken for forecasts, guaranteed returns, or wagering advice.

Mitigation: Present outputs as research context only and do not use them to place bets, perform account actions, or provide financial advice.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/sports-betting-research)
- [Crawlora Publisher Profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and JSON result interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include timestamped odds snapshots, event comparisons, and reminders to verify current odds, operator terms, and local rules.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
