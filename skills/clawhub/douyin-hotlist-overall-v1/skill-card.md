## Description:

Provides read-only access to public Douyin search, trending lists, creator posts, and video comments, returning structured JSON for content and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use it to search public Douyin content, retrieve trending lists, review creator posts and comments, and support short-video topic research, competitor monitoring, and public-opinion analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup terms and links are sent to the third-party Guaikei data API.

Mitigation: Only submit search terms and links that are appropriate to share with that provider.

Risk: The API token could be exposed or API usage could incur charges.

Mitigation: Protect the API token and check the provider's pricing before use.

Risk: Request details and results remain in local logs.

Mitigation: Review saved logs and remove them when they are no longer needed.

## Reference(s):

- [Guaikei data API](https://www.guaikei.com)
- [Release changelog](references/changelog.md)
- [Release page](https://clawhub.ai/why20261/skills/douyin-hotlist-overall-v1)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [Structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search, creator-post, comment, and trending-list records; request details and results are also saved in local logs.]

## Skill Version(s):

1.4.0 (source: server release metadata, changelog, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
