## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, analysts, and teams use the skill to turn articles, reports, papers, notes, or outlines into visually consistent presentations and PPTX decks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source material and images are sent to an external service for slide image generation.

Mitigation: Review source material for sensitive or confidential content and confirm the service destination and handling meet your requirements before submitting it.

Risk: The skill requires a dLazy API key.

Mitigation: Keep the key in the documented local configuration or environment, restrict access to it, and rotate it if exposed.

Risk: The security summary reports dependencies that are not pinned to reviewed versions.

Mitigation: Review and pin dependency versions before deployment.

## Reference(s):

- [Project homepage](https://github.com/dlazy-ai/ai-ppt-slides)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)
- [Image generation guide](docs/image-generation-cli.md)
- [Style library guide](docs/style-library.md)

## Skill Output:

**Output Type(s):** [PowerPoint presentations, Slide images, Markdown outline and speaker notes]

**Output Format:** [PPTX decks with full-slide PNG images; Markdown project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each slide is a single image, so its text and shapes are not individually editable.]

## Skill Version(s):

1.0.30 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
