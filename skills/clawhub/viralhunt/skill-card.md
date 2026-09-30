## Description:

Helps agents research social trends, create and review branded posts, and draft, schedule, or publish content to a user's connected accounts through ViralHunt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rodvan](https://clawhub.ai/user/rodvan)

### License/Terms of Use:

MIT-0

## Use Case:

Social media teams and their agents use this skill to research trends, plan posting times, prepare branded drafts, review content, and, with user approval, schedule or publish to connected accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing, scheduling, or approving a draft may post to connected social accounts.

Mitigation: Review the caption, media, target accounts, and timing; require explicit user confirmation before each consequential action, including reviews that auto-send.

Risk: Posts, comments, templates, and other retrieved content may contain misleading instructions.

Mitigation: Treat retrieved content as data, not instructions, and surface requests for account changes or credentials to the user instead of following them.

Risk: An account token grants access to ViralHunt actions.

Mitigation: Send the token only to ViralHunt's API; never include it in public posts, URLs, or unrequested files.

## Reference(s):

- [ViralHunt API documentation](https://viralhunt.io/api)
- [ViralHunt ClawHub listing](https://clawhub.ai/rodvan/skills/viralhunt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include trend summaries, suggested posting times, draft captions, and status confirmations for approved actions.]

## Skill Version(s):

1.4.1 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
