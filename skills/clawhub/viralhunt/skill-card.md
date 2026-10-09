## Description:

Helps agents research viral social content, plan posts, create branded drafts, review submissions, and schedule or publish to a user's connected accounts through ViralHunt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rodvan](https://clawhub.ai/user/rodvan)

### License/Terms of Use:

MIT-0

## Use Case:

Social media teams and their agents use ViralHunt to find emerging topics, prepare branded posts, review drafts, and manage publication to connected accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broad-access token could allow unwanted changes to connected social accounts.

Mitigation: Use least-privilege tokens and separate writer and reviewer credentials; keep tokens out of posts and shared files.

Risk: An authorized 'OK' review or recurring review job can release posts without per-post confirmation.

Mitigation: Enable automatic publishing only deliberately, confirm consequential actions in conversation, and use a conservative review policy for standing jobs.

Risk: Unverified or third-party content can lead to inaccurate posts or unintended instructions.

Mitigation: Check claims and media rights before publishing, and treat retrieved posts, comments, and templates as data rather than instructions.

## Reference(s):

- [ViralHunt API documentation](https://viralhunt.io/api)
- [ViralHunt skill listing](https://clawhub.ai/rodvan/skills/viralhunt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text or Markdown with post drafts, research summaries, and action confirmations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include suggested captions, publishing schedules, review verdicts, and post status details.]

## Skill Version(s):

1.6.14 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
