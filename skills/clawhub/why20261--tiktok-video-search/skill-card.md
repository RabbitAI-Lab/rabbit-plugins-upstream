## Description:

Searches public TikTok videos by keyword and retrieves creator posts or video comments for content and audience analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and analysts use this skill to find popular public TikTok videos, examine a creator's posts, and review public comments for content research and competitor analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and the API token are sent to a third-party data service.

Mitigation: Use the skill only if sharing query targets with guaikei.com is acceptable; protect the API token as a credential.

Risk: Temporary JSON logs may contain public usernames, comments, links, and engagement data.

Mitigation: Collect only needed public data, restrict access to saved results, and delete logs when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/tiktok-video-search)
- [Command options and result format](references/options.md)
- [Guaikei API service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries grounded in structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include public video links, engagement metrics, comments, and notices about empty results or parameter fallbacks.]

## Skill Version(s):

1.0.0 (source: skill frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
