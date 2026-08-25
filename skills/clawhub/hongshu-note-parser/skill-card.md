## Description:

Parses a user-provided Xiaohongshu note link, downloads note content and images, and helps an agent produce an interactive capsule-card HTML analysis report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouq2039-lang](https://clawhub.ai/user/zhouq2039-lang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and brand or content teams use this skill to turn a single Xiaohongshu note into structured note data, AI-authored content and visual-strategy analysis, and a self-contained HTML report for competitive or campaign analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu note links, extracted content, and downloaded images may contain personal or sensitive information and are stored under the output directory.

Mitigation: Process only links explicitly provided by the user, avoid sensitive notes, and review or remove generated output files according to the user's data-handling needs.

Risk: The HTML report generator embeds image paths or image URLs from the analysis JSON.

Mitigation: Generate the analysis JSON through this workflow and review image references before rendering or sharing the HTML report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhouq2039-lang/skills/hongshu-note-parser)
- [Publisher profile](https://clawhub.ai/user/zhouq2039-lang)
- [README](artifact/README.md)
- [Skill instructions](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, json, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, structured JSON, downloaded image files, and self-contained HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes note data, downloaded images, and HTML reports under the configured output directory; no external API key is required.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
