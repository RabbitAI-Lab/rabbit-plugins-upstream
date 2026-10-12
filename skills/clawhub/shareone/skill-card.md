## Description:

Publishes HTML and Markdown pages and shares PDF, Word, and PowerPoint documents through ShareOne short links, with options for access controls, updates, and comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beep879](https://clawhub.ai/user/beep879)

### License/Terms of Use:

MIT

## Use Case:

Developers and other ShareOne users use this skill to publish pages and documents as shareable links, manage access settings, update content, and handle feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An authenticated delete helper can invalidate shares without enforcing the documented confirmation step.

Mitigation: Explicitly confirm each share deletion with the user before running the helper; add a confirmation check to the wrapper or script.

Risk: Account credentials and changes to collaborators or share settings can affect access to content.

Mitigation: Protect the API key and confirm collaborator and settings changes before applying them.

Risk: A long-lived comment watcher can continue processing events beyond the intended session.

Mitigation: Run it only with a chosen handler or session and stop it when no longer needed.

## Reference(s):

- [ShareOne skill release](https://clawhub.ai/beep879/skills/shareone)
- [ShareOne website](https://shareone.vip)
- [ShareOne skill documentation](SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Share links, Shell commands]

**Output Format:** [Text or Markdown with ShareOne links and optional commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include published content, download links, or comment summaries.]

## Skill Version(s):

1.9.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
