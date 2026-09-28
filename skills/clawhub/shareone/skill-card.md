## Description:

Publishes HTML and Markdown pages or PDF, Word, and PowerPoint documents to ShareOne short links and helps manage access settings, comments, downloads, and updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beep879](https://clawhub.ai/user/beep879)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other ShareOne users can publish web pages and documents as short links, manage sharing settings, and collaborate on text-page feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some collaborator and settings workflows can send a ShareOne API key to a host taken from an untrusted full link.

Mitigation: For these workflows, use bare share IDs or slugs, or links from known ShareOne domains; rotate the key if it may have been used with a suspicious link.

Risk: Published content and API credentials are entrusted to an external hosting service.

Mitigation: Review material before publishing, use access controls where appropriate, and provide an API key only if comfortable with ShareOne handling it.

## Reference(s):

- [ShareOne website](https://shareone.vip)
- [ShareOne skill on ClawHub](https://clawhub.ai/beep879/skills/shareone)

## Skill Output:

**Output Type(s):** [Text, Markdown, URLs, Shell commands]

**Output Format:** [Markdown with ShareOne links and optional command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Links can have access passwords, watermarks, and comments; published content is hosted by ShareOne.]

## Skill Version(s):

1.3.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
