## Description:

Converts trusted Markdown files into mobile-friendly local HTML pages, with optional public URL preparation only after explicit user request and confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Developers, writers, and agent users use this skill to convert Markdown outputs, notes, tables, and code snippets into local HTML that is easier to read and share on mobile devices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML from untrusted Markdown may execute script through an unescaped code block language label.

Mitigation: Convert only trusted Markdown, or escape or allowlist code block language labels before opening or publishing generated HTML.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/md-out-of-chat)
- [Live web demo](https://2uf0a7axwwwr.space.minimaxi.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; generated artifacts are local HTML files or a local deployable folder.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3. Public URL workflows require explicit user request, explicit confirmation, and an available trusted deploy tool.]

## Skill Version(s):

1.5.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
