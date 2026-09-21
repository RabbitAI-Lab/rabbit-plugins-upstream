## Description:

Research public Resy and OpenTable restaurant discovery, profiles, and time-specific availability snapshots. Use for dining shortlists or reservation-demand comparisons, not booking or ordering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to compare public restaurant profiles, menus, reviews, and observed availability snapshots from Resy and OpenTable for a requested local dining date, time, and party size. It supports dining shortlists and reservation-demand comparisons, but does not book, hold, modify, cancel, or purchase reservations or ticketed events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restaurant names, locations, dates, party sizes, and related search parameters are sent to Crawlora with the user's Crawlora API key.

Mitigation: Use the skill only for public dining research, avoid unnecessary private details, and confirm the user is comfortable sharing the query parameters with Crawlora before making calls.

Risk: Displayed availability can change after retrieval and does not hold inventory.

Mitigation: Present availability as a dated snapshot with retrieved_at, provider, provider ID, requested local date/time/zone, party size, and source URL where available.

Risk: The skill is read-only and cannot make, change, cancel, or purchase reservations or ticketed dining events.

Mitigation: Keep booking and ticketing actions out of scope, and direct users to the relevant provider if they want to complete a reservation or purchase.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/dining-demand-research)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, API calls]

**Output Format:** [Markdown with restaurant comparison tables, source links, timestamps, and optional shell commands for Crawlora API calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Availability results are dated snapshots and should include retrieved_at, provider ID, requested local date/time/zone, party size, and source URL when available.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
