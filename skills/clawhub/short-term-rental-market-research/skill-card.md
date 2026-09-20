## Description:

Compare short-term rental market supply, listing density, room mix, price distributions, and review signals using Crawlora Airbnb aggregates and selected live listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Market researchers, analysts, and agents use this skill to build comparable Airbnb short-term-rental market panels, including supply, density, room mix, price basis, review signals, and separately labeled live listing examples. It is intended for market comparison and follow-up research, not occupancy, revenue, investment, or legal-permission conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, locations, and the Crawlora API key are sent to Crawlora.

Mitigation: Use an approved Crawlora account, keep the API key in the environment, and avoid submitting sensitive research scopes unless that sharing is acceptable.

Risk: Suppressed or empty aggregate cells may be misread as zero supply or complete coverage.

Mitigation: Preserve suppression floors, coverage notes, filters, and retrieval timestamps, and describe unavailable evidence separately from observed zero values.

Risk: Live listing samples and public calendar hints may be overstated as occupancy, revenue, investment, or legal conclusions.

Mitigation: Keep live examples separate from aggregate statistics and state that listing density, calendar hints, and review snippets support further research only.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown market comparison with optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes geography, filter scope, observed supply, density context, price basis, collection dates, and explicit sampling and suppression limits.]

## Skill Version(s):

1.0.8 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
