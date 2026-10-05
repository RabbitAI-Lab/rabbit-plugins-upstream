## Description:

Helps agents research social trends, create and review branded posts, and publish or schedule content to a user's connected accounts through ViralHunt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rodvan](https://clawhub.ai/user/rodvan)

### License/Terms of Use:

MIT-0

## Use Case:

Content teams and their agents use ViralHunt to research trends, prepare and review on-brand drafts, and publish or schedule posts to connected social accounts with user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A publishing action may send content to the wrong account, at the wrong time, or with unreviewed copy or media.

Mitigation: Show the exact caption, media, accounts and time, then obtain the user's explicit approval before publishing or scheduling.

Risk: An OK review may publish a post when the organization has auto-approval enabled.

Mitigation: Check whether auto-approval is enabled and treat an OK review as a publishing action requiring explicit user approval.

Risk: A ViralHunt token grants access to account research and potentially connected publishing workflows.

Mitigation: Use a token with the least role needed and share it only with ViralHunt.

## Reference(s):

- [ViralHunt API documentation](https://viralhunt.io/api)
- [ViralHunt on ClawHub](https://clawhub.ai/rodvan/skills/viralhunt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown with draft post copy and optional commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can prepare branded draft content and advise on scheduling or publishing to connected accounts.]

## Skill Version(s):

1.5.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
