## Description:

PostLake analytics reads per-post and normalized cross-platform social media performance metrics, including impressions, reach, engagement, CTR, and follower growth, so agents can report results or recommend what to post next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[postlake](https://clawhub.ai/user/postlake)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and operators use this skill to retrieve PostLake social analytics, summarize per-post performance, compare platform results over 7, 30, or 90 days, and choose what to post next.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires POSTLAKE_API_KEY, which is sensitive account credential material.

Mitigation: Provide the key only to agents that should read PostLake analytics, and scope or rotate it according to PostLake account controls.

Risk: Analytics may lag for a few hours after posting, so very recent results can be incomplete.

Mitigation: Call out freshness limits when summarizing recent posts and re-check metrics after platform reporting catches up.

## Reference(s):

- [PostLake analytics Skill on ClawHub](https://clawhub.ai/postlake/skills/postlake-analytics)
- [PostLake publisher profile](https://clawhub.ai/user/postlake)
- [PostLake API base URL](https://api.postlake.dev)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline API request examples and concise analysis guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires POSTLAKE_API_KEY and reads analytics from the PostLake API; metrics may lag by a few hours after posting.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
