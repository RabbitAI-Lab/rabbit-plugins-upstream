## Description:

Generates terminal, HTML, and SVG charts from simple data inputs, including bar, line, pie, table, sparkline, dashboard, progress, and heatmap views.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongbai233](https://clawhub.ai/user/kongbai233)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and other external users use this skill to generate quick terminal visualizations and shareable HTML or SVG chart files from simple inline data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML or SVG files may contain unescaped chart labels or titles from user-provided data.

Mitigation: Use trusted chart data, avoid publishing generated files from untrusted inputs, and review or sanitize HTML/XML text before opening or sharing the output.

Risk: Chart generation can write files to output paths or local data directories.

Mitigation: Run the skill in a sandboxed workspace and confirm output paths before execution.

## Reference(s):

- [Chart Generator ClawHub listing](https://clawhub.ai/kongbai233/skills/chart-generator-2-0-0)
- [BytesAgain homepage](https://bytesagain.com)
- [Data visualization best practices](tips.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Terminal text, Markdown guidance, shell command examples, and generated HTML/SVG chart files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write chart files to user-selected output paths or the current directory and may persist local chart history.]

## Skill Version(s):

1.0.0 (source: server release metadata; packaged skill frontmatter version: 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
