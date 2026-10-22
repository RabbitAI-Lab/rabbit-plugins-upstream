## Description:

Retrieves public Douyin videos, creator profiles, comments, and trending topics through keyword search and returns structured results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Social-media analysts, content strategists, and brand teams use this skill to search public Douyin posts, review creator activity and comments, and monitor trending topics. Its structured results support content research, competitor tracking, and sentiment review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries are sent to the API provider and may disclose information included in search terms.

Mitigation: Use a dedicated provider token and submit only queries you are comfortable sharing with the provider.

Risk: API use may incur service charges.

Mitigation: Check the provider's charges and choose request limits deliberately.

Risk: Retrieved results are saved locally and may remain in logs/.

Mitigation: Review and manage saved files in logs/ according to your data-handling requirements.

Risk: Formatted timestamps use Beijing time and may be misread in other time zones.

Mitigation: Interpret displayed timestamps as Beijing time when comparing or reporting dates.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/douyin-content-insights)
- [Publisher profile](https://clawhub.ai/user/why20261)
- [Guaikei API provider and token setup](https://www.guaikei.com)
- [Options reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON data]

**Output Format:** [Structured JSON containing Douyin video, creator, comment, or trending-topic results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Result counts are configurable up to 10,000 records per request; documented results are saved locally.]

## Skill Version(s):

1.4.0 (source: skill frontmatter, package.json, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
