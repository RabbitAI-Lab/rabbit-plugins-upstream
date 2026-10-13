## Description:

Search public Douyin videos and trends, retrieve creator posts and video comments, and return structured results for content research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, brands, and content teams use this skill to find popular public Douyin content, track trends and creators, and analyze video comments for content planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search keywords and Douyin links are sent to a third-party API using a GUAIKEI token.

Mitigation: Use a managed token and submit only keywords or links that may be shared with www.guaikei.com.

Risk: Local result logs and responses can contain public comments and creator metrics.

Mitigation: Limit log retention and sharing; handle the data under Douyin terms and applicable privacy rules.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/why20261/skills/douyin-videos-search)
- [GUAIKEI API provider](https://www.guaikei.com)
- [Options and configuration](references/options.md)
- [Search output schema](assets/search_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [Text, JSON data, Guidance]

**Output Format:** [Structured JSON results with a status, message, request details, and public Douyin data; optional text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers keyword results, trending topics, creator posts and metrics, or video comments; may return an empty result or an error.]

## Skill Version(s):

1.3.0 (source: frontmatter, changelog, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
