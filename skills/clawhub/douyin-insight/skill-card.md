## Description:

Analyzes public Douyin content through keyword search, trending topics, creator posts, and video comments to support competitor and content research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Brands, creators, and marketing analysts use this skill to compare public Douyin videos and creators, track trends, and examine comments for content and audience insights.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin keywords, links, and the GUAIKEI service token are sent to a third-party service.

Mitigation: Use only approved public-data queries, confirm that external sharing is authorized, and keep the token private.

Risk: Search, post, and comment results are saved in local logs.

Mitigation: Restrict access to the logs and remove retained results when no longer needed.

Risk: Using the skill for private or logged-in content would exceed its public-data purpose.

Mitigation: Limit use to public Douyin data and do not supply private or logged-in material.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/douyin-insight)
- [Usage options](references/options.md)
- [Release changelog](references/changelog.md)
- [GUAIKEI service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON data, Text analysis]

**Output Format:** [Structured JSON results with optional natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include status, error codes, request details, and public-content metrics; search, post, and comment results are also saved locally.]

## Skill Version(s):

1.3.0 (source: ClawHub release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
