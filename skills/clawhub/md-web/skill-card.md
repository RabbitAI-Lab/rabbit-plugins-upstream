## Description:

MD Web turns markdown into a public, shareable Docsify web page by uploading it to a user-configured S3-compatible bucket.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use MD Web when they want an agent to publish markdown as a public web page or return a shareable link instead of pasting long content into chat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded markdown is publicly accessible at the returned URL.

Mitigation: Use the skill only for content intended for public sharing, and do not upload secrets, private notes, API keys, personal data, or confidential material.

Risk: S3 access keys are stored in plaintext in the user's md-web configuration file.

Mitigation: Use a narrowly scoped token for a dedicated bucket, keep the local configuration file private, and avoid committing or sharing it.

Risk: The skill can change bucket lifecycle settings, and expire_days: 0 clears the bucket lifecycle configuration.

Mitigation: Use a dedicated bucket and avoid Admin Read & Write permissions unless automatic expiry management is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rockbenben/skills/md-web)
- [Project homepage](https://github.com/rockbenben/aishort-skills/tree/main/skills/md-web)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown response containing a filename and clickable public URL, with shell commands or configuration JSON during setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Success output is a public URL; uploaded markdown is rendered by Docsify from user-owned S3-compatible storage.]

## Skill Version(s):

1.1.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
