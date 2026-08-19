## Description:

Creates HTML slide decks through a guided briefing workflow, validates each page against the bundled HTML-to-PPTX specification, and converts validated slides into PowerPoint files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cqcmj74](https://clawhub.ai/user/cqcmj74)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to interview stakeholders, create standards-compliant HTML slide decks, validate layout and design constraints, and convert the result to PPTX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote image URLs in slide HTML can be fetched during conversion.

Mitigation: Review slide HTML and assets for remote image references before running conversion, and use trusted local assets when possible.

Risk: Local file paths referenced by slide HTML can be embedded into generated PPTX files.

Mitigation: Check for file:// URLs and absolute local paths before conversion, especially when working with sensitive material.

Risk: Cached slide artifacts may retain sensitive content.

Mitigation: Clear or disable slides/.cache when converting confidential decks.

## Reference(s):

- [HTML Conversion Specification](reference/html-spec.md)
- [Design Principles](reference/design-principles.md)
- [Interview Guide](reference/interview-guide.md)
- [Theme Presets](reference/theme-presets.md)
- [Snippet Index](assets/snippets/INDEX.md)
- [ClawHub Skill Page](https://clawhub.ai/cqcmj74/skills/html-slides-to-pptx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Guided Markdown responses plus generated HTML, CSS, JSON configuration, validation commands, and PPTX files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires node and npm; conversion depends on the bundled slide validation and PPTX conversion scripts.]

## Skill Version(s):

2.1.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
