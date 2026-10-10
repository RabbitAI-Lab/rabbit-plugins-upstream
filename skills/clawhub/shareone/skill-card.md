## Description:

Publishes HTML and Markdown pages or PDF, Word, and PowerPoint documents as ShareOne short links, with options for access controls, comments, downloads, and updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beep879](https://clawhub.ai/user/beep879)

### License/Terms of Use:

MIT

## Use Case:

Developers and other users employ this skill to publish and manage shareable web pages and documents, including links for previews, collaboration, and client delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Collaborator or share-settings operations on a link supplied by an untrusted person may send a stored ShareOne API key to an attacker-controlled host.

Mitigation: Wait for URL-origin handling to be fixed before installing, or avoid these management operations on untrusted links.

Risk: Publishing can expose secrets or private material through a public, persistent link.

Mitigation: Review content before publishing; do not publish secrets, private documents, or sensitive conversation history.

## Reference(s):

- [ShareOne skill release](https://clawhub.ai/beep879/skills/shareone)
- [ShareOne website](https://shareone.vip)
- [Publishing text pages](workflows/publish-text-page.md)
- [Git-backed versions](workflows/git-backed-versions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with share links and optional commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public share links can have optional access controls and collaboration settings.]

## Skill Version(s):

1.7.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
