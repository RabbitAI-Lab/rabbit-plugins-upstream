## Description:

Searches TikTok public content by keyword, retrieves creators’ public posts and video comments, and returns structured JSON for competitor and content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

TikTok creators, brands, and market researchers can use the skill to find content by keyword, review a creator’s public posts, and inspect video comments for competitor research, content planning, and audience insight.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and the service token are sent to guaikei.com, and API use may incur charges.

Mitigation: Use the service only if you accept that data sharing and any applicable charges; keep request counts within the plan limits.

Risk: Opting in to logging retains result files locally.

Mitigation: Leave logging disabled unless you need local copies, and handle retained results according to your data practices.

## Reference(s):

- [TikTok data service and token access](https://www.guaikei.com)
- [ClawHub release page](https://clawhub.ai/why20261/skills/tiktok-insight)
- [Command options and output fields](references/options.md)
- [Release changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Structured data]

**Output Format:** [JSON output envelope containing arrays of TikTok search results, creator posts, or video comments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be empty; some zero or empty fields may be omitted, and playback URLs may expire.]

## Skill Version(s):

1.1.1 (source: release metadata, frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
