## Description:

Convert Markdown articles into LinkedIn-ready rich text while preserving formatting and preparing tables and images for pasting into the article editor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and writers use the skill to turn a Markdown article draft into formatted content for LinkedIn's article editor, with options for tables, images, and code blocks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags a risk of network activity when rendering untrusted table content in Chromium, which is reported to run without its sandbox; the scan evidence is incomplete.

Mitigation: Review the security guidance before converting untrusted articles or tables, and avoid processing untrusted table content until the rendering risk is addressed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/j3ffyang/skills/md-to-linkedin)

## Skill Output:

**Output Type(s):** [HTML, Files, Rich text]

**Output Format:** [HTML rich-text fragment for pasting, with an HTML file and optional table images or DOCX]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves article formatting; tables can be flattened to lists or rendered as images, and local images can be embedded.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
