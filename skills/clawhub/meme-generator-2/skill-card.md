## Description:

Generate SVG-based memes from text with classic templates, batch generation, quote packs, animated effects, and optional HTML export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Developers, creators, and automation agents use this skill to generate lightweight SVG memes from prompt text, quote packs, built-in meme templates, or trusted custom SVG templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected output paths can write generated SVG or HTML files outside the intended folder.

Mitigation: Review output and output-dir values before running single, batch, quote-generation, or HTML export commands.

Risk: Custom templates read a local SVG file and carry that template content into generated output.

Mitigation: Use custom SVG templates from trusted sources and inspect generated SVG or HTML before sharing it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/meme-generator-2)
- [Source Repository](https://github.com/voronindenis5/meme-generator)
- [SVG Text Rendering Guide](references/svg-text.md)
- [Template Reference Guide](references/templates.md)

## Skill Output:

**Output Type(s):** [text, code, shell commands, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands; generated SVG files and optional HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline output by default; batch mode can create multiple files in a user-selected directory.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
