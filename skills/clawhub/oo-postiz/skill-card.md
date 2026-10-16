## Description:

Helps an agent manage posts, connected channels, and media in a user's Postiz account through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

People managing social media use this skill to review connected Postiz channels and posts, create drafts, publish or schedule content, and import media through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creating, publishing, or scheduling a post, or importing media, changes the connected Postiz account.

Mitigation: Review the exact payload and expected effect with the user before approving a write action.

Risk: The optional first-time setup includes a command that downloads and runs a CLI installer.

Mitigation: Install only when needed, after verifying the publisher and checking the official installation guide or a verified package.

## Reference(s):

- [Postiz skill on ClawHub](https://clawhub.ai/oomol/skills/oo-postiz)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Postiz](https://postiz.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Plain text with optional JSON action results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can report connected channels, posts, publishing outcomes, and media-import results.]

## Skill Version(s):

1.0.1 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
