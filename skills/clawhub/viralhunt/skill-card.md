## Description:

Helps teams discover rising social content, plan and create branded posts, review drafts, and schedule or publish to their connected accounts through ViralHunt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rodvan](https://clawhub.ai/user/rodvan)

### License/Terms of Use:

MIT-0

## Use Case:

Social media teams and their agents use ViralHunt to research trends, prepare branded posts and translations, manage draft reviews, and publish or schedule posts on authorized connected accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A token with publishing permissions can send content to connected social accounts.

Mitigation: Use narrowly scoped tokens and require explicit confirmation before normal publish or approve actions.

Risk: An approved review can release a post without a separate per-post prompt when automated reviewer or auto-approve settings are enabled.

Mitigation: Keep writer and reviewer tokens separate, review automation settings carefully, and require human review when appropriate.

## Reference(s):

- [ViralHunt API documentation](https://viralhunt.io/api)
- [ViralHunt ClawHub release](https://clawhub.ai/rodvan/skills/viralhunt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Conversational guidance and structured post drafts, with API request examples when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report research findings, draft or review outcomes, and publishing status for connected accounts.]

## Skill Version(s):

1.6.21 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
