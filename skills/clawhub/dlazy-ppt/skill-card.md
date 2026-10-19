## Description:

Generates visually unified, image-based PowerPoint decks from articles, reports, papers, notes, or outlines using dLazy for slide images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Presentation creators use this skill to turn source material into a cohesive image-based slide deck with an outline and optional speaker notes. Slides are not individually editable as text or shapes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Slide prompts and supplied images are uploaded to dLazy or a configured service.

Mitigation: Avoid sensitive source images unless necessary and review the service destination before use.

Risk: The skill stores a dLazy API key and sets up a local runtime with installed Python packages.

Mitigation: Use a scoped key, review the local setup, and rotate or revoke the key when no longer needed.

Risk: Generated files may be written to a default project location.

Mitigation: Choose an explicit output directory before generating a deck.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [Project homepage](https://github.com/dlazy-ai/ai-ppt-slides)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Files, Markdown, Guidance]

**Output Format:** [PPTX presentation, PNG slide images, and Markdown outline and speaker notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Slides are full-slide images rather than separately editable elements.]

## Skill Version(s):

1.0.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
