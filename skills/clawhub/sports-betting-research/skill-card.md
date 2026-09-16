## Description:

Researches public sportsbook markets, event schedules, live status, and game context using DraftKings Sportsbook, ESPN, and SofaScore through the Crawlora API. Use for odds snapshots and event comparisons, not wagering, account actions, or financial advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to collect timestamped public sportsbook market snapshots and compare them with sports event schedules, status, scores, team, and player context. It supports research and reporting, not wagering decisions or account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sportsbook odds, availability, and legal access can vary by jurisdiction and time.

Mitigation: Verify material decisions with licensed operators and local rules before relying on returned market data.

Risk: Returned odds or line movement could be mistaken for betting, financial, or predictive advice.

Mitigation: Use outputs as timestamped research snapshots only and keep them separate from recommendations or forecasts.

Risk: Requests are sent to Crawlora with a Crawlora API key.

Mitigation: Do not provide sportsbook account credentials, payment data, or private personal data in requests.

## Reference(s):

- [Endpoint Reference](artifact/reference/endpoints.md)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/sports-betting-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and scoped GET requests to documented Crawlora sports endpoints.]

## Skill Version(s):

1.0.0 (source: server release metadata, created 2026-09-14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
