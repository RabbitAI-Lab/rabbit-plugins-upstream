## Description:

Publishes HTML and Markdown pages or PDF, Word, and PowerPoint documents to ShareOne short links and helps manage access settings, comments, downloads, and updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beep879](https://clawhub.ai/user/beep879)

### License/Terms of Use:

MIT

## Use Case:

Developers and other ShareOne users can publish pages and documents as shareable links, set access controls, and handle comments or content updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A supplied link may cause ShareOne credentials to be sent to an unintended host.

Mitigation: Use canonical ShareOne links or an explicitly trusted base URL; avoid collaborator and settings changes through unknown full URLs, and keep keys scoped or disposable until host validation is fixed.

Risk: Share deletion lacks an executable confirmation gate.

Mitigation: Confirm the target and obtain explicit user approval before deleting a share.

Risk: A persistent notification watcher can act beyond the intended share or run an untrusted handler.

Mitigation: Enable it only for a chosen project and share scope with a trusted handler command.

## Reference(s):

- [ShareOne skill on ClawHub](https://clawhub.ai/beep879/skills/shareone)
- [ShareOne website](https://shareone.vip)
- [ShareOne skill documentation](artifact/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with ShareOne short links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report publishing, access settings, download, update, or comment results.]

## Skill Version(s):

1.11.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
