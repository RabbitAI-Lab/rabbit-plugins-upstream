## Description:

Helps agents discover Douyin creators and analyze public posts, comments, search results, and trending topics for content and partnership research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content researchers and marketing teams use this skill to find Douyin creators, compare public post engagement, examine comments, and follow trending topics when evaluating content or potential collaborators.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin keywords or links and the API token are sent to a third-party data provider.

Mitigation: Use only when this data transfer is acceptable, and protect the API token.

Risk: Search, creator-post, and comment results are saved in local logs by default.

Mitigation: Review, restrict access to, and remove saved results according to your retention policy.

Risk: Private, login-only, or redistributed data may require authorization.

Mitigation: Use publicly available data and confirm rights before accessing or redistributing results.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/why20261/skills/douyin-kol-discovery)
- [API provider](https://www.guaikei.com)
- [Skill options and parameters](artifact/references/options.md)
- [Skill changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown or text with structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public Douyin search, creator-post, comment, and trending-topic data; some results are saved locally by default.]

## Skill Version(s):

1.3.0 (source: server release, frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
