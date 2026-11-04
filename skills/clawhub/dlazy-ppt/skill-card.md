## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can turn articles, reports, papers, notes, or outlines into visually consistent PowerPoint decks where each slide is a generated image. It is suited to presentations that do not require individually editable text, charts, or shapes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connection check can expose the API key through insecure URLs or authenticated cross-origin or downgrade redirects.

Mitigation: Use a version that enforces HTTPS and blocks authenticated cross-origin and downgrade redirects; the default URL alone does not address redirect handling.

Risk: Confidential figures may be exposed through image-link access or retention when submitted for processing.

Mitigation: Submit only material permitted for dLazy to process, and verify image-link access and retention before uploading confidential figures.

Risk: Dependency versions and remote storage protections remain unverified.

Mitigation: Verify dependency versions and remote storage protections before using sensitive presentation material.

## Reference(s):

- [Project homepage](https://github.com/dlazy-ai/ai-ppt-slides)

## Skill Output:

**Output Type(s):** [PowerPoint files (PPT/PPTX), Slide images, Markdown guidance]

**Output Format:** [Image-based PPTX assembled from full-slide images; Markdown project notes and speaker notes may accompany the deck.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each slide is a single image, so its text and visual elements are not individually editable.]

## Skill Version(s):

1.0.28 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
