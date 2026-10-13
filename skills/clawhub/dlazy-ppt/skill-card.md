## Description:

Creates visually consistent, image-based PowerPoint presentations from articles, reports, papers, notes, or outlines using dLazy to generate each slide.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Presentation creators use this skill to turn source material into a visually unified PowerPoint deck with generated slide images, an outline, and optional speaker notes. It suits presentations that do not require individually editable text or graphics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deck prompts and selected local images are sent to dLazy for slide generation.

Mitigation: Review confidential source material and selected images before generating slides.

Risk: The skill uses a dLazy API key stored in a shared local runtime.

Mitigation: Control access to the shared runtime and use a dedicated key that can be rotated or revoked.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [Project documentation (homepage listed in skill metadata)](https://github.com/dlazy-ai/ai-ppt-slides)
- [dLazy API key configuration](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Files, Markdown, Guidance]

**Output Format:** [PowerPoint (.pptx), PNG slide images, and Markdown outline and speaker notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Slides are full-page images rather than individually editable presentation elements.]

## Skill Version(s):

1.0.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
