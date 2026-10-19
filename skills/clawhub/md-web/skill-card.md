## Description:

Publishes Markdown files to a user-configured S3-compatible bucket and returns shareable public web page links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

People who need to share Markdown documents as web pages can publish them to their own public S3-compatible bucket and receive a link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Published documents are publicly accessible and may expose sensitive information.

Mitigation: Publish only with the user's explicit approval; exclude secrets and personal information.

Risk: Stored bucket credentials may be exposed if the configuration file is shared.

Mitigation: Prefer environment variables for credentials and protect any local configuration file.

Risk: Bucket administration permissions can affect content beyond the published documents.

Mitigation: Use a dedicated public-documents bucket and Object Read & Write credentials; grant Admin Read & Write only when intentionally enabling expiry.

Risk: Content on the published domain is public and untrusted.

Mitigation: Treat the published domain as untrusted and avoid relying on it for private content.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/rockbenben/skills/md-web)
- [Skill homepage (declared in metadata)](https://github.com/rockbenben/aishort-skills/tree/main/skills/md-web)

## Skill Output:

**Output Type(s):** [Markdown, Text, Configuration guidance]

**Output Format:** [Markdown document and public web page URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Published documents are publicly accessible; the agent returns a link after upload.]

## Skill Version(s):

1.2.2 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
