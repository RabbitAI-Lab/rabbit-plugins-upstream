## Description:

A Douyin operations assistant that searches public posts, creator works, comments, and trending lists, returning structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content operators and analysts use the skill to retrieve public Douyin content, monitor creator accounts and comments, and track trends for topic research and sentiment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and links are sent to the third-party service at guaikei.com.

Mitigation: Send only queries you are comfortable sharing, and review the provider's pricing and data-handling terms.

Risk: The API token requires protection, and saved logs retain original inputs and retrieved results without automatic expiry.

Mitigation: Protect the API token and delete saved logs when they are no longer needed.

## Reference(s):

- [Service and API information](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON data]

**Output Format:** [Structured JSON records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records may include authors, engagement metrics, tags, and links; results are saved locally.]

## Skill Version(s):

1.4.0 (source: server-resolved release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
