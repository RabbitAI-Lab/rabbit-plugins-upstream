## Description:

Creates a date-ordered calendar of disclosed or statute-derived events for the user's holdings, with source anchors and no trading or market-impact judgments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and research teams tracking Chinese A-share holdings use it to organize confirmed upcoming events for up to 10 issuers and prepare monitoring or meeting materials. It excludes undisclosed or predicted dates and does not provide trading timing or event-impact judgments.

### Deployment Geography for Use:

Global (for Chinese A-share disclosures)

## Known Risks and Mitigations:

Risk: Connection examples can expose CUE_API_KEY to destinations outside the intended service.

Mitigation: Use user-supplied disclosures until credential handling is corrected; authenticated requests should use approved HTTPS destinations and prevent redirects from forwarding authorization elsewhere.

Risk: Cue queries reveal the selected issuers.

Mitigation: Include only issuers needed for the requested calendar.

Risk: A passing automated check does not establish that event dates are accurate.

Mitigation: Verify calendar dates against the original disclosures even after PASS.

## Reference(s):

- [Event taxonomy](references/event-taxonomy.md)
- [Cue Data MCP setup](https://cuecue.cn/hub/mcp)
- [Cue Omni Reader setup](https://cuecue.cn/hub/omni-reader)

## Skill Output:

**Output Type(s):** [Markdown, JSON Lines]

**Output Format:** [Markdown calendar and progress ledger with a JSON Lines source index]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Date-ordered events for up to 10 issuers; each calendar date must be anchored to a disclosure or applicable statute. The automated check does not replace review against original disclosures.]

## Skill Version(s):

0.1.33 (source: SKILL.md frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
