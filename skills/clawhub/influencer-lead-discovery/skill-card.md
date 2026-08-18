## Description:

Cross-platform influencer discovery and shortlist building across YouTube, TikTok, and Instagram.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyu-xixihaha](https://clawhub.ai/user/chengyu-xixihaha)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, growth, and partnership teams use this skill to search, enrich, compare, and rank creator candidates across YouTube, TikTok, and Instagram for campaign outreach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creator search terms, profile identifiers, and shortlist context may be sent to the Scrumball/scdata API gateway.

Mitigation: Use the skill only with data appropriate for that external service, and configure SCRUMBALL_BASE_URL or SCRUMBALL_API_KEY only for endpoints and environments you trust.

## Reference(s):

- [API Index](references/api-index.md)
- [Request and Response Guide](references/request-response.md)
- [Operation Manifest](references/operations.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown shortlist with candidate rationale, risk notes, next steps, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API operation IDs, platform identifiers, profile/content signals, and data quality caveats.]

## Skill Version(s):

1.0.2 (source: server release metadata and config.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
