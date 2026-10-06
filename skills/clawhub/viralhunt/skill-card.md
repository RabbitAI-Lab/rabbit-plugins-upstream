## Description:

Helps teams discover trending content, create branded social posts, and draft, review, schedule, or publish them through ViralHunt-connected accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rodvan](https://clawhub.ai/user/rodvan)

### License/Terms of Use:

MIT-0

## Use Case:

Social media teams and their agents use ViralHunt to research emerging topics, prepare branded content for review, and schedule or publish posts to their connected accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A ViralHunt token may allow an agent to review, schedule, or publish content to connected social accounts.

Mitigation: Grant only the permissions needed, keep auto-approve reviewer tokens narrowly scoped, and monitor the review queue.

Risk: Rendering remote brand templates locally may expose the agent's browser environment.

Mitigation: Render in an isolated browser or container without a persistent profile, secrets, or private-network access.

## Reference(s):

- [ViralHunt API documentation](https://viralhunt.io/api)
- [ViralHunt skill listing](https://clawhub.ai/rodvan/skills/viralhunt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Images, Guidance]

**Output Format:** [Trend summaries, social post copy, drafts, and branded images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create drafts, reviews, scheduled posts, or published posts in connected accounts.]

## Skill Version(s):

1.6.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
