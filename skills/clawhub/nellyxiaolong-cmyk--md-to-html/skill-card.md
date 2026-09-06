## Description:

Convert Markdown (.md) files to styled, self-contained HTML pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nellyxiaolong-cmyk](https://clawhub.ai/user/nellyxiaolong-cmyk)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical writers use this skill to convert local Markdown documents, notes, READMEs, and API documentation into standalone styled HTML for viewing or sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML from untrusted Markdown can execute scripts when opened in a browser.

Mitigation: Use the skill only with trusted Markdown, or fix the converter to escape or sanitize inline content and add a restrictive Content Security Policy before opening or sharing generated HTML.

## Reference(s):

- [Skill documentation](SKILL.md)
- [Markdown conversion script](scripts/md2html.py)
- [ClawHub skill page](https://clawhub.ai/nellyxiaolong-cmyk/skills/md-to-html)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Text]

**Output Format:** [Standalone HTML file plus a concise text status report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated HTML embeds CSS and has no external runtime dependencies; output path defaults to <input>.html when omitted.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
