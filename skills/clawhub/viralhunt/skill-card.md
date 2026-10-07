## Description:

Helps teams discover rising social content, prepare on-brand drafts, review posts, and schedule or publish to their connected accounts through ViralHunt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rodvan](https://clawhub.ai/user/rodvan)

### License/Terms of Use:

MIT-0

## Use Case:

Social media teams and their agents use ViralHunt to research trends, prepare branded posts for review, and schedule or publish approved content across connected accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can schedule or publish content to connected social accounts.

Mitigation: Review the caption, media, accounts, and timing before authorizing each publishing action.

Risk: A recurring reviewer job or trusted Team setting can release scheduled posts after an agent approves them without fresh per-post chat confirmation.

Mitigation: Enable automated reviews only when intended, restrict who can approve releases, and check review rules and queued posts before activation.

## Reference(s):

- [ViralHunt API documentation](https://viralhunt.io/api)
- [ViralHunt skill listing](https://clawhub.ai/rodvan/skills/viralhunt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Images, Guidance]

**Output Format:** [Conversational text and Markdown, with API request examples and optional branded images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create drafts, review decisions, and scheduled or published posts on connected accounts.]

## Skill Version(s):

1.6.3 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
