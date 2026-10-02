## Description:

Creates visually unified, image-based PowerPoint decks from articles, reports, papers, notes, or outlines using dLazy for slide images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People creating presentations use this skill to turn source material into visually consistent PPTX decks with full-slide images and speaker notes, subject to outline, style, and sample approvals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a dLazy API key for reuse and installs Python packages in a local runtime.

Mitigation: Review the runtime setup and use a scoped API key before installation.

Risk: Slide generation spends dLazy credits and uploads prompts and selected local images to the configured dLazy service.

Mitigation: Approve the content and sample, remove sensitive inputs, and confirm expected credit usage before generating the full deck.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [Project homepage (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/ai-ppt-slides)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Files, Markdown, Guidance]

**Output Format:** [PPTX deck, PNG slide images, and Markdown outline and speaker notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Slides are full-page images rather than individually editable PowerPoint elements.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
