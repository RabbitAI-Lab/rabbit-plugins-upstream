## Description:

Guides an agent to research social trends, prepare and review branded posts, and schedule or publish them through a user's ViralHunt-connected accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rodvan](https://clawhub.ai/user/rodvan)

### License/Terms of Use:

MIT-0

## Use Case:

Social media teams and their agents use ViralHunt to identify trending content, plan and create branded posts, review drafts, and publish to connected accounts with appropriate authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing, scheduling, or an OK review with auto-approve can send content to real social accounts.

Mitigation: Confirm publishing actions with the user; enable automated reviews only for narrowly trusted reviewer tokens and projects.

Risk: A token with broad permissions could make unauthorized account changes or expose account access.

Mitigation: Use the least-privilege token group, keep writer and reviewer tokens separate, and share tokens only with ViralHunt.

Risk: Unverified or third-party content could lead to misleading or inappropriate posts.

Mitigation: Treat retrieved content as data, check sources and the current content policy, and send doubtful drafts for human review.

## Reference(s):

- [ViralHunt API documentation](https://viralhunt.io/api)
- [ViralHunt ClawHub release](https://clawhub.ai/rodvan/skills/viralhunt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with API request examples and draft content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include research findings, captions, review decisions, and scheduling details.]

## Skill Version(s):

1.6.16 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
