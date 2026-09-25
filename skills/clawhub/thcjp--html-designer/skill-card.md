## Description:

HTML设计工具 helps agents produce and improve HTML/CSS page layouts, visual design code, and design-review guidance for web and UI/UX work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and agent users can use this skill to generate HTML/CSS layout code, review typography and spacing, and receive practical visual-design improvements for web pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad file, command, API, and credential authority for a design-helper workflow.

Mitigation: Install and run it only in a controlled workspace with explicit approval for shell commands, outbound API use, and file writes.

Risk: The artifact includes API-key setup guidance without identifying a concrete required external service.

Mitigation: Do not provide real API keys unless the service requirement is confirmed and the key can be scoped, rotated, and kept out of version control.

Risk: Generated HTML/CSS or design advice may be inaccurate, inaccessible, or unsuitable for production.

Mitigation: Review generated code and guidance for accessibility, browser compatibility, security, and project design requirements before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/html-designer)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON examples, shell command snippets, and HTML/CSS code guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose file edits, command execution steps, API-key configuration, and design recommendations that should be reviewed before use.]

## Skill Version(s):

1.0.1 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
