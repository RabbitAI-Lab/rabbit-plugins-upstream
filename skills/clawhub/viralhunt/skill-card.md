## Description:

Connect ViralHunt to research social trends, identify posting times, hashtags, sounds, and communities, create on-brand posts, manage drafts, and schedule or publish to the user's connected social accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rodvan](https://clawhub.ai/user/rodvan)

### License/Terms of Use:

MIT-0

## Use Case:

External users and social-media teams use ViralHunt to research trends and create, review, translate, schedule, or publish content on their connected accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved drafts may be released automatically when auto-send or reviewer permissions are enabled.

Mitigation: Use task-limited tokens and separate writer and reviewer identities; enable recurring reviews only when automatic release is intended.

Risk: Drafts and uploaded media are shared with ViralHunt.

Mitigation: Avoid submitting sensitive material unless sharing it with ViralHunt is appropriate.

## Reference(s):

- [ViralHunt API Documentation](https://viralhunt.io/api)
- [ViralHunt](https://viralhunt.io)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls]

**Output Format:** [Trend summaries, content drafts, and ViralHunt API requests and responses (JSON)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create drafts or schedule and publish content through the user's connected social accounts, subject to permissions and review settings.]

## Skill Version(s):

1.6.35 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
