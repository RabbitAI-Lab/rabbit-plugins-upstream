## Description:

Generates visually unified image-based PowerPoint decks from articles, reports, papers, notes, or outlines using dLazy for slide images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Presentation creators use this skill to turn source material into visually consistent image-based PowerPoint decks with slide images and optional speaker notes. It is not suited to decks requiring individually editable slide elements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Slide prompts and attached source images may be uploaded to the configured dLazy service.

Mitigation: Review source material for sensitive content and approve service use before generating slides.

Risk: Slide generation consumes organization credits.

Mitigation: Confirm expected slide count and credit budget before running generation.

Risk: Local runtime and API-key configuration may persist under ~/.dlazy-ppt.

Mitigation: Protect local credentials and set DLAZY_PPT_HOME when a different storage location is required.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [Declared skill documentation and examples](https://github.com/dlazy-ai/ai-ppt-slides)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Files, Markdown, Guidance]

**Output Format:** [PowerPoint (.pptx), PNG slide images, and Markdown outline or speaker notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Slides are full-page images rather than separately editable PowerPoint elements.]

## Skill Version(s):

1.0.18 (source: ClawHub release; bundled skill frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
