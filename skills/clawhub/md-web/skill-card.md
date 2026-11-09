## Description:

Publishes Markdown through the user's S3-compatible bucket as a public Docsify page and returns a shareable link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can publish a Markdown document to their own S3-compatible bucket as a public web page and share the generated link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bucket credentials are stored in plaintext in the local config file, and the security scan flags credential handling.

Mitigation: Keep credentials out of chat and version control; use the documented environment variables or a dedicated, bucket-scoped Object Read & Write token.

Risk: Published Markdown is public and its inline HTML can affect the rendered page; the security scan also flags possible content injection.

Mitigation: Review the document and its embedded markup before publishing, and publish only content from trusted sources.

Risk: Viewer setup overwrites shared files at the bucket root, and optional expiration changes the bucket lifecycle configuration.

Mitigation: Get explicit approval before setup or lifecycle changes, and confirm the bucket and retention scope before proceeding.

Risk: The security scan inspected only part of the listed components, so unreported components are not cleared by the scan.

Mitigation: Review the complete skill and its components before installation or use.

## Reference(s):

- [md-web project page](https://github.com/rockbenben/aishort-skills/tree/main/skills/md-web)

## Skill Output:

**Output Type(s):** [Text, URL]

**Output Format:** [Shareable URL to a public Docsify-rendered Markdown page]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The uploaded page is public; uploads remain available unless optional expiration is configured.]

## Skill Version(s):

1.3.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
