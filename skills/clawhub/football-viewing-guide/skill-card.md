## Description:

Builds a dated, country-specific football broadcast guide from Crawlora's FotMob market, channel, and match listings without promising streaming access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Football fans and assistants use this skill to find listed channels for a match or prepare a local-time fixture guide for a selected country within the current seven-day window.

### Deployment Geography for Use:

Global; broadcast listings depend on the selected supported market.

## Known Risks and Mitigations:

Risk: Football lookup queries and the API key are sent to Crawlora.

Mitigation: Use a dedicated key, keep it secret, and review Crawlora's terms and privacy practices before submitting sensitive queries.

Risk: A listed channel may not be available through the viewer's subscription or device, and schedules may change.

Mitigation: Present listings as time-stamped, market-specific information; avoid promising access or inventing stream URLs.

Risk: The guide covers only the provider's current seven-day window.

Mitigation: Label dates outside that window as uncovered rather than implying a complete schedule.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/football-viewing-guide)
- [Crawlora FotMob endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown fixture table with local times, market, listed channels, and source links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Distinguishes missing listings from fetch failures; does not guarantee streaming access or subscription availability.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
