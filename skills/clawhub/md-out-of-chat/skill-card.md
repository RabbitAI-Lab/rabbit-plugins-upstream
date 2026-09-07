## Description:

Converts an explicitly named Markdown file into a mobile-friendly local HTML page, with public URL sharing only after a separate user request and confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Developers, employees, and external users can use this skill when an agent needs to turn a named Markdown report, note, or chat export into a phone-readable HTML file for local viewing or user-confirmed sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local converter reads the Markdown file the user names and may embed same-folder image files referenced by that Markdown.

Mitigation: Use the skill only with files the user explicitly identifies, and review embedded local image paths logged during conversion.

Risk: A public URL could expose Markdown content if sharing is requested.

Mitigation: Generate public sharing output only after the user separately requests it and confirms what will be published.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/md-out-of-chat)
- [Live web demo](https://2uf0a7axwwwr.space.minimaxi.com)

## Skill Output:

**Output Type(s):** [Files, Markdown, Shell commands, Guidance]

**Output Format:** [Local HTML file path or user-confirmed public URL guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default output is a local HTML file; public sharing is opt-in and requires explicit user confirmation.]

## Skill Version(s):

1.5.2 (source: server-resolved release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
