## Description:

Helps agents research trending social content, prepare branded drafts, review posts, and schedule or publish to a user's connected accounts through ViralHunt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rodvan](https://clawhub.ai/user/rodvan)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and account holders use this skill to research social trends, create and review branded posts, and publish or schedule approved content on their connected social accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing or approving a review may release content to connected social accounts.

Mitigation: Preview content, accounts and timing; get explicit approval for consequential actions and enable auto-approve or reviewer jobs only when intended.

Risk: An account token can authorize actions on the user's behalf.

Mitigation: Use a least-privilege token, send it only to ViralHunt, and rotate it if exposed.

Risk: Third-party posts and templates may contain misleading content or instructions.

Mitigation: Treat retrieved material as data, verify claims and rights, and review drafts against the current content policy.

## Reference(s):

- [ViralHunt API documentation](https://viralhunt.io/api)
- [ViralHunt skill on ClawHub](https://clawhub.ai/rodvan/skills/viralhunt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with post drafts, API examples, and publishing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can propose content and review decisions for the user's connected social accounts.]

## Skill Version(s):

1.6.11 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
