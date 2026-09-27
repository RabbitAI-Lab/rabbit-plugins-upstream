## Description:

Publishes HTML and Markdown pages or PDF, Word, and PowerPoint documents as ShareOne links, with options for access controls, comments, downloads, and updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beep879](https://clawhub.ai/user/beep879)

### License/Terms of Use:

MIT

## Use Case:

Developers and other ShareOne users can publish generated pages and documents as shareable links, manage access settings, and collaborate through comments on text pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing selected files, generated content, or conversation excerpts can expose private data through hosted links.

Mitigation: Review content before upload; omit secrets and private data, and use passwords or watermarks when appropriate.

Risk: Authenticated settings and collaborator actions may send the saved API key to the origin of a supplied full URL.

Mitigation: Verify link origins before authenticated actions and avoid non-ShareOne or unfamiliar full URLs.

## Reference(s):

- [ShareOne website](https://shareone.vip)
- [ShareOne skill release](https://clawhub.ai/beep879/skills/shareone)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or text with ShareOne links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include public share links and instructions for access or updates.]

## Skill Version(s):

1.3.3 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
