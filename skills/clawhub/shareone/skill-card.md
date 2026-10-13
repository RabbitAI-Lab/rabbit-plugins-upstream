## Description:

Publishes HTML and Markdown pages and PDF, Word, or PowerPoint documents as ShareOne short links, with support for access controls, comments, downloads, and updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beep879](https://clawhub.ai/user/beep879)

### License/Terms of Use:

MIT

## Use Case:

Developers and other ShareOne users can publish agent-generated pages and documents as shareable links, manage access settings, and update or discuss existing shares.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Owner-authenticated collaborator or settings operations on untrusted full links may send an API key and sensitive settings to an untrusted origin.

Mitigation: Use known ShareOne links or explicit trusted endpoints for these operations; avoid full links from untrusted domains until URL-origin handling is fixed.

Risk: Publishing conversation or document content to a persistent public link may expose sensitive information.

Mitigation: Review and redact content before publishing, and provide a ShareOne API key only if you accept the associated access and publishing risks.

## Reference(s):

- [ShareOne skill release](https://clawhub.ai/beep879/skills/shareone)
- [ShareOne website](https://shareone.vip)
- [Publishing text pages](workflows/publish-text-page.md)
- [Credentials and environment](workflows/environment-and-credentials.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with share links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Published content may be available through persistent public links.]

## Skill Version(s):

1.10.1 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
