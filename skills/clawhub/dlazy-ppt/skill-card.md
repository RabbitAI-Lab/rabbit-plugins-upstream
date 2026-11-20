## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and teams can turn articles, reports, papers, notes, or outlines into visually unified, image-based PowerPoint presentations; each slide is a full-page image rather than separately editable text and shapes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A possible API-key exposure path is reported.

Mitigation: Store DLAZY_API_KEY securely, keep it out of source files and slide prompts, and rotate it if exposure is suspected.

Risk: Slide source content and supplied assets may be transferred to dLazy for image generation.

Mitigation: Avoid sending sensitive material unless the transfer is approved; check the configured endpoint before use.

Risk: Dependency versions are not fixed, and scanner analysis was partial because some referenced paths could not be resolved.

Mitigation: Review unresolved references and dependency versions before deployment, and pin dependencies where reproducibility is required.

## Reference(s):

- [Project documentation](https://github.com/dlazy-ai/ai-ppt-slides)
- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Files, Images, Guidance]

**Output Format:** [Image-based PowerPoint (.pptx) assembled from PNG slide images, with optional Markdown outline and speaker notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Slides are full-page images; individual text, charts, and shapes are not separately editable.]

## Skill Version(s):

1.0.33 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
