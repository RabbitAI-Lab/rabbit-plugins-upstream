## Description:

Creates visually consistent, image-based PowerPoint decks from articles, reports, papers, notes, or outlines using dLazy to generate each slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, creators, and developers use this skill to turn source materials into visually unified presentation decks with generated slide images, an outline, and speaker notes. It is suited to image-based slides rather than independently editable slide elements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Slide prompts and attached images are uploaded to dLazy.

Mitigation: Use only content approved for sharing with dLazy; avoid private or regulated material unless the service is approved for that data.

Risk: The skill can store an API key and set up a persistent shared runtime.

Mitigation: Use a revocable dLazy key, isolate the runtime directory with DLAZY_PPT_HOME, and review the bootstrap before installing dependencies.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [Project homepage (listed in skill metadata)](https://github.com/dlazy-ai/ai-ppt-slides)

## Skill Output:

**Output Type(s):** [Files, Markdown, Text]

**Output Format:** [PowerPoint (.pptx), PNG slide images, Markdown outline and speaker notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Slides are full-page 16:9 images, not individually editable PowerPoint elements.]

## Skill Version(s):

1.0.20 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
