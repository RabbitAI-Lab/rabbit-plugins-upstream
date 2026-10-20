## Description:

Generates visually consistent, image-based PowerPoint decks from articles, reports, papers, notes, or outlines using dLazy for slide images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Presentation creators use this skill to turn source material into a unified slide deck with generated images and presenter notes. Slides are full-page images rather than individually editable text and shapes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Slide prompts and any attached source images are sent to the configured dLazy service.

Mitigation: Review content and obtain approval before sending sensitive material to the service.

Risk: The dLazy API key is stored locally in a shared runtime configuration.

Mitigation: Protect local access to the key and use a dedicated credential where appropriate.

Risk: The workflow installs Python dependencies into a shared runtime.

Mitigation: Review the listed dependencies and use an isolated environment when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [Project documentation (declared homepage; not verified import provenance)](https://github.com/dlazy-ai/ai-ppt-slides)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Markdown, Configuration guidance, Shell commands]

**Output Format:** [Text and Markdown guidance with paths to generated slide images and a PowerPoint deck]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow also saves a PPTX deck, slide PNGs, an outline, and optional presenter notes as project files.]

## Skill Version(s):

1.0.23 (source: ClawHub release metadata; artifact frontmatter states 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
